# Generated by Django 2.2.6 on 2019-10-24 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll_app', '0002_poll_questions_votos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll_questions',
            name='votos',
            field=models.IntegerField(default=0, editable=False),
        ),
    ]
