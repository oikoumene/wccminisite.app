from five import grok
from plone.directives import dexterity, form
from wccminisite.app.content.homepage import Ihomepage
from Products.CMFCore.utils import getToolByName

grok.templatedir('templates')

class Index(dexterity.DisplayForm):
    grok.context(Ihomepage)
    grok.require('zope2.View')
    grok.template('homepage_view')
    grok.name('view')
    
    @property
    def portal_catalog(self):
        return getToolByName(self.context, "portal_catalog")
    
    def contents(self):
        context = self.context
        
        if context.pages_sources:
            source_path = '/'.join(context.pages_sources.to_object.getPhysicalPath())
            brains = self.portal_catalog.unrestrictedSearchResults(path={'query':source_path, 'depth':1},
                                                                   portal_type='Document',
                                                                   sort_on='created',
                                                                   sort_order='reverse',
                                                                   review_state='internally_published')[:5]
            
            return brains
        return None
        

