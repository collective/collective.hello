# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2
from zope.configuration import xmlconfig

import collective.hello


class CollectiveHelloLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        xmlconfig.file(
            'configure.zcml',
            collective.hello,
            context=configurationContext
        )

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.hello:default')


COLLECTIVE_HELLO_FIXTURE = CollectiveHelloLayer()


COLLECTIVE_HELLO_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_HELLO_FIXTURE,),
    name='CollectiveHelloLayer:IntegrationTesting'
)


COLLECTIVE_HELLO_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_HELLO_FIXTURE,),
    name='CollectiveHelloLayer:FunctionalTesting'
)


COLLECTIVE_HELLO_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        COLLECTIVE_HELLO_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='CollectiveHelloLayer:AcceptanceTesting'
)
