from five import grok
from plone.directives import dexterity, form
from wccminisite.app.content.homepage import Ihomepage

grok.templatedir('templates')

class Index(dexterity.DisplayForm):
    grok.context(Ihomepage)
    grok.require('zope2.View')
    grok.template('homepage_view')
    grok.name('view')

