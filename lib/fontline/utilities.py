#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


def file_exists(filepath):
    """Tests for existence of a file on the string filepath"""
    if os.path.exists(filepath) and os.path.isfile(filepath):  # test that exists and is a file
        return True
    else:
        return False


def is_supported_filetype(filepath):
    """Tests file extension to determine appropriate file type for the application"""
    testpath = filepath.lower()
    if testpath.endswith('.ttf') or testpath.endswith('.otf'):
        return True
    else:
        return False
