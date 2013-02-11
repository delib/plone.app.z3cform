import zope.schema.interfaces
import z3c.form.interfaces


class IChoiceField(zope.schema.interfaces.IChoice,
                   zope.schema.interfaces.IFromUnicode):
    """ Special marker for choice fields that use our widget """


class ISetField(zope.schema.interfaces.ISet,
                zope.schema.interfaces.IFromUnicode):
    """ Special marker for set fields that use our widget """


# class ISelectWidget(z3c.form.interfaces.IWidget):
#     """Select widget with ability to used select or
#        radiobutton/checkbox widgets."""
