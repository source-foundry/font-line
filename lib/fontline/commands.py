#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os.path

from fontTools import ttLib
from fontline.utilities import get_sha1

from standardstreams import stderr


def get_font_report(fontpath):
    tt = ttLib.TTFont(fontpath)

    # Vertical metrics values as integers
    os2_typo_ascender = tt['OS/2'].sTypoAscender
    os2_typo_descender = tt['OS/2'].sTypoDescender
    os2_win_ascent = tt['OS/2'].usWinAscent
    os2_win_descent = tt['OS/2'].usWinDescent
    os2_typo_linegap = tt['OS/2'].sTypoLineGap
    hhea_ascent = tt['hhea'].ascent
    hhea_descent = tt['hhea'].descent
    hhea_linegap = tt['hhea'].lineGap
    ymax = tt['head'].yMax
    ymin = tt['head'].yMin
    units_per_em = tt['head'].unitsPerEm

    # Calculated values
    os2_typo_total_height = os2_typo_ascender + -(os2_typo_descender)
    os2_win_total_height = os2_win_ascent + os2_win_descent
    hhea_total_height = hhea_ascent + -(hhea_descent)
    typo_to_upm = 1.0 * (os2_typo_linegap + os2_typo_total_height) / units_per_em
    winascdesc_to_upm = 1.0 * os2_win_total_height / units_per_em
    hheaascdesc_to_upm = 1.0 * hhea_total_height / units_per_em

    # The file path header
    report = [" "]
    report.append("=== " + fontpath + " ===")
    namerecord_list = tt['name'].names
    # The version string
    for needle in namerecord_list:
        if needle.langID == 0 and needle.nameID == 5:
            report.append(needle.toStr())
            break
    # The SHA1 string
    report.append("SHA1: " + get_sha1(fontpath))
    report.append("")
    # The vertical metrics strings
    report.append("--- Metrics ---")
    report.append("[head] Units per Em: \t{}".format(units_per_em))
    report.append("[head] yMax: \t\t{}".format(ymax))
    report.append("[head] yMin: \t\t{}".format(ymin))
    report.append("[OS/2] TypoAscender: \t{}".format(os2_typo_ascender))
    report.append("[OS/2] TypoDescender: \t{}".format(os2_typo_descender))
    report.append("[OS/2] WinAscent: \t{}".format(os2_win_ascent))
    report.append("[OS/2] WinDescent: \t{}".format(os2_win_descent))
    report.append("[hhea] Ascent: \t\t{}".format(hhea_ascent))
    report.append("[hhea] Descent: \t{}".format(hhea_descent))
    report.append("")
    report.append("[hhea] LineGap: \t{}".format(hhea_linegap))
    report.append("[OS/2] TypoLineGap: \t{}".format(os2_typo_linegap))
    report.append("")
    report.append("--- Height Calculations by Table Values ---")
    report.append("[OS/2] TypoAscender to TypoDescender: \t{}".format(os2_typo_total_height))
    report.append("[OS/2] WinAscent to WinDescent: \t{}".format(os2_win_total_height))
    report.append("[hhea] Ascent to Descent: \t\t{}".format(hhea_total_height))
    report.append("")
    report.append("--- Delta Values ---")
    report.append("WinAscent to TypoAscender: \t{}".format(os2_win_ascent - os2_typo_ascender))
    report.append("Ascent to TypoAscender: \t{}".format(hhea_ascent - os2_typo_ascender))
    report.append("WinDescent to TypoDescender: \t{}".format(os2_win_descent - -(os2_typo_descender)))
    report.append("Descent to TypoDescender: \t{}".format(os2_typo_descender - hhea_descent))
    report.append("")
    report.append("--- Ratios ---")
    report.append("(Typo Asc + Desc + Linegap) / UPM: \t{0:.3g}".format(typo_to_upm))
    report.append("(winAsc + winDesc) / UPM: \t\t{0:.3g}".format(winascdesc_to_upm))
    report.append("(hhea Asc + Desc) / UPM: \t\t{0:.3g}".format(hheaascdesc_to_upm))

    return "\n".join(report)


def modify_linegap_percent(fontpath, percent):
    try:
        tt = ttLib.TTFont(fontpath)

        # get observed start values from the font
        os2_typo_ascender = tt['OS/2'].sTypoAscender
        os2_typo_descender = tt['OS/2'].sTypoDescender
        os2_typo_linegap = tt['OS/2'].sTypoLineGap
        hhea_ascent = tt['hhea'].ascent
        hhea_descent = tt['hhea'].descent
        units_per_em = tt['head'].unitsPerEm

        # calculate necessary delta values
        os2_typo_ascdesc_delta = os2_typo_ascender + -(os2_typo_descender)
        hhea_ascdesc_delta = hhea_ascent + -(hhea_descent)

        # define percent UPM from command line request
        factor = 1.0 * int(percent) / 100

        # define line spacing units
        line_spacing_units = int(factor * units_per_em)

        # define total height as UPM + line spacing units
        total_height = line_spacing_units + units_per_em

        # height calculations for adjustments
        delta_height = total_height - hhea_ascdesc_delta
        upper_lower_add_units = int(0.5 * delta_height)

        # redefine hhea linegap to 0 in all cases
        hhea_linegap = 0

        # Define metrics based upon original design approach in the font
        # Google metrics approach
        if os2_typo_linegap == 0 and (os2_typo_ascdesc_delta > units_per_em):
            # define values
            os2_typo_ascender += upper_lower_add_units
            os2_typo_descender -= upper_lower_add_units
            hhea_ascent += upper_lower_add_units
            hhea_descent -= upper_lower_add_units
            os2_win_ascent = hhea_ascent
            os2_win_descent = -hhea_descent
        # Adobe metrics approach
        elif os2_typo_linegap == 0 and (os2_typo_ascdesc_delta == units_per_em):
            hhea_ascent += upper_lower_add_units
            hhea_descent -= upper_lower_add_units
            os2_win_ascent = hhea_ascent
            os2_win_descent = -hhea_descent
        else:
            os2_typo_linegap = line_spacing_units
            hhea_ascent = int(os2_typo_ascender + 0.5 * os2_typo_linegap)
            hhea_descent = -(total_height - hhea_ascent)
            os2_win_ascent = hhea_ascent
            os2_win_descent = -hhea_descent

        # define updated values from above calculations
        tt['hhea'].lineGap = hhea_linegap
        tt['OS/2'].sTypoAscender = os2_typo_ascender
        tt['OS/2'].sTypoDescender = os2_typo_descender
        tt['OS/2'].sTypoLineGap = os2_typo_linegap
        tt['OS/2'].usWinAscent = os2_win_ascent
        tt['OS/2'].usWinDescent = os2_win_descent
        tt['hhea'].ascent = hhea_ascent
        tt['hhea'].descent = hhea_descent

        tt.save(get_linegap_percent_filepath(fontpath, percent))
        return True
    except Exception as e:  # pragma: no cover
        stderr("[font-line] ERROR: Unable to modify the line spacing in the font file '" + fontpath + "'. " + str(e))
        sys.exit(1)


def get_linegap_percent_filepath(fontpath, percent):
    fontpath_list = os.path.split(fontpath)
    font_dirname = fontpath_list[0]
    font_basename = fontpath_list[1]
    basepath_list = font_basename.split(".")
    outfile_basename = basepath_list[0] + "-linegap" + percent + "." + basepath_list[1]
    return os.path.join(font_dirname, outfile_basename)
