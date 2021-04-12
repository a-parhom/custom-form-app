# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtraInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('region', models.CharField(max_length=21, verbose_name=b'Region', choices=[(b'ark', b'Автономна Республіка Крим'), (b'vinnytsia_oblast', b'Вінницька область'), (b'volyn_oblast', b'Волинська область'), (b'dnipro_oblast', b'Дніпропетровська область'), (b'donetsk_oblast', b'Донецька область'), (b'zhytomyr_oblast', b'Житомирська область'), (b'zakarpatska_oblast', b'Закарпатська область'), (b'zaporizhzhia_oblast', b'Запорізька область'), (b'ivanofrankivsk_oblast', b'Івано-Франківська область'), (b'kyiv_oblast', b'Київська область'), (b'kirovograd_oblast', b'Кіровоградська область'), (b'luhansk_oblast', b'Луганська область'), (b'lviv_oblast', b'Львівська область'), (b'mykolaiv_oblast', b'Миколаївська область'), (b'odessa_oblast', b'Одеська область'), (b'poltava_oblast', b'Полтавська область'), (b'rivne_oblast', b'Рівненська область'), (b'sumy_oblast', b'Сумська область'), (b'ternopil_oblast', b'Тернопільська область'), (b'kharkiv_oblast', b'Харківська область'), (b'kherson_oblast', b'Херсонська область'), (b'khmelnytskyi_oblast', b'Хмельницька область'), (b'cherkasy_oblast', b'Черкаська область'), (b'chernivtsi_oblast', b'Чернівецька область'), (b'chernihiv_oblast', b'Чернігівська область'), (b'kyiv_city', b'м. Київ'), (b'sevastopol_city', b'м. Севастополь'), (b'other_country', b'Інша країна')])),
                ('user', models.OneToOneField(null=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
