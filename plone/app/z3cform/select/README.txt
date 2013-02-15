
Basic imports

  >>> import zope.interface
  >>> import zope.schema
  >>> import z3c.form
  >>> import plone.app.z3cform

Set up a test request and context

  >>> from zope.publisher.browser import TestRequest
  >>> from z3c.form.interfaces import IFormLayer
  >>> context = object()
  >>> request = TestRequest(skin=plone.app.z3cform.interfaces.IPloneFormLayer)

Selection Field

First, let's try it with > 5 values

    >>> class IPerson(zope.interface.Interface):
    ...     id = zope.schema.Choice(
    ...         title=u'Cities',
    ...         description=u"Where we go.",
    ...         values=(u"Washington, DC", u"Budapest", u"Bristol", u"San Francisco", u"Arnhem", u"Brasilia"),
    ...         required=True)
    ...

    >>> class ConferenceForm(object):
    ...     prefix = 'form.'
    ...     fields = z3c.form.field.Fields(IPerson)
    >>> conferenceForm = ConferenceForm()

    >>> manager = z3c.form.field.FieldWidgets(conferenceForm, request, context)
    >>> manager.ignoreContext = True
    >>> manager.update()

    >>> manager['id']
    <SelectWidget 'form.widgets.id'>

    >>> manager.mode = z3c.form.interfaces.INPUT_MODE
    >>> print manager['id'].render()
    <BLANKLINE>
    ...<select id="form-widgets-id" name="form.widgets.id:list"
            class="select-widget required choice-field" size="1">
    <option id="form-widgets-id-0" value="Washington, DC">Washington, DC</option>
    <option id="form-widgets-id-1" value="Budapest">Budapest</option>
    <option id="form-widgets-id-2" value="Bristol">Bristol</option>
    <option id="form-widgets-id-3" value="San Francisco">San Francisco</option>
    <option id="form-widgets-id-4" value="Arnhem">Arnhem</option>
    <option id="form-widgets-id-5" value="Brasilia">Brasilia</option>
    </select>...
    <input name="form.widgets.id-empty-marker" type="hidden"
           value="1" />...

Then, < 5 values

    >>> class IPerson(zope.interface.Interface):
    ...     id = zope.schema.Choice(
    ...         title=u'Cities',
    ...         description=u"Where we go.",
    ...         values=(u"San Francisco", u"Arnhem", u"Brasilia"),
    ...         required=True)
    ...

    >>> class ConferenceForm(object):
    ...     prefix = 'form.'
    ...     fields = z3c.form.field.Fields(IPerson)
    >>> conferenceForm = ConferenceForm()

    >>> manager = z3c.form.field.FieldWidgets(conferenceForm, request, context)
    >>> manager.ignoreContext = True
    >>> manager.update()

    >>> manager['id']
    <SelectWidget 'form.widgets.id'>

    >>> manager.mode = z3c.form.interfaces.INPUT_MODE
    >>> print manager['id'].render()
    <BLANKLINE>
    ...<span class="option">
          <label for="form-widgets-id-0">
            <input id="form-widgets-id-0"
                   name="form.widgets.id"
                   class="select-widget required choice-field"
                   readonly="" accesskey=""
                   value="San Francisco" type="radio" />
            <span class="label">San Francisco</span>
          </label>
        </span>
        <span class="option">
          <label for="form-widgets-id-1">
            <input id="form-widgets-id-1"
                   name="form.widgets.id"
                   class="select-widget required choice-field"
                   readonly="" accesskey="" value="Arnhem"
                   type="radio" />
            <span class="label">Arnhem</span>
          </label>
        </span>
        <span class="option">
          <label for="form-widgets-id-2">
            <input id="form-widgets-id-2"
                   name="form.widgets.id"
                   class="select-widget required choice-field"
                   readonly="" accesskey="" value="Brasilia"
                   type="radio" />
            <span class="label">Brasilia</span>
          </label>
        </span>...
