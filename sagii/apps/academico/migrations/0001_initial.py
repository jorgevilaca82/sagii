# Generated by Django 2.1.7 on 2019-03-21 02:49

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0001_initial'),
        ('recursos_humanos', '0001_initial'),
        ('administracao', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(1, 'Matriculado'), (2, 'Evadido')])),
                ('ra', models.CharField(max_length=255)),
                ('pessoa_fisica', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='base.PessoaFisica')),
            ],
        ),
        migrations.CreateModel(
            name='Campus',
            fields=[
                ('pessoajuridica_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base.PessoaJuridica')),
            ],
            bases=('base.pessoajuridica',),
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='DiretoriaEnsino',
            fields=[
                ('setor_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='administracao.Setor')),
            ],
            bases=('administracao.setor',),
        ),
        migrations.CreateModel(
            name='InscricaoCandidato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(1, 'Deferida'), (2, 'Indeferida'), (3, 'Deferida após recurso')])),
                ('pessoa_fisica', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='base.PessoaFisica')),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('funcionario_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='recursos_humanos.Funcionario')),
                ('titulacao', models.IntegerField(choices=[(1, 'Gradução'), (2, 'Especialização'), (3, 'Mestrador'), (4, 'Doutorado'), (5, 'Pós Doutorado')])),
            ],
            bases=('recursos_humanos.funcionario',),
            managers=[
                ('servidores', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='diretoriaensino',
            name='diretor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='recursos_humanos.Funcionario'),
        ),
        migrations.AddField(
            model_name='curso',
            name='de',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='academico.DiretoriaEnsino'),
        ),
    ]
