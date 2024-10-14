# Generated by Django 5.1 on 2024-09-18 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0005_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('menid', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('menname', models.TextField(max_length=225)),
                ('menroomno', models.CharField(default='sk2', max_length=3)),
            ],
        ),
    ]