#!/usr/bin/env python3

"""
The app.py module defines a main() function that includes the logic for the `font-line`
command line executable.

This command line executable modifies the line spacing metrics in one or more fonts that
are provided as command
line arguments to the executable.  It currently supports .ttf and .otf font builds.
"""

import sys

from commandlines import Command
from standardstreams import stdout, stderr

from fontline import settings
from fontline.commands import (
    get_font_report,
    modify_linegap_percent,
    get_linegap_percent_filepath,
)
from fontline.utilities import file_exists, is_supported_filetype


def main():
    """Defines the logic for the `font-line` command line executable"""
    c = Command()

    if c.does_not_validate_missing_args():
        stderr(
            "[font-line] ERROR: Please include one or more arguments with your command."
        )
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

    # REPORT sub-command
    if c.subcmd == "report":
        if c.argc < 2:
            stderr(
                "[font-line] ERROR: Missing file path argument(s) after the "
                "report subcommand."
            )
            sys.exit(1)
        else:
            for fontpath in c.argv[1:]:
                # test for existence of file on path
                if file_exists(fontpath):
                    # test that filepath includes file of a supported file type
                    if is_supported_filetype(fontpath):
                        stdout(get_font_report(fontpath))
                    else:
                        stderr(
                            "[font-line] ERROR: '"
                            + fontpath
                            + "' does not appear to be a supported font file type."
                        )
                else:
                    stderr(
                        "[font-line] ERROR: '"
                        + fontpath
                        + "' does not appear to be a valid filepath."
                    )
    # PERCENT sub-command
    elif c.subcmd == "percent":
        if c.argc < 3:
            stderr("[font-line] ERROR: Not enough arguments.")
            sys.exit(1)
        else:
            percent = c.argv[1]
            # test the percent integer argument
            try:
                percent_int = int(
                    percent
                )  # test that the argument can be cast to an integer value
                if percent_int <= 0:
                    stderr(
                        "[font-line] ERROR: Please enter a percent value that is "
                        "greater than zero."
                    )
                    sys.exit(1)
                if percent_int > 100:
                    stdout(
                        "[font-line] Warning: You entered a percent value over 100%. "
                        "Please confirm that this is your intended metrics modification."
                    )
            except ValueError:
                stderr(
                    "[font-line] ERROR: You entered '"
                    + percent
                    + "'. This argument needs to be an integer value."
                )
                sys.exit(1)
            for fontpath in c.argv[2:]:
                if file_exists(fontpath):
                    if is_supported_filetype(fontpath):
                        if modify_linegap_percent(fontpath, percent) is True:
                            outpath = get_linegap_percent_filepath(fontpath, percent)
                            stdout(
                                "[font-line] '"
                                + fontpath
                                + "' successfully modified to '"
                                + outpath
                                + "'."
                            )
                        else:  # pragma: no cover
                            stderr(
                                "[font-line] ERROR: Unsuccessful modification of '"
                                + fontpath
                                + "'."
                            )
                    else:
                        stderr(
                            "[font-line] ERROR: '"
                            + fontpath
                            + "' does not appear to be a supported font file type."
                        )
                else:
                    stderr(
                        "[font-line] ERROR: '"
                        + fontpath
                        + "' does not appear to be a valid filepath."
                    )
    else:
        stderr(
            "[font-lines] ERROR: You used an unsupported argument to the executable. "
            "Please review the `font-line --help` documentation and try again."
        )
        sys.exit(1)
