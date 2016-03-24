#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from fontTools import ttLib

from commandlines import Command
from fontline import settings
from standardstreams import stdout, stderr


def main():
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





