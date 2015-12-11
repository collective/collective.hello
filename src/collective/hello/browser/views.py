from Products.Five.browser import BrowserView
from zope.annotation.interfaces import IAnnotations
from zope.component.hooks import getSite
from .. import KEY

import json
import requests
from requests_hawk import HawkAuth

class HelloView(BrowserView):

    def __call__(self):
        if self.request.method == 'POST':
            annotations = IAnnotations(self.context)
            # Get hawk token
            hawkSessionToken = requests.post("https://loop.services.mozilla.com/v0/registration").headers["Hawk-Session-Token"]
            hawkAuth = HawkAuth(hawkSessionToken)
            # Create room - maxSize cannot be greater than 5
            dataRoom = { "roomName": str(self.context.title), "roomOwner": str(getSite().title), "maxSize": 5 }
            loopRoom = requests.post("https://loop.services.mozilla.com/v0/rooms", auth=hawkAuth, data=dataRoom)
            # Store roomToken
            annotations[KEY] = json.loads(loopRoom.content)["roomToken"]
            # Return object with roomToken and credentials
            response_data = {}
            response_data["roomToken"] = json.loads(loopRoom.content)["roomToken"]
            response_data["credentials"] = {}
            response_data["credentials"]["algorithm"] = hawkAuth.credentials['algorithm']
            response_data["credentials"]["id"] = hawkAuth.credentials['id']
            response_data["credentials"]["key"] = hawkAuth.credentials['key']
            return json.dumps(response_data)
        else:
            return None
