# Generated by Django 3.0.2 on 2020-01-05 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('summary', models.TextField(help_text='Enter the content of article', max_length=1000)),
                ('date_of_publish', models.DateField(blank=True, null=True)),
                ('num_views', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a subject of article', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(help_text='Enter your name', max_length=200)),
                ('text', models.CharField(help_text='Enter the text of comment', max_length=200)),
                ('date_of_publish', models.DateField()),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Article')),
                ('replied_to', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Comment')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='subject',
            field=models.ManyToManyField(help_text='Select a subject for this article', to='blog.Subject'),
        ),
    ]