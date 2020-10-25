#!/usr/bin/env python3

# ------------------------------------------------------------------------------
# Application Name
# ------------------------------------------------------------------------------
app_name = "font-line"

# ------------------------------------------------------------------------------
# Version Number
# ------------------------------------------------------------------------------
major_version = "3"
minor_version = "1"
patch_version = "3"

# ------------------------------------------------------------------------------
# Help String
# ------------------------------------------------------------------------------

HELP = """====================================================
font-line
Copyright 2019 Christopher Simpkins
MIT License
Source: https://github.com/source-foundry/font-line
====================================================

ABOUT

font-line is a font vertical metrics reporting and line spacing modification tool.

SUB-COMMANDS

  percent - adjust font line spacing to % of UPM value
  report - generate report of font metrics and derived values

OPTIONS

  -h | --help        display application help
  -v | --version     display application version
       --usage       display usage information

USAGE

 $ font-line report [fontpath 1] <fontpath ...>
 $ font-line percent [integer] [fontpath 1] <fontpath ...>
 $ font-line [-v|-h] [--help|--usage|--version]

Reports are sent to the standard output stream with the `report` sub-command.

Original font files are not modified when you use the `percent` sub-command.  Instead
a new file write occurs on a path that is displayed in the standard output stream when
completed.  No modifications are made to the original glyph set or hints associated with
the original font build.

For more information about the OpenType table modifications that occur, please see the
project documentation at:

https://github.com/source-foundry/font-line"""

# ------------------------------------------------------------------------------
# Version String
# ------------------------------------------------------------------------------

VERSION = "font-line v" + major_version + "." + minor_version + "." + patch_version


# ------------------------------------------------------------------------------
# Usage String
# ------------------------------------------------------------------------------

USAGE = """
Usage: font-line [subcommand] <arg> [font path 1] <font path 2> <font path ...>"""
