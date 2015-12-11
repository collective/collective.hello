from plone.supermodel import model, directives
from plone.autoform.interfaces import IFormFieldProvider
from zope import schema
from zope.interface import alsoProvides


class IHello(model.Schema):

    enabledModule = schema.Bool(
        title=u"Video conversation",
        description=u"Add appear.in iframe when the event is started",
        required=False,
    )

alsoProvides(IHello, IFormFieldProvider)
