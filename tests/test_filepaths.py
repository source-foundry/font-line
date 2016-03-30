#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import pytest

from fontline.commands import get_linegap_percent_filepath

test_filepath_one = "test.ttf"
test_filepath_two = "./test.ttf"
test_filepath_three = "/dir1/dir2/test.ttf"
test_filepath_four = "~/dir1/dir2/test.ttf"
percent_value = "10"

expected_linegap_basename = "test-linegap" + percent_value + ".ttf"

expected_testpath_list_one = os.path.split(test_filepath_one)
expected_testpath_list_two = os.path.split(test_filepath_two)
expected_testpath_list_three = os.path.split(test_filepath_three)
expected_testpath_list_four = os.path.split(test_filepath_four)

expected_testpath_one = os.path.join(expected_testpath_list_one[0], expected_linegap_basename)
expected_testpath_two = os.path.join(expected_testpath_list_two[0], expected_linegap_basename)
expected_testpath_three = os.path.join(expected_testpath_list_three[0], expected_linegap_basename)
expected_testpath_four = os.path.join(expected_testpath_list_four[0], expected_linegap_basename)


def test_linegap_outfile_filepath_basename():
    response = get_linegap_percent_filepath(test_filepath_one, percent_value)
    assert response == expected_testpath_one


def test_linegap_outfile_filepath_samedir_withdotsyntax():
    response = get_linegap_percent_filepath(test_filepath_two, percent_value)
    assert response == expected_testpath_two


def test_linegap_outfile_filepath_differentdir_fromroot():
    response = get_linegap_percent_filepath(test_filepath_three, percent_value)
    assert response == expected_testpath_three


def test_linegap_outfile_filepath_differentdir_fromuser():
    response = get_linegap_percent_filepath(test_filepath_four, percent_value)
    assert response == expected_testpath_four

