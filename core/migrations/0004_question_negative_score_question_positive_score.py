# Generated by Django 4.1.7 on 2023-03-11 12:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0003_remove_testresult_result_testresult_score_answer"),
    ]

    operations = [
        migrations.AddField(
            model_name="question",
            name="negative_score",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="question",
            name="positive_score",
            field=models.IntegerField(default=0),
        ),
    ]
