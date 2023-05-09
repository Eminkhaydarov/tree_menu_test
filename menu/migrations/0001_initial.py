# Generated by Django 4.2.1 on 2023-05-09 04:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_name', models.CharField(max_length=255)),
                ('URL', models.URLField(blank=True, max_length=255, null=True)),
                ('named_url', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('URL', models.CharField(max_length=255)),
                ('named_url', models.CharField(blank=True, max_length=255, null=True)),
                ('menu_main', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menu', to='menu.menu')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='menu.menuitem')),
            ],
        ),
    ]