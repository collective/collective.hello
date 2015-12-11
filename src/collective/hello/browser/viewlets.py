from plone.app.layout.viewlets.common import ViewletBase
from collective.hello.behaviors.hello import IHello
from datetime import datetime
import pytz

class HelloViewlet(ViewletBase):

    def roomURL(self):
        return "https://appear.in/"+self.context.id

    # Display module

    def enabledModule(self):
        return IHello(self.context).enabledModule

    def currentEvent(self):
        afterStart = (datetime.now(pytz.utc) >= self.context.start)
        beforeEnd = (datetime.now(pytz.utc) <= self.context.end)
        return (beforeEnd and afterStart)

    def displayModule(self):
        return (self.enabledModule() and self.currentEvent())
