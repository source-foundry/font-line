#!/usr/bin/env python
# -*- coding: utf-8 -*-

from commandlines import Command
from fontlines import settings
from standardstreams import stdout, stderr


def main():
    c = Command()

    if c.is_help_request():
        stdout(settings.HELP)


if __name__ == '__main__':
    main()
