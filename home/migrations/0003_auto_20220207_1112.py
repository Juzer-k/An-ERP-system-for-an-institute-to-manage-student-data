# Generated by Django 3.0 on 2022-02-07 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_student_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='batch',
            name='Students',
        ),
        migrations.AddField(
            model_name='batch',
            name='Students',
            field=models.ManyToManyField(to='home.Student'),
        ),
    ]