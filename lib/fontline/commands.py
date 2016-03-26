#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from fontTools import ttLib
from fontline.utilities import get_sha1

from standardstreams import stderr


def get_font_report(fontpath):
    tt = ttLib.TTFont(fontpath)

    # Vertical metrics values as integers
    os2_typo_ascender = tt['OS/2'].__dict__['sTypoAscender']
    os2_typo_descender = tt['OS/2'].__dict__['sTypoDescender']
    os2_win_ascent = tt['OS/2'].__dict__['usWinAscent']
    os2_win_descent = tt['OS/2'].__dict__['usWinDescent']
    os2_typo_linegap = tt['OS/2'].__dict__['sTypoLineGap']
    hhea_ascent = tt['hhea'].__dict__['ascent']
    hhea_descent = tt['hhea'].__dict__['descent']
    hhea_linegap = tt['hhea'].__dict__['lineGap']
    units_per_em = tt['head'].__dict__['unitsPerEm']

    linegap_to_upm = 1.0 * os2_typo_linegap / units_per_em

    # Calculated values
    os2_typo_total_height = os2_typo_ascender + -(os2_typo_descender)
    os2_win_total_height = os2_win_ascent + os2_win_descent
    hhea_total_height = hhea_ascent + -(hhea_descent)

    # The file path header
    report_string = " \n"
    report_string = report_string + "=== " + fontpath + " ===\n"
    namerecord_list = tt['name'].__dict__['names']
    # The version string
    for needle in namerecord_list:
        if needle.__dict__['langID'] == 0 and needle.__dict__['nameID'] == 5:
            report_string = report_string + str(needle.__dict__['string']) + "\n"
    # The SHA1 string
    report_string = report_string + "SHA1: " + get_sha1(fontpath) + "\n\n"
    # The vertical metrics strings
    report_string = report_string + "[head] Units per Em: \t" + str(units_per_em) + "\n"
    report_string = report_string + "[OS/2] TypoAscender: \t" + str(os2_typo_ascender) + "\n"
    report_string = report_string + "[OS/2] TypoDescender: \t" + str(os2_typo_descender) + "\n"
    report_string = report_string + "[OS/2] WinAscent: \t" + str(os2_win_ascent) + "\n"
    report_string = report_string + "[OS/2] WinDescent: \t" + str(os2_win_descent) + "\n"
    report_string = report_string + "[hhea] Ascent: \t\t" + str(hhea_ascent) + "\n"
    report_string = report_string + "[hhea] Descent: \t" + str(hhea_descent) + "\n\n"
    report_string = report_string + "[hhea] LineGap: \t" + str(hhea_linegap) + "\n"
    report_string = report_string + "[OS/2] TypoLineGap: \t" + str(os2_typo_linegap) + "\n\n"
    report_string = report_string + "--- Height Calculations by Table Values ---" + "\n"
    report_string = report_string + "[OS/2] TypoAscender to TypoDescender: \t" + str(os2_typo_total_height) + "\n"
    report_string = report_string + "[OS/2] WinAscent to WinDescent: \t" + str(os2_win_total_height) + "\n"
    report_string = report_string + "[hhea] Ascent to Descent: \t\t" + str(hhea_total_height) + "\n\n"
    report_string = report_string + "--- Delta Values ---" + "\n"
    report_string = report_string + "WinAscent to TypoAscender: \t" + str(os2_win_ascent - os2_typo_ascender) + "\n"
    report_string = report_string + "Ascent to TypoAscender: \t" + str(hhea_ascent - os2_typo_ascender) + "\n"
    report_string = report_string + "WinDescent to TypoDescender: \t" + str(os2_win_descent - -(os2_typo_descender)) + "\n"
    report_string = report_string + "Descent to TypoDescender: \t" + str(os2_typo_descender - hhea_descent) + "\n\n"
    report_string = report_string + "--- Ratio of TypoLineGap to UPM ---" + "\n"
    report_string = report_string + "TypoLineGap / UPM: \t" + str('{0:.3g}'.format(linegap_to_upm))

    return report_string


def modify_linegap_percent(fontpath, percent):
    try:
        tt = ttLib.TTFont(fontpath)

        # get observed start values from the font
        os2_typo_ascender = tt['OS/2'].__dict__['sTypoAscender']
        os2_typo_descender = tt['OS/2'].__dict__['sTypoDescender']

        # redefine hhea linegap to 0
        hhea_linegap = 0

        factor = 1.0 * int(percent) / 100

        if os2_typo_descender < 0:
            os2_typo_linegap = int(factor * (os2_typo_ascender + -(os2_typo_descender)))
            total_height = os2_typo_ascender + -(os2_typo_descender) + os2_typo_linegap
        else:
            os2_typo_linegap = int(factor * (os2_typo_ascender + os2_typo_descender))
            total_height = os2_typo_ascender + os2_typo_descender + os2_typo_linegap

        hhea_ascent = int(os2_typo_ascender + 0.5 * os2_typo_linegap)
        hhea_descent = -(total_height - hhea_ascent)

        os2_win_ascent = hhea_ascent
        os2_win_descent = -hhea_descent

        # define updated values
        tt['hhea'].__dict__['lineGap'] = hhea_linegap
        tt['OS/2'].__dict__['sTypoLineGap'] = os2_typo_linegap
        tt['OS/2'].__dict__['usWinAscent'] = os2_win_ascent
        tt['OS/2'].__dict__['usWinDescent'] = os2_win_descent
        tt['hhea'].__dict__['ascent'] = hhea_ascent
        tt['hhea'].__dict__['descent'] = hhea_descent

        tt.save(get_linegap_percent_filepath(fontpath, percent))
        return True
    except Exception as e:
        stderr("[font-line] ERROR: Unable to modify the line spacing in the font file '" + fontpath + "'. " + str(e))
        sys.exit(1)


def get_linegap_percent_filepath(fontpath, percent):
    path_list = fontpath.split(".")
    return path_list[0] + "-linegap" + percent + "." + path_list[1]
