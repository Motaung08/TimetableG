# Generated by Django 2.1.7 on 2019-05-16 03:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Log_In', '0002_auto_20190516_0524'),
        ('Register', '0009_auto_20190516_0113'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registeredstd',
            name='Course_Code',
        ),
        migrations.AlterField(
            model_name='announcements',
            name='Course_Code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Courses.Courses'),
        ),
        migrations.AlterField(
            model_name='class',
            name='Course_Code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Courses.Courses'),
        ),
        migrations.DeleteModel(
            name='Courses',
        ),
        migrations.DeleteModel(
            name='RegisteredStd',
        ),
    ]
