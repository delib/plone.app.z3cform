import zope.schema
import zope.schema.interfaces
import z3c.form.interfaces


class IChoiceField(zope.schema.interfaces.IChoice,
                   zope.schema.interfaces.IFromUnicode):
    """ Special marker for choice fields that use our widget """


class ISetField(zope.schema.interfaces.ISet,
                zope.schema.interfaces.IFromUnicode):
    """ Special marker for set fields that use our widget """


class ISelectWidget(z3c.form.interfaces.ISelectWidget):
    """Select widget with ability to use select or
       radiobutton/checkbox widgets."""

    input_format = zope.schema.Choice(
        title=u'Input Format',
        values=(None, u'auto', u'select', u'individual'),
        default=u'auto'
    )

    size = zope.schema.Int(
        title=u'Size',
        description=u'Rows to display in selection boxes',
        default=5,
    )

    def widget_format(self):
        """ return 'individual' or 'select' """
