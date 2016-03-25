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
