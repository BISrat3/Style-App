# Generated by Django 4.0.5 on 2022-06-09 01:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_style_app', '0010_alter_review_cat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='cat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='main_style_app.category'),
        ),
    ]
