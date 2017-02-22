from five import grok
from Products.CMFCore.interfaces import IContentish
from Products.CMFCore.utils import getToolByName

grok.templatedir('templates')

class NetworkFacetedView(grok.View):
    grok.context(IContentish)
    grok.name('networkfacetedview')
    grok.require('zope2.View')
    
    @property
    def portal_membership(self):
        return getToolByName(self.context, 'portal_membership')
    
    def getMember(self, username=None):
        data = {'img':''}
        member = self.portal_membership.getMemberById(username)
        if member:
            data['img'] = self.portal_membership.getPersonalPortrait(username).absolute_url()
        return data
        