#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fontTools import ttLib


def get_font_report(fontpath):
    tt = ttLib.TTFont(fontpath)
    # The file path header
    report_string = " \n"
    report_string = report_string + "=== " + fontpath + " ===\n"
    namerecord_list = tt['name'].__dict__['names']
    # The version string
    for needle in namerecord_list:
        if needle.__dict__['langID'] == 0 and needle.__dict__['nameID'] == 5:
            report_string = report_string + needle.__dict__['string'] + "\n\n"
    # The vertical metrics strings
    report_string = report_string + "[OS/2] TypoAscender: \t" + str(tt['OS/2'].__dict__['sTypoAscender']) + "\n"
    report_string = report_string + "[OS/2] TypoDescender: \t" + str(tt['OS/2'].__dict__['sTypoDescender']) + "\n"
    report_string = report_string + "[OS/2] WinAscent: \t" + str(tt['OS/2'].__dict__['usWinAscent']) + "\n"
    report_string = report_string + "[OS/2] WinDescent: \t" + str(tt['OS/2'].__dict__['usWinDescent']) + "\n"
    report_string = report_string + "[hhea] Ascent: \t\t" + str(tt['hhea'].__dict__['ascent']) + "\n"
    report_string = report_string + "[hhea] Descent: \t" + str(tt['hhea'].__dict__['descent']) + "\n\n"
    report_string = report_string + "[OS/2] TypoLineGap: \t" + str(tt['OS/2'].__dict__['sTypoLineGap'])

    return report_string


def modify_font(fontpath, percent):
    tt = ttLib.TTFont(fontpath)
    os2_typo_ascender = tt['OS/2'].__dict__['sTypoAscender']
    os2_typo_descender = tt['OS/2'].__dict__['sTypoDescender']

    factor = 1.0 * int(percent) / 100

    if os2_typo_descender < 0:
        os2_typo_linegap = int(factor * (os2_typo_ascender + -(os2_typo_descender)))
        total_height = os2_typo_ascender + -(os2_typo_descender) + os2_typo_linegap
    else:
        os2_typo_linegap = int(factor * (os2_typo_ascender + os2_typo_descender))
        total_height = os2_typo_ascender + os2_typo_descender + os2_typo_linegap

    hhea_ascender = int(os2_typo_ascender + 0.5 * os2_typo_linegap)
    hhea_descender = -(total_height - hhea_ascender)

    os2_win_ascent = hhea_ascender
    os2_win_descent = -hhea_descender

    print(os2_typo_ascender)
    print(os2_typo_descender)
    print(factor)
    print(os2_typo_linegap)
    print(total_height)
    print(hhea_ascender)
    print(hhea_descender)
    print(os2_win_ascent)
    print(os2_win_descent)