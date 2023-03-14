# Generated by Django 4.1.7 on 2023-02-22 04:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0059_course_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='video',
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('videos', models.ManyToManyField(to='profile.video')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='content',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='profile.content'),
        ),
    ]