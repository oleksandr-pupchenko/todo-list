# Generated by Django 3.2.4 on 2023-12-02 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('deadline_date', models.DateTimeField(blank=True, null=True)),
                ('is_done', models.BooleanField(default=True)),
                ('tags', models.ManyToManyField(related_name='tasks', to='todolist.Tag')),
            ],
            options={
                'ordering': ['is_done', '-created_date'],
            },
        ),
    ]
