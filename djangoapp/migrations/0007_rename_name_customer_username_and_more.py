# Generated by Django 4.1 on 2024-10-07 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0006_alter_customer_name_alter_customer_phone_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='name',
            new_name='username',
        ),
        migrations.AddField(
            model_name='customer',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics/'),
        ),
    ]
