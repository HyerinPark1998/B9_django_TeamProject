# Generated by Django 4.2 on 2023-04-11 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0002_alter_profile_profile_image_alter_profile_subscript"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="profile_image",
            field=models.ImageField(
                blank=True, null=True, upload_to="profile_images/", verbose_name="유저이미지"
            ),
        ),
    ]
