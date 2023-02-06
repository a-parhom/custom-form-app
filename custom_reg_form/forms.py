from .models import ExtraInfo
from django.forms import ModelForm
from django.utils.translation import ugettext as _

class ExtraInfoForm(ModelForm):
    """
    The fields on this form are derived from the ExtraInfo model in models.py.
    """
    def __init__(self, *args, **kwargs):
        super(ExtraInfoForm, self).__init__(*args, **kwargs)
        self.fields['region'].error_messages = {
            "required": _("Будь ласка, вкажіть регіон."),
        }

    class Meta(object):
        model = ExtraInfo
        fields = ('region',)
        serialization_options = {'region':{'default':''}}
