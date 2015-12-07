from plone.supermodel import model, directives
from plone.autoform.interfaces import IFormFieldProvider
from zope import schema
from zope.interface import alsoProvides


class IHello(model.Schema):

    enabledModule = schema.Bool(
        title=u"Hello join button",
        description=u"Add button to join hello conversation when the event is started",
        required=False,
    )

alsoProvides(IHello, IFormFieldProvider)