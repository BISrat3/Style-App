# Generated by Django 4.0.5 on 2022-06-09 02:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_style_app', '0011_alter_review_cat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='cat',
        ),
    ]
