# Generated by Django 4.0.6 on 2022-07-27 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quizapp', '0002_category_quesform_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='quesform',
            name='marks',
            field=models.IntegerField(default=2),
        ),
    ]
