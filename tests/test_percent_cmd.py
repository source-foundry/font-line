#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import pytest
import os.path
import os

# ///////////////////////////////////////////////////////
#
# report sub-command tests
#
# ///////////////////////////////////////////////////////


def test_percent_cmd_too_few_args(capsys):
    with pytest.raises(SystemExit):
        from fontline.app import main
        sys.argv = ['font-line', 'percent']
        main()
        out, err = capsys.readouterr()
        assert err == "[font-line] ERROR: Not enough arguments."


def test_percent_cmd_too_few_args_two(capsys):
    with pytest.raises(SystemExit):
        from fontline.app import main
        sys.argv = ['font-line', 'percent', '10']
        main()
        out, err = capsys.readouterr()
        assert err == "[font-line] ERROR: Not enough arguments."


def test_percent_cmd_percent_arg_not_integer(capsys):
    with pytest.raises(SystemExit):
        from fontline.app import main
        sys.argv = ['font-line', 'percent', 'astring', 'Test.ttf']
        main()
        out, err = capsys.readouterr()
        assert err.startswith("[font-line] ERROR: You entered ") is True


def test_percent_cmd_percent_arg_less_zero(capsys):
    with pytest.raises(SystemExit):
        from fontline.app import main
        sys.argv = ['font-line', 'percent', '-1', 'Test.ttf']
        main()
        out, err = capsys.readouterr()
        assert err == "[font-line] ERROR: Please enter a percent value that is greater than zero."


def test_percent_cmd_percent_arg_over_hundred(capsys):
    from fontline.app import main
    sys.argv = ['font-line', 'percent', '200', 'Test.ttf']
    main()
    out, err = capsys.readouterr()
    assert out.startswith("[font-line] Warning: You entered a percent value over 100%.")


def test_percent_cmd_font_file_missing(capsys):
    from fontline.app import main
    sys.argv = ['font-line', 'percent', '20', 'Test.ttf']
    main()
    out, err = capsys.readouterr()
    assert ("does not appear to be a valid filepath" in err) is True


def test_percent_cmd_font_file_wrong_filetype(capsys):
    from fontline.app import main
    testfile_path = os.path.join("tests", "testingfiles", "bogus.txt")
    sys.argv = ['font-line', 'percent', '20', testfile_path]
    main()
    out, err = capsys.readouterr()
    assert ("does not appear to be a supported font file type." in err) is True
