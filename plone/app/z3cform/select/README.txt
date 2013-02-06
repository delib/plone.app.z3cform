Boilerplate setup for minimal widget testing framework
TODO: should be a layer

  >>> import zope.schema
  >>> from z3c.form import browser
  >>> from zope.configuration import xmlconfig
  >>> import zope.component
  >>> import zope.security
  >>> import zope.i18n
  >>> import z3c.form
  >>> xmlconfig.XMLConfig('meta.zcml', zope.component)()
  >>> xmlconfig.XMLConfig('meta.zcml', zope.security)()
  >>> xmlconfig.XMLConfig('meta.zcml', zope.i18n)()
  >>> xmlconfig.XMLConfig('meta.zcml', z3c.form)()
  >>> xmlconfig.XMLConfig('configure.zcml', z3c.form)()
  >>> import zope.component
  >>> import zope.i18n.negotiator
  >>> zope.component.provideUtility(zope.i18n.negotiator.negotiator)
  >>> from z3c.form import interfaces
  >>> from z3c.form.testing import TestRequest
  >>> def setupWidget(field):
  ...     request = TestRequest()
  ...     widget = zope.component.getMultiAdapter((field, request),
  ...         interfaces.IFieldWidget)
  ...     widget.id = 'foo'
  ...     widget.name = 'bar'
  ...     return widget

Selection Field

  >>> field = zope.schema.Choice(
  ...   values=(u"Bristol", u"San Francisco", u"Arnhem")
  ...   )
  >>> widget = setupWidget(field)
  >>> widget.update()

  >>> widget.__class__
  <class 'plone.app.z3cform.select.SelectWidget'>

  >>> print widget.render()
  Here's the work!
