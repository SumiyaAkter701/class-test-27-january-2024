# Generated by Django 5.0.1 on 2024-01-27 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_alter_customuser_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='BC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.PositiveIntegerField(blank=True, null=True)),
                ('address', models.CharField(max_length=300)),
                ('family_member_count', models.PositiveIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='address',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='age',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='family_member_count',
        ),
    ]
