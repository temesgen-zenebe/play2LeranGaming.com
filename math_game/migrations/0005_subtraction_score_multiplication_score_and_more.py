# Generated by Django 4.0.5 on 2022-07-29 10:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('math_game', '0004_addition_score'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subtraction_score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operator', models.CharField(max_length=50)),
                ('max_range', models.SmallIntegerField(default=2)),
                ('score', models.IntegerField(default=0)),
                ('point', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(editable=False, unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='subtractionScore', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-point'],
            },
        ),
        migrations.CreateModel(
            name='Multiplication_score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operator', models.CharField(max_length=50)),
                ('max_range', models.SmallIntegerField(default=2)),
                ('score', models.IntegerField(default=0)),
                ('point', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(editable=False, unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='multiplicationScore', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-point'],
            },
        ),
        migrations.CreateModel(
            name='Division_score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operator', models.CharField(max_length=50)),
                ('max_range', models.SmallIntegerField(default=2)),
                ('score', models.IntegerField(default=0)),
                ('point', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(editable=False, unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='divisionScore', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-point'],
            },
        ),
    ]