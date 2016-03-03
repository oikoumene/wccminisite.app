from collective.grok import gs
from wccminisite.app import MessageFactory as _

@gs.importstep(
    name=u'wccminisite.app', 
    title=_('wccminisite.app import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('wccminisite.app.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
