from plone.app.layout.viewlets.common import ViewletBase
from collective.hello.behaviors.hello import IHello
from zope.annotation.interfaces import IAnnotations
from datetime import datetime
from plone import api
from .. import KEY
import pytz

class HelloViewlet(ViewletBase):

    def authenticator(self):
        authenticator = self.context.restrictedTraverse("@@authenticator")
        return authenticator.token()

    def roomURL(self):
        annotations = IAnnotations(self.context)
        return "https://hello.firefox.com/"+annotations[KEY]

    # Display module

    def enabledModule(self):
        return IHello(self.context).enabledModule

    def currentEvent(self):
        afterStart = (datetime.now(pytz.utc) >= self.context.start)
        beforeEnd = (datetime.now(pytz.utc) <= self.context.end)
        return (beforeEnd and afterStart)

    def displayModule(self):
        return (self.enabledModule() and self.currentEvent())


    # Display join button

    def existingHelloConversation(self):
        annotations = IAnnotations(self.context)
        return KEY in annotations and annotations[KEY]

    def displayJoinButton(self):
        return (self.displayModule() and self.existingHelloConversation())


    # Display create room button

    def sufficientPermissionsToCreate(self):
        if not api.user.is_anonymous():
            return (('Manager' in api.user.get_roles()) or ('Owner' in api.user.get_roles()))
        else:
            return False

    def displayCreateButton(self):
        return (self.displayModule() and (not self.existingHelloConversation()) and self.sufficientPermissionsToCreate())
