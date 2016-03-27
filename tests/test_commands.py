#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import pytest

from fontline.commands import get_linegap_percent_filepath


def test_commands_function_getlg_percent_filepath():
    response = get_linegap_percent_filepath("Test.ttf", "20")
    assert response == "Test-linegap20.ttf"

