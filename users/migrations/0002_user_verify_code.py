# Generated by Django 4.2.6 on 2023-11-13 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='verify_code',
            field=models.CharField(default='75162', max_length=5, verbose_name='Код верификации'),
        ),
    ]