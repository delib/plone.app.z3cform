import Acquisition
import zope.component
import zope.interface
import zope.schema.interfaces
import zope.component.hooks

import z3c.form.interfaces
import z3c.form.browser.select

# from interfaces import ISelectWidget


class SelectWidget(z3c.form.browser.select.SelectWidget):

    zope.interface.implementsOnly(z3c.form.interfaces.ISelectWidget)

    def update(self):
        super(SelectWidget, self).update()
        z3c.form.browser.widget.addFieldClass(self)


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
    return widget
