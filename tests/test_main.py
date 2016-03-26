#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import pytest


# ///////////////////////////////////////////////////////
#
# pytest capsys capture tests
#    confirms capture of std output and std error streams
#
# ///////////////////////////////////////////////////////

def test_pytest_capsys(capsys):
    print("bogus text for a test")
    sys.stderr.write("more text for a test")
    out, err = capsys.readouterr()
    assert out == "bogus text for a test\n"
    assert out != "something else"
    assert err == "more text for a test"
    assert err != "something else"


# ///////////////////////////////////////////////////////
#
# Standard output tests for help, usage, version
#
# ///////////////////////////////////////////////////////

def test_fontline_commandline_shorthelp(capsys):
    with pytest.raises(SystemExit):
        from fontline.app import main
        sys.argv = ['font-line', '-h']
        main()
        out, err = capsys.readouterr()
        assert out.startswith("====================================================") is True
        assert out.endswith("https://github.com/source-foundry/font-line") is True


def test_fontline_commandline_longhelp(capsys):
    with pytest.raises(SystemExit):
        from fontline.app import main
        sys.argv = ['font-line', '--help']
        main()
        out, err = capsys.readouterr()
        assert out.startswith("====================================================") is True
        assert out.endswith("https://github.com/source-foundry/font-line") is True


def test_fontline_commandline_longusage(capsys):
    with pytest.raises(SystemExit):
        from fontline.app import main
        sys.argv = ['font-line', '--usage']
        main()
        out, err = capsys.readouterr()
        assert out.endswith("Usage: font-line [subcommand] <arg> [font path 1] <font path 2> <font path ...>") is True


def test_fontline_commandline_shortversion(capsys):
    with pytest.raises(SystemExit):
        from fontline.app import main
        from fontline.app import settings
        sys.argv = ['font-line', '-v']
        main()
        out, err = capsys.readouterr()
        assert out == settings.VERSION


def test_fontline_commandline_longversion(capsys):
    with pytest.raises(SystemExit):
        from fontline.app import main
        from fontline.app import settings
        sys.argv = ['font-line', '--version']
        main()
        out, err = capsys.readouterr()
        assert out == settings.VERSION


# ///////////////////////////////////////////////////////
#
# Command line argument error test
#
# ///////////////////////////////////////////////////////

def test_fontline_commandline_notenough_args(capsys):
    with pytest.raises(SystemExit):
        from fontline.app import main
        from fontline.app import settings
        sys.argv = ['font-line']
        main()
        out, err = capsys.readouterr()
        assert err == "[font-line] ERROR: Please include one or more arguments with your command."


