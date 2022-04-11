# Generated by Django 4.0.3 on 2022-04-10 23:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfilePic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profilePic', models.FileField(max_length=250, null=True, upload_to='profilePic/')),
                ('Time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='content',
            new_name='Message',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='timeStamp',
        ),
        migrations.AddField(
            model_name='contact',
            name='Time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
