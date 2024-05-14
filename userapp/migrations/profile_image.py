from django.db import migrations, models
import usersapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('usersapp', '0003_alter_profile_options_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='usersapp/static/usersapp/avatar_default.jpg', upload_to=usersapp.models.user_directory_path, verbose_name='Аватар'),
        ),
    ]