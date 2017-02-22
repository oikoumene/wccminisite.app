from five import grok
from plone.directives import dexterity, form
from wccminisite.app.content.profile import Iprofile

grok.templatedir('templates')

class Index(dexterity.DisplayForm):
    grok.context(Iprofile)
    grok.require('zope2.View')
    grok.template('profile_view')
    grok.name('view')

