#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import pytest
import os.path
import os
import shutil
from fontTools import ttLib

from fontline.utilities import file_exists

# ///////////////////////////////////////////////////////
#
# utility functions for module tests
#
# ///////////////////////////////////////////////////////


def create_test_file(filepath):
    filepath_list = filepath.split(".")
    testpath = filepath_list[0] + "-test." + filepath_list[1]
    shutil.copyfile(filepath, testpath)
    return True


def erase_test_file(filepath):
    os.remove(filepath)
    return True


# ///////////////////////////////////////////////////////
#
# percent sub-command command line logic tests
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


# ///////////////////////////////////////////////////////
#
# percent sub-command command functionality tests
#
# ///////////////////////////////////////////////////////

def test_percent_cmd_ttf_file_10_percent(capsys):
    try:
        from fontline.app import main
        fontpath = os.path.join('tests', 'testingfiles', 'Hack-Regular.ttf')
        testpath = os.path.join('tests', 'testingfiles', 'Hack-Regular-test.ttf')
        newfont_path = os.path.join('tests', 'testingfiles', 'Hack-Regular-test-linegap10.ttf')
        create_test_file(fontpath)
        assert file_exists(testpath) is True
        sys.argv = ['font-line', 'percent', '10', testpath]
        main()

        assert file_exists(newfont_path)

        tt = ttLib.TTFont(newfont_path)

        os2_typo_ascender = tt['OS/2'].__dict__['sTypoAscender']
        os2_typo_descender = tt['OS/2'].__dict__['sTypoDescender']
        os2_win_ascent = tt['OS/2'].__dict__['usWinAscent']
        os2_win_descent = tt['OS/2'].__dict__['usWinDescent']
        os2_typo_linegap = tt['OS/2'].__dict__['sTypoLineGap']
        hhea_ascent = tt['hhea'].__dict__['ascent']
        hhea_descent = tt['hhea'].__dict__['descent']
        hhea_linegap = tt['hhea'].__dict__['lineGap']
        units_per_em = tt['head'].__dict__['unitsPerEm']

        assert os2_typo_ascender == 1556
        assert os2_typo_descender == -492
        assert os2_win_ascent == 1658
        assert os2_win_descent == 594
        assert units_per_em == 2048
        assert os2_typo_linegap == 204
        assert hhea_ascent == 1658
        assert hhea_descent == -594
        assert hhea_linegap == 0

        erase_test_file(testpath)
        erase_test_file(newfont_path)
    except Exception as e:
        # cleanup test files
        if file_exists(testpath):
            erase_test_file(testpath)
        if file_exists(newfont_path):
            erase_test_file(newfont_path)
        raise e


def test_percent_cmd_otf_file_10_percent(capsys):
    try:
        from fontline.app import main
        fontpath = os.path.join('tests', 'testingfiles', 'Hack-Regular.otf')
        testpath = os.path.join('tests', 'testingfiles', 'Hack-Regular-test.otf')
        newfont_path = os.path.join('tests', 'testingfiles', 'Hack-Regular-test-linegap10.otf')
        create_test_file(fontpath)
        assert file_exists(testpath) is True
        sys.argv = ['font-line', 'percent', '10', testpath]
        main()

        assert file_exists(newfont_path)

        tt = ttLib.TTFont(newfont_path)

        os2_typo_ascender = tt['OS/2'].__dict__['sTypoAscender']
        os2_typo_descender = tt['OS/2'].__dict__['sTypoDescender']
        os2_win_ascent = tt['OS/2'].__dict__['usWinAscent']
        os2_win_descent = tt['OS/2'].__dict__['usWinDescent']
        os2_typo_linegap = tt['OS/2'].__dict__['sTypoLineGap']
        hhea_ascent = tt['hhea'].__dict__['ascent']
        hhea_descent = tt['hhea'].__dict__['descent']
        hhea_linegap = tt['hhea'].__dict__['lineGap']
        units_per_em = tt['head'].__dict__['unitsPerEm']

        assert os2_typo_ascender == 1556
        assert os2_typo_descender == -492
        assert os2_win_ascent == 1658
        assert os2_win_descent == 594
        assert units_per_em == 2048
        assert os2_typo_linegap == 204
        assert hhea_ascent == 1658
        assert hhea_descent == -594
        assert hhea_linegap == 0

        erase_test_file(testpath)
        erase_test_file(newfont_path)
    except Exception as e:
        # cleanup test files
        if file_exists(testpath):
            erase_test_file(testpath)
        if file_exists(newfont_path):
            erase_test_file(newfont_path)
        raise e