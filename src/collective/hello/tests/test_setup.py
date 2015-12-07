# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from collective.hello.testing import COLLECTIVE_HELLO_INTEGRATION_TESTING  # noqa
from plone import api

import unittest2 as unittest


class TestSetup(unittest.TestCase):
    """Test that collective.hello is properly installed."""

    layer = COLLECTIVE_HELLO_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if collective.hello is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('collective.hello'))

    def test_uninstall(self):
        """Test if collective.hello is cleanly uninstalled."""
        self.installer.uninstallProducts(['collective.hello'])
        self.assertFalse(self.installer.isProductInstalled('collective.hello'))

    def test_browserlayer(self):
        """Test that ICollectiveHelloLayer is registered."""
        from collective.hello.interfaces import ICollectiveHelloLayer
        from plone.browserlayer import utils
        self.assertIn(ICollectiveHelloLayer, utils.registered_layers())
