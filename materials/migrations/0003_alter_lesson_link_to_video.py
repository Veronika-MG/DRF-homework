# Generated by Django 5.0.6 on 2024-06-24 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("materials", "0002_alter_course_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lesson",
            name="link_to_video",
            field=models.CharField(
                blank=True,
                help_text="Укажите ссылку на видео",
                max_length=150,
                null=True,
                verbose_name="Ссылка на видео",
            ),
        ),
    ]
