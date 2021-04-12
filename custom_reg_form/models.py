from django.conf import settings
from django.db import models

# Backwards compatible settings.AUTH_USER_MODEL
USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class ExtraInfo(models.Model):
    """
    This model contains two extra fields that will be saved when a user registers.
    The form that wraps this model is in the forms.py file.
    """
    user = models.OneToOneField(USER_MODEL, null=True)
    REGION = (
        ('ark', 'Автономна Республіка Крим'),
        ('vinnytsia_oblast', 'Вінницька область'),
        ('volyn_oblast', 'Волинська область'),
        ('dnipro_oblast', 'Дніпропетровська область'),
        ('donetsk_oblast', 'Донецька область'),
        ('zhytomyr_oblast', 'Житомирська область'),
        ('zakarpatska_oblast', 'Закарпатська область'),
        ('zaporizhzhia_oblast', 'Запорізька область'),
        ('ivanofrankivsk_oblast', 'Івано-Франківська область'),
        ('kyiv_oblast', 'Київська область'),
        ('kirovograd_oblast', 'Кіровоградська область'),
        ('luhansk_oblast', 'Луганська область'),
        ('lviv_oblast', 'Львівська область'),
        ('mykolaiv_oblast', 'Миколаївська область'),
        ('odessa_oblast', 'Одеська область'),
        ('poltava_oblast', 'Полтавська область'),
        ('rivne_oblast', 'Рівненська область'),
        ('sumy_oblast', 'Сумська область'),
        ('ternopil_oblast', 'Тернопільська область'),
        ('kharkiv_oblast', 'Харківська область'),
        ('kherson_oblast', 'Херсонська область'),
        ('khmelnytskyi_oblast', 'Хмельницька область'),
        ('cherkasy_oblast', 'Черкаська область'),
        ('chernivtsi_oblast', 'Чернівецька область'),
        ('chernihiv_oblast', 'Чернігівська область'),
        ('kyiv_city', 'м. Київ'),
        ('sevastopol_city', 'м. Севастополь'),
        ('other_country', 'Інша країна'),
    )

    region = models.CharField(
        verbose_name="Region",
        choices=REGION,
        max_length=21,
    )
