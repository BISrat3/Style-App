# Generated by Django 4.0.5 on 2022-06-08 23:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_style_app', '0008_rename_shirt_review_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='cat',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='main_style_app.category'),
        ),
    ]
