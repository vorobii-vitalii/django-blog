# Generated by Django 3.0.2 on 2020-01-05 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_subject_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='annotation',
            field=models.CharField(help_text='Enter brief introduction to subject', max_length=500, null=True),
        ),
    ]
