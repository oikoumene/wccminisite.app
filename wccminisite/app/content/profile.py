from five import grok
from plone.directives import dexterity, form

from zope import schema
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from plone.autoform.interfaces import IFormFieldProvider
from zope.interface import alsoProvides

from zope.interface import invariant, Invalid

from z3c.form import group, field

from plone.namedfile.interfaces import IImageScaleTraversable
from plone.namedfile.field import NamedImage, NamedFile
from plone.namedfile.field import NamedBlobImage, NamedBlobFile

from plone.app.textfield import RichText

from z3c.relationfield.schema import RelationList, RelationChoice
from plone.formwidget.contenttree import ObjPathSourceBinder
from plone.multilingualbehavior.directives import languageindependent
from collective import dexteritytextindexer

from wccminisite.app import MessageFactory as _

from plone.z3cform.fieldsets.utils import move
from plone.directives import dexterity, form
from z3c.form.interfaces import IAddForm, IEditForm, HIDDEN_MODE, INPUT_MODE, DISPLAY_MODE


# Interface class; used to define content-type schema.

class Iprofile(form.Schema, IImageScaleTraversable):
    """
    profile
    """

    username = schema.TextLine(
           title=_(u"Portal Username"),
           required=True,
        )
    pass

alsoProvides(Iprofile, IFormFieldProvider)

class profileAddForm(dexterity.AddForm):
    grok.name('wccminisite.app.profile')
    form.wrap(False)
    
    def updateWidgets(self):
        super(profileAddForm, self).updateWidgets()
        pass
        
    
    def updateFields(self):
        super(profileAddForm, self).updateFields()
        self.fields['IDublinCore.title'].field.title = _(u'Full name')
        self.fields['IDublinCore.description'].mode = HIDDEN_MODE
        
class profileEditForm(dexterity.EditForm):
    grok.context(Iprofile)
    
    def updateFields(self):
        super(profileEditForm, self).updateFields()
        self.fields['IDublinCore.title'].field.title = _(u'Full name')
        self.fields['IDublinCore.description'].mode = HIDDEN_MODE
        
