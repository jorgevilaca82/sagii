# Generated by Django 2.1.7 on 2019-03-21 02:49

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0001_initial'),
        ('administracao', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('pessoafisica_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base.PessoaFisica')),
                ('tipo', models.IntegerField(choices=[(1, 'CLT Permanente'), (2, 'CLT Temporário'), (3, 'Prestador de Serviço'), (4, 'Servidor Público'), (5, 'Estagiário'), (6, 'Trainee'), (7, 'Menor Aprendiz')])),
                ('matricula', models.CharField(max_length=25)),
                ('empregador', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='base.PessoaJuridica')),
                ('setor_lotacao', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='administracao.Setor')),
            ],
            bases=('base.pessoafisica',),
            managers=[
                ('servidores', django.db.models.manager.Manager()),
            ],
        ),
    ]