# Generated by Django 3.2.12 on 2022-06-17 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0003_services'),
    ]

    operations = [
        migrations.CreateModel(
            name='VolunteerRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('volunteer', models.CharField(max_length=120)),
                ('rating', models.IntegerField()),
            ],
        ),
    ]