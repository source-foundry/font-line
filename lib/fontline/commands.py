#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fontTools import ttLib

from standardstreams import stdout


def get_font_report(fontpath):
    tt = ttLib.TTFont(fontpath)
    # The file path header
    report_string = " \n"
    report_string = report_string + "=== " + fontpath + " ===\n"
    namerecord_list = tt['name'].__dict__['names']
    # The version string
    for needle in namerecord_list:
        if needle.__dict__['langID'] == 0 and needle.__dict__['nameID'] == 5:
            report_string = report_string + needle.__dict__['string']

    return report_string
