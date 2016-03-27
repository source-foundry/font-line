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


def test_report_cmd_too_few_args(capsys):
    with pytest.raises(SystemExit):
        from fontline.app import main
        sys.argv = ['font-line', 'report']
        main()
        out, err = capsys.readouterr()
        assert err == "[font-line] ERROR: Missing file path argument(s) after the report subcommand."


def test_report_cmd_missing_file_request(capsys):
    from fontline.app import main
    sys.argv = ['font-line', 'report', 'missing.txt']
    main()
    out, err = capsys.readouterr()
    assert err.startswith("[font-line] ERROR: ")


def test_report_cmd_unsupported_filetype(capsys):
    from fontline.app import main
    filepath = os.path.join('tests', 'testingfiles', 'bogus.txt')
    sys.argv = ['font-line', 'report', filepath]
    main()
    out, err = capsys.readouterr()
    assert err.startswith("[font-line] ERROR: ")


def test_report_cmd_reportstring_filename(capsys):
    from fontline.app import main
    filepath = os.path.join('tests', 'testingfiles', 'Hack-Regular.ttf')
    sys.argv = ['font-line', 'report', filepath]
    main()
    out, err = capsys.readouterr()
    assert "Hack-Regular.ttf " in out


def test_report_cmd_reportstring_version(capsys):
    from fontline.app import main
    filepath = os.path.join('tests', 'testingfiles', 'Hack-Regular.ttf')
    sys.argv = ['font-line', 'report', filepath]
    main()
    out, err = capsys.readouterr()
    assert "Version 2.020;DEV-03192016;" in out


def test_report_cmd_reportstring_sha1(capsys):
    from fontline.app import main
    filepath = os.path.join('tests', 'testingfiles', 'Hack-Regular.ttf')
    sys.argv = ['font-line', 'report', filepath]
    main()
    out, err = capsys.readouterr()
    assert "SHA1: 638f033cc1b6a21597359278bee62cf7e96557ff" in out


def test_report_cmd_reportstring_upm(capsys):
    from fontline.app import main
    filepath = os.path.join('tests', 'testingfiles', 'Hack-Regular.ttf')
    sys.argv = ['font-line', 'report', filepath]
    main()
    out, err = capsys.readouterr()
    assert "[head] Units per Em: \t2048" in out


def test_report_cmd_reportstring_typoascender(capsys):
    from fontline.app import main
    filepath = os.path.join('tests', 'testingfiles', 'Hack-Regular.ttf')
    sys.argv = ['font-line', 'report', filepath]
    main()
    out, err = capsys.readouterr()
    assert "[OS/2] TypoAscender: \t1556" in out


def test_report_cmd_reportstring_typodescender(capsys):
    from fontline.app import main
    filepath = os.path.join('tests', 'testingfiles', 'Hack-Regular.ttf')
    sys.argv = ['font-line', 'report', filepath]
    main()
    out, err = capsys.readouterr()
    assert "[OS/2] TypoDescender: \t-492" in out


def test_report_cmd_reportstring_winascent(capsys):
    from fontline.app import main
    filepath = os.path.join('tests', 'testingfiles', 'Hack-Regular.ttf')
    sys.argv = ['font-line', 'report', filepath]
    main()
    out, err = capsys.readouterr()
    assert "[OS/2] WinAscent: \t1901" in out


def test_report_cmd_reportstring_windescent(capsys):
    from fontline.app import main
    filepath = os.path.join('tests', 'testingfiles', 'Hack-Regular.ttf')
    sys.argv = ['font-line', 'report', filepath]
    main()
    out, err = capsys.readouterr()
    assert "[OS/2] WinDescent: \t483" in out


def test_report_cmd_reportstring_ascent(capsys):
    from fontline.app import main
    filepath = os.path.join('tests', 'testingfiles', 'Hack-Regular.ttf')
    sys.argv = ['font-line', 'report', filepath]
    main()
    out, err = capsys.readouterr()
    assert "[hhea] Ascent: \t\t1901" in out


def test_report_cmd_reportstring_descent(capsys):
    from fontline.app import main
    filepath = os.path.join('tests', 'testingfiles', 'Hack-Regular.ttf')
    sys.argv = ['font-line', 'report', filepath]
    main()
    out, err = capsys.readouterr()
    assert "[hhea] Descent: \t-483" in out


def test_report_cmd_reportstring_linegap(capsys):
    from fontline.app import main
    filepath = os.path.join('tests', 'testingfiles', 'Hack-Regular.ttf')
    sys.argv = ['font-line', 'report', filepath]
    main()
    out, err = capsys.readouterr()
    assert "[hhea] LineGap: \t0" in out


def test_report_cmd_reportstring_typolinegap(capsys):
    from fontline.app import main
    filepath = os.path.join('tests', 'testingfiles', 'Hack-Regular.ttf')
    sys.argv = ['font-line', 'report', filepath]
    main()
    out, err = capsys.readouterr()
    assert "[hhea] TypoLineGap: \t0" in out


def test_report_cmd_reportstring_typoA_typoD(capsys):
    from fontline.app import main
    filepath = os.path.join('tests', 'testingfiles', 'Hack-Regular.ttf')
    sys.argv = ['font-line', 'report', filepath]
    main()
    out, err = capsys.readouterr()
    assert "[OS/2] TypoAscender to TypoDescender: \t2048" in out


def test_report_cmd_reportstring_winA_winD(capsys):
    from fontline.app import main
    filepath = os.path.join('tests', 'testingfiles', 'Hack-Regular.ttf')
    sys.argv = ['font-line', 'report', filepath]
    main()
    out, err = capsys.readouterr()
    assert "[OS/2] WinAscent to WinDescent: \t2384" in out


def test_report_cmd_reportstring_ascent_descent(capsys):
    from fontline.app import main
    filepath = os.path.join('tests', 'testingfiles', 'Hack-Regular.ttf')
    sys.argv = ['font-line', 'report', filepath]
    main()
    out, err = capsys.readouterr()
    assert "[hhea] Ascent to Descent: \t\t2384" in out
