# Generated by Django 4.1.7 on 2023-03-03 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0070_usercourse_checkout'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='course_status',
        ),
        migrations.RemoveField(
            model_name='course',
            name='course_type',
        ),
        migrations.AddField(
            model_name='instructor',
            name='gender',
            field=models.CharField(choices=[('man', 'man'), ('women', 'women')], default='man', max_length=20),
        ),
    ]
