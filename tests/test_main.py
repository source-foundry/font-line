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
