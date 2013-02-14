import zope.component
import zope.interface
import zope.schema.interfaces
import zope.component.hooks

import z3c.form.interfaces
import z3c.form.browser.select

try:
    import plone.autoform.widgets
    have_autoform = True
except:
    have_autoform = False

from interfaces import ISelectWidget


class SelectWidget(z3c.form.browser.select.SelectWidget):

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


if have_autoform:
    SelectWidgetExportImportHandler = plone.autoform.widgets.WidgetExportImportHandler(ISelectWidget)

