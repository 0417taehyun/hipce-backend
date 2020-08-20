# Generated by Django 3.1 on 2020-08-20 12:06

from django.db import migrations, models
import user.validation


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.CharField(max_length=50, unique=True, validators=[user.validation.validate_account])),
                ('password', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50, validators=[user.validation.validate_name])),
                ('phone', models.CharField(max_length=50, validators=[user.validation.validate_phone])),
                ('email', models.CharField(max_length=50, unique=True, validators=[user.validation.validate_email])),
                ('birthday', models.CharField(max_length=50, validators=[user.validation.validate_birthday])),
                ('is_sms_marketing_agree', models.BooleanField(blank=True, default=False)),
                ('is_email_maketing_agree', models.BooleanField(blank=True, default=False)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
