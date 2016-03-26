#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import pytest
import os.path

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
    filepath = os.path.join('testingfiles', 'missing.txt')
    sys.argv = ['font-line', 'report', filepath]
    main()
    out, err = capsys.readouterr()
    assert err.startswith("[font-line] ERROR: ")

