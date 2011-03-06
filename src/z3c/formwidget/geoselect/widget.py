# -*- coding: utf-8 -*-

# zope imports
from z3c.form.widget import FieldWidget
from z3c.form.browser.text import TextWidget
from z3c.form.interfaces import IFieldWidget, IFormLayer
from zope.component import adapter
from zope.interface import implementer, implementsOnly
from zope.schema.interfaces import ITextLine

# local imports
from z3c.formwidget.geoselect.interfaces import IGeoSelectWidget


class GeoSelectWidget(TextWidget):
    """Geo Select Widget based on TextWidget."""
    implementsOnly(IGeoSelectWidget)

    klass = u'geoselect-widget'
    value = u''


@adapter(ITextLine, IFormLayer)
@implementer(IFieldWidget)
def GeoSelectFieldWidget(field, request):
    """Factory for GeoSelectWidget"""
    return FieldWidget(field, GeoSelectWidget(request))
