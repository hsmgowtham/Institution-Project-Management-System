# Generated by Django 4.0.8 on 2022-11-27 23:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student', '0002_alter_student_table'),
        ('course', '0002_alter_course_table'),
        ('instituition', '0002_alter_instituition_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('url', models.CharField(max_length=150)),
                ('course', models.ForeignKey(blank=True, db_column='course_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='course.course')),
                ('instituition', models.ForeignKey(blank=True, db_column='instituition_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='instituition.instituition')),
                ('student', models.ForeignKey(blank=True, db_column='student_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='student.student')),
            ],
            options={
                'db_table': 'Project',
            },
        ),
    ]
