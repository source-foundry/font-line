#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
The app.py module defines a main() function that includes the logic for the `font-line` command line executable.

This command line executable modifies the line spacing metrics in one or more fonts that are provided as command
line arguments to the executable.  It currently supports .ttf and .otf font builds.
"""

import sys

from fontTools import ttLib

from commandlines import Command
from fontline import settings
from fontline.utilities import file_exists
from standardstreams import stdout, stderr


def main():
    """Defines the logic for the `font-line` command line executable"""
    c = Command()

    if c.does_not_validate_missing_args():
        stderr("[font-line] ERROR: please include one or more arguments with your command.\n")
        sys.exit(1)

    if c.is_help_request():
        stdout(settings.HELP)
        sys.exit(0)
    elif c.is_version_request():
        stdout(settings.VERSION)
        sys.exit(0)
    elif c.is_usage_request():
        stdout(settings.USAGE)
        sys.exit(0)

    if c.subcmd == "report":
        if c.argc < 2:
            stderr("[font-line] ERROR: missing file path argument(s) after the report subcommand.")
            sys.exit(1)
        else:
            for fontpath in c.argv[1:]:
                # test for existence of file on path
                if file_exists(fontpath):
                    testpath = fontpath.lower()
                    if testpath.endswith(".ttf") or testpath.endswith(".otf"):
                        stdout("TRUE")
                    else:
                        stderr("[font-line] '" + fontpath + "' does not appear to be a supported file type.")
                else:
                    stderr("[font-line] ERROR: '" + fontpath + "' does not appear to be a valid filepath." )
    elif c.subcmd == "mod":
        pass
    else:
        stderr("[font-lines] ERROR: You used an unsupported argument to the executable. Please review the"
               " `font-line --help` documentation and try again.")
        sys.exit(1)
