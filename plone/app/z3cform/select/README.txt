Smart Selection Widget
======================

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
---------------

First, let's try a form field with > 5 values

    >>> class IConference(zope.interface.Interface):
    ...     id = zope.schema.Choice(
    ...         title=u'Cities',
    ...         description=u"Where we go.",
    ...         values=(u"Washington, DC", u"Budapest", u"Bristol", u"San Francisco", u"Arnhem", u"Brasilia"),
    ...         required=True)

    >>> class ConferenceForm(object):
    ...     prefix = 'form.'
    ...     fields = z3c.form.field.Fields(IConference)

    >>> conferenceForm = ConferenceForm()
    >>> manager = z3c.form.field.FieldWidgets(conferenceForm, request, context)
    >>> manager.ignoreContext = True
    >>> manager.update()

See if it provides our version of ISelectWidget

    >>> plone.app.z3cform.select.interfaces.ISelectWidget.providedBy(manager['id'])
    True

Check that the widget knows how to render itself as a selection

    >>> manager['id'].widget_format()
    'select'

    >>> manager.mode = z3c.form.interfaces.INPUT_MODE
    >>> print manager['id'].render()
    <BLANKLINE>
    ...<select id="form-widgets-id" name="form.widgets.id:list"
            class="select-widget required choice-field" size="1">...

Then, < 5 values

    >>> class IConference(zope.interface.Interface):
    ...     id = zope.schema.Choice(
    ...         title=u'Cities',
    ...         description=u"Where we go.",
    ...         values=(u"San Francisco", u"Arnhem", u"Brasilia"),
    ...         required=True)

    >>> class ConferenceForm(object):
    ...     prefix = 'form.'
    ...     fields = z3c.form.field.Fields(IConference)

    >>> conferenceForm = ConferenceForm()
    >>> manager = z3c.form.field.FieldWidgets(conferenceForm, request, context)
    >>> manager.ignoreContext = True
    >>> manager.update()

We should be formatted as individual controls

    >>> manager['id'].widget_format()
    'individual'

And, those controls should be radio buttons

    >>> manager.mode = z3c.form.interfaces.INPUT_MODE
    >>> print manager['id'].render()
    <BLANKLINE>
    ...<input id="form-widgets-id-0"
               name="form.widgets.id"
               class="select-widget required choice-field"
               readonly="" accesskey=""
               value="San Francisco" type="radio" />
        <span class="label">San Francisco</span>...


Multi-Selection Field
---------------------

First, let's try it with > 5 values

    >>> class IConference(zope.interface.Interface):
    ...     id = zope.schema.Set(
    ...         title=u'Cities',
    ...         description=u"Where we go.",
    ...         value_type=zope.schema.Choice(values=(u"Washington, DC", u"Budapest", u"Bristol", u"San Francisco", u"Arnhem", u"Brasilia")),
    ...         required=True)

    >>> class ConferenceForm(object):
    ...     prefix = 'form.'
    ...     fields = z3c.form.field.Fields(IConference)

    >>> conferenceForm = ConferenceForm()
    >>> manager = z3c.form.field.FieldWidgets(conferenceForm, request, context)
    >>> manager.ignoreContext = True
    >>> manager.update()

Check to make sure we're using our interface

    >>> plone.app.z3cform.select.interfaces.ISelectWidget.providedBy(manager['id'])
    True

And that we're formatted for a select

    >>> manager['id'].widget_format()
    'select'

Rendering should be a select with "multiple"

    >>> manager.mode = z3c.form.interfaces.INPUT_MODE
    >>> print manager['id'].render()
    <BLANKLINE>
    ...<select id="form-widgets-id" name="form.widgets.id:list"
            class="select-widget required set-field"
            multiple="multiple" size="5">...

Then, < 5 values

    >>> class IConference(zope.interface.Interface):
    ...     id = zope.schema.Set(
    ...         title=u'Cities',
    ...         description=u"Where we go.",
    ...         value_type=zope.schema.Choice(values=[u"San Francisco", u"Arnhem", u"Brasilia"]),
    ...         required=True)

    >>> class ConferenceForm(object):
    ...     prefix = 'form.'
    ...     fields = z3c.form.field.Fields(IConference)

    >>> conferenceForm = ConferenceForm()
    >>> manager = z3c.form.field.FieldWidgets(conferenceForm, request, context)
    >>> manager.ignoreContext = True
    >>> manager.update()

We should be set for individual controls

    >>> manager['id'].widget_format()
    'individual'

And render as checkboxes

    >>> manager.mode = z3c.form.interfaces.INPUT_MODE
    >>> print manager['id'].render()
    <BLANKLINE>
    ...<input type="checkbox" id="form-widgets-id-0"
             name="form.widgets.id:list"
             class="select-widget required set-field"
             alt="" readonly="" accesskey=""
             value="San Francisco" />
      <label for="form-widgets-id-0">
        <span class="label">San Francisco</span>
      </label>...

Demonstrate that we can coerce to selection

    >>> manager['id'].input_format = 'select'
    >>> manager.update()

    >>> manager['id'].widget_format()
    'select'

    >>> print manager['id'].render()
    <BLANKLINE>
    ...<select id="form-widgets-id" name="form.widgets.id:list"
            class="select-widget required set-field"
            multiple="multiple" size="5">
    <option id="form-widgets-id-0" value="San Francisco">San Francisco</option>...

Or back to individual

    >>> manager['id'].input_format = 'individual'
    >>> manager.update()

    >>> manager['id'].widget_format()
    'individual'

    >>> manager.mode = z3c.form.interfaces.INPUT_MODE
    >>> print manager['id'].render()
    <BLANKLINE>
    ...<input type="checkbox" id="form-widgets-id-0"
             name="form.widgets.id:list"
             class="select-widget required set-field"
             alt="" readonly="" accesskey=""
             value="San Francisco" />
      <label for="form-widgets-id-0">
        <span class="label">San Francisco</span>
      </label>...
