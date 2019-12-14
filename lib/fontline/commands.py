#!/usr/bin/env python3

import sys
import os.path

from fontTools import ttLib
from standardstreams import stderr


from fontline.metrics import MetricsObject


def get_font_report(fontpath):
    tt = ttLib.TTFont(fontpath)
    metrics = MetricsObject(tt, fontpath)

    # The file path header
    report = ["=== " + fontpath + " ==="]

    report.append(metrics.version)

    # The SHA1 string
    report.append("SHA1: " + metrics.sha1)
    report.append("")
    # The vertical metrics strings
    report.append(":" * 50)
    report.append("  Metrics")
    report.append(":" * 50)
    report.append("[head] Units per Em:   {}".format(metrics.units_per_em))
    report.append("[head] yMax:           {}".format(metrics.ymax))
    report.append("[head] yMin:          {}".format(metrics.ymin))
    report.append("[OS/2] CapHeight:      {}".format(metrics.os2_cap_height))
    report.append("[OS/2] xHeight:        {}".format(metrics.os2_x_height))
    report.append("[OS/2] TypoAscender:   {}".format(metrics.os2_typo_ascender))
    report.append("[OS/2] TypoDescender: {}".format(metrics.os2_typo_descender))
    report.append("[OS/2] WinAscent:      {}".format(metrics.os2_win_ascent))
    report.append("[OS/2] WinDescent:     {}".format(metrics.os2_win_descent))
    report.append("[hhea] Ascent:         {}".format(metrics.hhea_ascent))
    report.append("[hhea] Descent:       {}".format(metrics.hhea_descent))
    report.append("")
    report.append("[hhea] LineGap:        {}".format(metrics.hhea_linegap))
    report.append("[OS/2] TypoLineGap:    {}".format(metrics.os2_typo_linegap))
    report.append("")

    report.append(":" * 50)
    report.append("  Ascent to Descent Calculations")
    report.append(":" * 50)
    report.append(
        "[hhea] Ascent to Descent:              {}".format(metrics.hhea_total_height)
    )
    report.append(
        "[OS/2] TypoAscender to TypoDescender:  {}".format(
            metrics.os2_typo_total_height
        )
    )
    report.append(
        "[OS/2] WinAscent to WinDescent:        {}".format(metrics.os2_win_total_height)
    )
    report.append("")

    report.append(":" * 50)
    report.append("  Delta Values")
    report.append(":" * 50)
    report.append(
        "[hhea] Ascent to [OS/2] TypoAscender:       {}".format(
            metrics.hhea_ascent - metrics.os2_typo_ascender
        )
    )
    report.append(
        "[hhea] Descent to [OS/2] TypoDescender:     {}".format(
            metrics.os2_typo_descender - metrics.hhea_descent
        )
    )
    report.append(
        "[OS/2] WinAscent to [OS/2] TypoAscender:    {}".format(
            metrics.os2_win_ascent - metrics.os2_typo_ascender
        )
    )
    report.append(
        "[OS/2] WinDescent to [OS/2] TypoDescender:  {}".format(
            metrics.os2_win_descent + metrics.os2_typo_descender
        )
    )
    report.append("")
    report.append(":" * 50)
    report.append("  Baseline to Baseline Distances")
    report.append(":" * 50)
    report.append("hhea metrics: {}".format(metrics.hhea_btb_distance))
    report.append("typo metrics: {}".format(metrics.typo_btb_distance))
    report.append("win metrics:  {}".format(metrics.win_btb_distance))
    report.append("")
    report.append(
        "[OS/2] fsSelection USE_TYPO_METRICS bit set: {}".format(
            metrics.fsselection_bit7_set
        )
    )
    report.append("")
    report.append(":" * 50)
    report.append("  Ratios")
    report.append(":" * 50)
    report.append("hhea metrics / UPM:  {0:.3g}".format(metrics.hheaascdesc_to_upm))
    report.append("typo metrics / UPM:  {0:.3g}".format(metrics.typo_to_upm))
    report.append("win metrics  / UPM:  {0:.3g}".format(metrics.winascdesc_to_upm))

    return "\n".join(report)


def modify_linegap_percent(fontpath, percent):
    try:
        tt = ttLib.TTFont(fontpath)

        # get observed start values from the font
        os2_typo_ascender = tt["OS/2"].sTypoAscender
        os2_typo_descender = tt["OS/2"].sTypoDescender
        os2_typo_linegap = tt["OS/2"].sTypoLineGap
        hhea_ascent = tt["hhea"].ascent
        hhea_descent = tt["hhea"].descent
        units_per_em = tt["head"].unitsPerEm

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
        tt["hhea"].lineGap = hhea_linegap
        tt["OS/2"].sTypoAscender = os2_typo_ascender
        tt["OS/2"].sTypoDescender = os2_typo_descender
        tt["OS/2"].sTypoLineGap = os2_typo_linegap
        tt["OS/2"].usWinAscent = os2_win_ascent
        tt["OS/2"].usWinDescent = os2_win_descent
        tt["hhea"].ascent = hhea_ascent
        tt["hhea"].descent = hhea_descent

        tt.save(get_linegap_percent_filepath(fontpath, percent))
        return True
    except Exception as e:  # pragma: no cover
        stderr(
            "[font-line] ERROR: Unable to modify the line spacing in the font file '"
            + fontpath
            + "'. "
            + str(e)
        )
        sys.exit(1)


def get_linegap_percent_filepath(fontpath, percent):
    fontpath_list = os.path.split(fontpath)
    font_dirname = fontpath_list[0]
    font_basename = fontpath_list[1]
    basepath_list = font_basename.split(".")
    outfile_basename = basepath_list[0] + "-linegap" + percent + "." + basepath_list[1]
    return os.path.join(font_dirname, outfile_basename)
