# Generated by Django 4.2.4 on 2023-08-26 19:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0002_alter_receipts_ingridients_alter_receipts_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('image', models.ImageField(upload_to='image/')),
                ('text_description', models.TextField(verbose_name='Текстовое описание')),
                ('cook_time', models.TimeField(verbose_name='Время приготовления')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Рецепт',
                'verbose_name_plural': 'Рецепты',
            },
        ),
        migrations.AlterModelOptions(
            name='ingridients',
            options={'verbose_name': 'Ингридиент', 'verbose_name_plural': 'Ингридиенты'},
        ),
        migrations.RenameField(
            model_name='ingridients',
            old_name='unit',
            new_name='measurement_unit',
        ),
        migrations.RenameField(
            model_name='ingridients',
            old_name='title',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='ingridients',
            name='quantity',
        ),
        migrations.DeleteModel(
            name='Receipts',
        ),
        migrations.AddField(
            model_name='recipes',
            name='ingridients',
            field=models.ManyToManyField(related_name='ingridients', to='api.ingridients', verbose_name='Ингридиенты'),
        ),
        migrations.AddField(
            model_name='recipes',
            name='tag',
            field=models.ManyToManyField(related_name='tags', to='api.tags', verbose_name='Тег'),
        ),
    ]
