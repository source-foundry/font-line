#!/usr/bin/env python3

import os

import pytest
from fontTools.ttLib import TTFont

from fontline.metrics import MetricsObject


@pytest.fixture()
def metricsobject():
    filepath = os.path.join("tests", "testingfiles", "FiraMono-Regular.ttf")
    tt = TTFont(filepath)
    yield MetricsObject(tt, filepath)


@pytest.fixture()
def metricsobject_bit7_clear():
    filepath = os.path.join("tests", "testingfiles", "Hack-Regular.ttf")
    tt = TTFont(filepath)
    yield MetricsObject(tt, filepath)


def test_mo_metadata(metricsobject):
    filepath = os.path.join("tests","testingfiles", "FiraMono-Regular.ttf")
    assert metricsobject.filepath == filepath
    assert metricsobject.version == "Version 3.206"
    assert metricsobject.sha1 == "e2526f6d8ab566afc7cf75ec192c1df30fd5913b"


def test_mo_metricsdata(metricsobject):
    assert metricsobject.units_per_em == 1000
    assert metricsobject.ymax == 1050
    assert metricsobject.ymin == -500
    assert metricsobject.os2_cap_height == 689
    assert metricsobject.os2_x_height == 527
    assert metricsobject.os2_typo_ascender == 935
    assert metricsobject.os2_typo_descender == -265
    assert metricsobject.os2_win_ascent == 935
    assert metricsobject.os2_win_descent == 265
    assert metricsobject.hhea_ascent == 935
    assert metricsobject.hhea_descent == -265
    assert metricsobject.hhea_linegap == 0
    assert metricsobject.os2_typo_linegap == 0


def test_mo_ascent_to_descent_values(metricsobject):
    assert metricsobject.hhea_total_height == 1200
    assert metricsobject.os2_typo_total_height == 1200
    assert metricsobject.os2_win_total_height == 1200


def test_mo_b2bd_values(metricsobject):
    assert metricsobject.hhea_btb_distance == 1200
    assert metricsobject.typo_btb_distance == 1200
    assert metricsobject.win_btb_distance == 1200


def test_mo_fsselection_bit7_set(metricsobject):
    assert metricsobject.fsselection_bit7_set is True


def test_mo_fsselection_bit7_clear(metricsobject_bit7_clear):
    assert metricsobject_bit7_clear.fsselection_bit7_set is False


def test_mo_ratios(metricsobject):
    assert metricsobject.hheaascdesc_to_upm == 1.2
    assert metricsobject.typo_to_upm == 1.2
    assert metricsobject.winascdesc_to_upm == 1.2

