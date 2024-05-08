"""Manifest Regression Tests
"""

import importlib
from os import path
import unittest
import sys
sys.path.append('../')
import sherlock as sh
from sites import SitesInformation


"""Test for some fatal changes to the data.json target manifest

Failure of these tests should not be a blocker in every scenario,
but they are a warning that users may experience breaking changes
when running without the use of --local.

Those breaking changes may be better dealt with alongside a
bump in version number, which alerts the user of an update.

"""
class TestLocalManifest(unittest.TestCase):
    """Test fails on fatals during parsing.
    Caught exceptions will not cause a failure here, as those are
    not breaking to users with the current HEAD either.
    """
    def test_parse_local_manifest(self):
        sites = SitesInformation(
            path.join(path.dirname(__file__), "../resources/data.json")
        )
        sites.remove_nsfw_sites
        return
