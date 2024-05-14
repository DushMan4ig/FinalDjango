from django.db import migrations, models
import usersapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('usersapp', '0005_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='avatar_default_cblgpyo.jpg', upload_to=usersapp.models.user_directory_path, verbose_name='Аватар'),
        ),
    ]