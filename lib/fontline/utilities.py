#!/usr/bin/env python3

import os
import hashlib


def file_exists(filepath):
    """Tests for existence of a file on the string filepath"""
    if os.path.exists(filepath) and os.path.isfile(
        filepath
    ):  # test that exists and is a file
        return True
    else:
        return False


def is_supported_filetype(filepath):
    """Tests file extension to determine appropriate file type for the application"""
    testpath = filepath.lower()
    if testpath.endswith(".ttf") or testpath.endswith(".otf"):
        return True
    else:
        return False


def get_sha1(filepath):
    with open(filepath, "rb") as bin_reader:
        data = bin_reader.read()
    return hashlib.sha1(data).hexdigest()
