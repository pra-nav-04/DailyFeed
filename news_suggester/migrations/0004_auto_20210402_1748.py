# Generated by Django 3.1.7 on 2021-04-02 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_suggester', '0003_watchhistory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsarticle',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='watchhistory',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]