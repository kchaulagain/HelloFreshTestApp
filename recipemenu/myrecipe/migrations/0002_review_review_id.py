# Generated by Django 3.2.6 on 2021-08-10 11:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myrecipe', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='review_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myrecipe.recipe'),
        ),
    ]
