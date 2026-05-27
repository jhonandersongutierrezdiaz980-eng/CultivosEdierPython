from django.test import TestCase
from django.urls import reverse
from .models import Cultivo

class CultivoModelViewTests(TestCase):
    def setUp(self):
        self.cultivo = Cultivo.objects.create(
            nombre="Zanahoria",
            agricultor="Juan Perez",
            zona="N",
            cantidad_sembrada=50,
            observaciones="Siembra inicial"
        )

    def test_modelo_str(self):
        self.assertEqual(str(self.cultivo), "Zanahoria - Juan Perez")

    def test_vista_lista_cultivos(self):
        response = self.client.get(reverse('cultivo_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Zanahoria")

    def test_creacion_cultivo_invalido(self):
        cultivo_malo = Cultivo(
            nombre="Tomate",
            agricultor="Ana",
            zona="S",
            cantidad_sembrada=0
        )
        with self.assertRaises(Exception):
            cultivo_malo.full_clean()
