from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Backwards compatible settings.AUTH_USER_MODEL
USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class ExtraInfo(models.Model):
    """
    This model contains two extra fields that will be saved when a user registers.
    The form that wraps this model is in the forms.py file.
    """
    user = models.OneToOneField(USER_MODEL, null=True, on_delete=models.CASCADE)
    REGION = (
        ('ark', _('Автономна Республіка Крим')),
        ('vinnytsia_oblast', _('Вінницька область')),
        ('volyn_oblast', _('Волинська область')),
        ('dnipro_oblast', _('Дніпропетровська область')),
        ('donetsk_oblast', _('Донецька область')),
        ('zhytomyr_oblast', _('Житомирська область')),
        ('zakarpatska_oblast', _('Закарпатська область')),
        ('zaporizhzhia_oblast', _('Запорізька область')),
        ('ivanofrankivsk_oblast', _('Івано-Франківська область')),
        ('kyiv_oblast', _('Київська область')),
        ('kirovograd_oblast', _('Кіровоградська область')),
        ('luhansk_oblast', _('Луганська область')),
        ('lviv_oblast', _('Львівська область')),
        ('mykolaiv_oblast', _('Миколаївська область')),
        ('odessa_oblast', _('Одеська область')),
        ('poltava_oblast', _('Полтавська область')),
        ('rivne_oblast', _('Рівненська область')),
        ('sumy_oblast', _('Сумська область')),
        ('ternopil_oblast', _('Тернопільська область')),
        ('kharkiv_oblast', _('Харківська область')),
        ('kherson_oblast', _('Херсонська область')),
        ('khmelnytskyi_oblast', _('Хмельницька область')),
        ('cherkasy_oblast', _('Черкаська область')),
        ('chernivtsi_oblast', _('Чернівецька область')),
        ('chernihiv_oblast', _('Чернігівська область')),
        ('kyiv_city', _('м. Київ')),
        ('sevastopol_city', _('м. Севастополь')),
        ('other_country', _('Інша країна')),
    )

    region = models.CharField(
        verbose_name=_("Регіон"),
        choices=REGION,
        max_length=25,
    )
