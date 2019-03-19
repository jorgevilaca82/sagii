from django.test import TestCase
from ..models import *


class PessoaTestCase(TestCase):

    def setUp(self):
        self.p1 = Pessoa.objects.create(
            nome_razao_social='Instituto Federal de Rondônia - IFRO')

    def test_pessoa_p1_exists(self):

        p1 = Pessoa.objects.filter(nome_razao_social__icontains='ifro')

        self.assertTrue(
            p1.exists(), 'não existe nenhuma pessoa com o critério procurado.')

        p1 = Pessoa.objects.get(pk=1)
        self.assertIsNotNone(p1)
        self.assertIsInstance(p1, Pessoa)
        self.assertEqual(p1.nome_razao_social,
                         'Instituto Federal de Rondônia - IFRO')

    def test_pessoa_p1_tem_enderecos(self):
        self.assertEquals(self.p1.base_endereco_related.count(), 0)

        end1 = Endereco(
            tipo=Endereco.Tipo.RESIDENCIAL,
            cep='76821-001',
            logradouro='Av. Tiradentes',
            numero='3009',
            bairro='Setor Industrial',
            cidade='Porto Velho',
            uf='RO',
            complemento='lado direito',
            principal=True,
            pessoa=self.p1
        )

        end1.save()

        self.assertEquals(self.p1.base_endereco_related.count(), 1)
        self.assertEquals(end1.tipo, Endereco.Tipo.RESIDENCIAL)
        self.assertEquals(end1.cep, '76821-001')
        self.assertEquals(end1.pessoa.nome_razao_social,
                          'Instituto Federal de Rondônia - IFRO')

        # save automatico do segundo endereço
        end2 = self.p1.base_endereco_related.create(
            tipo=Endereco.Tipo.COMERCIAL,
            cep='76804-124',
            logradouro='Av. 7 de setembro',
            numero='2090',
            bairro='Nossa Senhora das Graças',
            cidade='Porto Velho',
            uf='RO',
            complemento='lado direito'
        )

        self.assertIsNotNone(end2.pk)
        self.assertEquals(end2.pessoa.id, self.p1.id)
        self.assertGreater(self.p1.base_endereco_related.count(), 1,
                           'não existe mais de 1 endereco')

    def test_pessoa_p1_tem_contato_social(self):
        self.assertEquals(self.p1.base_contatosocial_related.count(), 0)

        c1_whatsapp = ContatoSocial(
            tipo=ContatoSocial.Tipo.WHATSAPP, valor='+55 69 9.9999-1234', pessoa=self.p1)
        
        c1_whatsapp.save()

        self.assertEquals(c1_whatsapp.pk, 1)
        self.assertIsNotNone(c1_whatsapp.pessoa)
        self.assertEquals(c1_whatsapp.pessoa.pk, self.p1.pk)
        self.assertEquals(str(c1_whatsapp), 'Whatsapp: +55 69 9.9999-1234')

