# Generated by Django 4.1 on 2022-09-02 19:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('InteractiveLearningApp', '0002_remove_language_conv_language_conversation'),
    ]

    operations = [
        migrations.AddField(
            model_name='testquiz',
            name='user1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]