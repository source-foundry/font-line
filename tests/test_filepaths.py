#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import pytest

from fontline.commands import get_linegap_percent_filepath

test_filepath_one = "test.ttf"
test_filepath_two = "./test.ttf"
test_filepath_three = "/dir1/dir2/test.ttf"
test_filepath_four = "~/dir1/dir2/test.ttf"
percent_value = "10"


def test_linegap_outfile_filepath_basename():
    response = get_linegap_percent_filepath(test_filepath_one, percent_value)
    assert response == "test-linegap10.ttf"


def test_linegap_outfile_filepath_samedir_withdotsyntax():
    response = get_linegap_percent_filepath(test_filepath_two, percent_value)
    assert response == "./test-linegap10.ttf"


def test_linegap_outfile_filepath_differentdir_fromroot():
    response = get_linegap_percent_filepath(test_filepath_three, percent_value)
    assert response == "/dir1/dir2/test-linegap10.ttf"


def test_linegap_outfile_filepath_differentdir_fromuser():
    response = get_linegap_percent_filepath(test_filepath_four, percent_value)
    assert response == "~/dir1/dir2/test-linegap10.ttf"

