# Generated by Django 4.2 on 2023-04-25 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0003_paper_subject_alter_paper_exam_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='question_ans_img_only',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='paper',
            name='question_ans_img',
            field=models.ImageField(blank=True, null=True, upload_to='./static/image/paperimage/'),
        ),
    ]