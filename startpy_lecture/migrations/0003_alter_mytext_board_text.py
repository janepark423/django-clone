# Generated by Django 4.1.5 on 2023-02-01 18:12

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('startpy_lecture', '0002_mytext_board_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mytext',
            name='board_text',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
    ]
