# Generated by Django 4.2.6 on 2023-11-23 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_alter_user_verify_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='verify_code',
            field=models.CharField(default='67842', max_length=5, verbose_name='Код верификации'),
        ),
    ]