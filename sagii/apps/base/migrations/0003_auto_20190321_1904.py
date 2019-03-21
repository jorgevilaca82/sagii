# Generated by Django 2.1.7 on 2019-03-21 23:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20190321_1856'),
    ]

    operations = [
        migrations.AddField(
            model_name='contatosocial',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contatosocial',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='documentopessoal',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='documentopessoal',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='endereco',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='endereco',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='telefone',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='telefone',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
