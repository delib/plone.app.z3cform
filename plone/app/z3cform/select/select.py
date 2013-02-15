import zope.component
import zope.interface
import zope.schema.interfaces
import zope.component.hooks
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

import z3c.form.interfaces
import z3c.form.browser.select

try:
    import plone.autoform.widgets
    have_autoform = True
except ImportError:
    have_autoform = False

try:
    import plone.schemaeditor.widgets
    have_schemaeditor = True
except ImportError:
    have_schemaeditor = False

from zope.i18nmessageid import MessageFactory
_ = MessageFactory('plone')

from interfaces import ISelectWidget


class SelectWidget(z3c.form.browser.select.SelectWidget):
    """ Selection widget that implements our extra UI """

    zope.interface.implementsOnly(ISelectWidget)

    def update(self):
        super(SelectWidget, self).update()
        z3c.form.browser.widget.addFieldClass(self)

    def widget_format(self):
        input_format = getattr(self, 'input_format', 'auto')
        if input_format == 'auto':
            if len(self.terms) > 5:
                return 'select'
            else:
                return 'individual'
        return input_format


@zope.component.adapter(zope.schema.interfaces.IChoice,
                        z3c.form.interfaces.IFormLayer)
@zope.interface.implementer(z3c.form.interfaces.IFieldWidget)
def SelectFieldWidget(field, request):
    """IFieldWidget factory for SelectWidget."""
    return z3c.form.widget.FieldWidget(field, SelectWidget(request))


@zope.component.adapter(
    zope.schema.interfaces.IUnorderedCollection,
    z3c.form.interfaces.IFormLayer)
@zope.interface.implementer(z3c.form.interfaces.IFieldWidget)
def CollectionSelectFieldWidget(field, request):
    """IFieldWidget factory for SelectWidget."""
    widget = z3c.form.widget.FieldWidget(field, SelectWidget(request))
    widget.size = 5
    widget.multiple = 'multiple'
    widget.input_format = 'auto'
    return widget


if have_schemaeditor:
    # Tell plone.schemaeditor how to display our input format widget

    select_styles = SimpleVocabulary(
        [SimpleTerm(value=u'auto', title=_(u'Auto')),
         SimpleTerm(value=u'select', title=_(u'Selection box')),
         SimpleTerm(value=u'individual', title=_(u'Individual controls'))]
        )

    class ISelectWidgetParameters(zope.interface.Interface):

        input_format = zope.schema.Choice(
            title=_(u'Input Format'),
            description=_(
                "Determines whether choices are displayed in a single "
                "control or several individual controls. "
                "Choose 'auto' to use single controls for small "
                "numbers of items and a select box for more."
                ),
            vocabulary=select_styles,
            default=u'auto',
        )

        size = zope.schema.Int(
            title=_(u'Size'),
            description=_(u'Rows to display in selection boxes'),
            default=5,
        )

    def get_select_widget_schema(schema_context, field):
        return ISelectWidgetParameters

    class SelectWidgetParameters(plone.schemaeditor.widgets.WidgetSettingsAdapter):
        schema = ISelectWidgetParameters


if have_autoform:
    # Arrange for serialization to/from supermodel
    SelectWidgetExportImportHandler = plone.autoform.widgets.WidgetExportImportHandler(ISelectWidget)
