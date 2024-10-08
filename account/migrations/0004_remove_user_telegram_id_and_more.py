# Generated by Django 5.1 on 2024-09-10 15:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_user_telegram_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='telegram_id',
        ),
        migrations.RemoveField(
            model_name='user',
            name='telegram_username',
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='email'),
        ),
        migrations.CreateModel(
            name='TelegramUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telegram_id', models.CharField(max_length=255, unique=True, verbose_name='telegram id')),
                ('telegram_username', models.CharField(blank=True, max_length=255, null=True, verbose_name='telegram username')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='telegram_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
