
Boilerplate setup for minimal widget testing framework
TODO: should be a layer

XXX  >>> import zope.schema
XXX  >>> from z3c.form import browser
XXX  >>> from zope.configuration import xmlconfig
XXX  >>> import zope.component
XXX  >>> import zope.security
XXX  >>> import zope.i18n
XXX  >>> import z3c.form
XXX  >>> import plone.app.z3cform
XXX
XXX### xmlconfig.XMLConfig('meta.zcml', zope.component)()
XXX### xmlconfig.XMLConfig('meta.zcml', zope.security)()
XXX### xmlconfig.XMLConfig('meta.zcml', zope.i18n)()
XXX### xmlconfig.XMLConfig('meta.zcml', z3c.form)()
XXX### xmlconfig.XMLConfig('configure.zcml', z3c.form)()
XXX
XXX  >>> xmlconfig.XMLConfig('meta.zcml', zope.component)()
XXX  >>> xmlconfig.XMLConfig('configure.zcml', zope.traversing)()
XXX  >>> xmlconfig.XMLConfig('configure.zcml', zope.publisher)()
XXX  >>> xmlconfig.XMLConfig('configure.zcml', zope.i18n)()
XXX  >>> xmlconfig.XMLConfig('meta.zcml', zope.i18n)()
XXX  >>> xmlconfig.XMLConfig('meta.zcml', z3c.form)()
XXX  >>> xmlconfig.XMLConfig('configure.zcml', plone.app.z3cform)()
XXX
XXX
XXX  >>> import zope.component
XXX  >>> import zope.i18n.negotiator
XXX  >>> zope.component.provideUtility(zope.i18n.negotiator.negotiator)
XXX  >>> from z3c.form import interfaces
XXX  >>> from z3c.form.testing import TestRequest

  >>> import zope.interface
  >>> import zope.schema
  >>> import z3c.form


Selection Field

    >>> class IPerson(zope.interface.Interface):
    ...     id = zope.schema.Choice(
    ...         title=u'Cities',
    ...         description=u"Where we go.",
    ...         values=(u"San Francisco", u"Arnhem"),
    ...         required=True)
    ...

    >>> from z3c.form import field

    >>> class ConferenceForm(object):
    ...     prefix = 'form.'
    ...     fields = field.Fields(IPerson)
    >>> conferenceForm = ConferenceForm()

    >>> from z3c.form.testing import TestRequest
    >>> request = TestRequest()
    >>> context = object()

    >>> manager = field.FieldWidgets(conferenceForm, request, context)
    >>> manager.ignoreContext = True
    >>> manager.update()

    >>> manager['id']
    <SelectWidget 'form.widgets.id'>

    >>> manager.mode = z3c.form.interfaces.INPUT_MODE
    >>> print manager['id'].render()
    <BLANKLINE>
    ...<select id="form-widgets-id" name="form.widgets.id:list" class="select-widget required choice-field" size="1">
    <option id="form-widgets-id-0" value="San Francisco">San Francisco</option>
    <option id="form-widgets-id-1" value="Arnhem">Arnhem</option>
    </select>
    <input name="form.widgets.id-empty-marker" type="hidden" value="1" />...

