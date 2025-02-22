from django.db import migrations, models
import usersapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('usersapp', '0002_alter_profile_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'Профиль пользователя сайта', 'verbose_name_plural': 'Профили пользователей сайта'},
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='avatar_default.jpg', upload_to=usersapp.models.user_directory_path, verbose_name='Аватар'),
        ),
    ]