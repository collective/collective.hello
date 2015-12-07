from Products.Five.browser import BrowserView
from zope.annotation.interfaces import IAnnotations
from .. import KEY

class HelloView(BrowserView):

    def __call__(self):
        annotations = IAnnotations(self.context)
        if self.request.method == 'POST':
            roomId = self.request.get("roomId")
            annotations[KEY] = roomId
        return annotations[KEY]
