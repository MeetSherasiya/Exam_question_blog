# Generated by Django 4.2 on 2023-04-25 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0004_paper_question_ans_img_only_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='question_subnum_or_only',
            field=models.BooleanField(default=False),
        ),
    ]
