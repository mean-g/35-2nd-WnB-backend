# Generated by Django 4.0.5 on 2022-08-03 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_kakao_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='kakao_id',
            field=models.BigIntegerField(unique=True),
        ),
    ]
