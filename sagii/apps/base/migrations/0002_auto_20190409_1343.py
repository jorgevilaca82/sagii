# Generated by Django 2.2 on 2019-04-09 17:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoajuridica',
            name='matriz',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='base_pessoajuridica_related', related_query_name='base_pessoajuridicas', to='base.PessoaJuridica'),
        ),
    ]