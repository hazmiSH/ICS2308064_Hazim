# Generated by Django 5.1 on 2024-08-29 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0003_alter_borrowing_book_id_alter_borrowing_student_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='student_stat',
            field=models.CharField(default='Active', max_length=10),
        ),
    ]
