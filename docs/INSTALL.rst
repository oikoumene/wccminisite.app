wccminisite.app Installation
----------------------------

To install wccminisite.app using zc.buildout and the plone.recipe.zope2instance
recipe to manage your project, you can do this:

* Add ``wccminisite.app`` to the list of eggs to install, e.g.:

    [buildout]
    ...
    eggs =
        ...
        wccminisite.app

* Re-run buildout, e.g. with:

    $ ./bin/buildout

