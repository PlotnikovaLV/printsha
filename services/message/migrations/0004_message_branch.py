# Generated by Django 3.2.7 on 2021-09-24 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0003_alter_message_theme'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='branch',
            field=models.CharField(choices=[('Столбцы', 'Столбцы'), ('Иное...', 'Иное...')], default='Дзержинск', max_length=20, verbose_name='отделение'),
        ),
    ]
