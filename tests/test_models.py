from django.test import TestCase
from main.models import *
from datetime import date


class QoshiqchiModelTest(TestCase):

    def setUp(self):
        self.qoshiqchi = Qoshiqchi.objects.create(
            ism="Jahongir Otajonov",
            t_sana=date(1980, 7, 28),
            davlat="O'zbekiston"
        )

    def test_qoshiqchi_str(self):
        self.assertEqual(str(self.qoshiqchi), "Jahongir Otajonov")

    def test_qoshiqchi_fields(self):
        self.assertEqual(self.qoshiqchi.ism, "Jahongir Otajonov")
        self.assertEqual(self.qoshiqchi.t_sana, date(1980, 7, 28))
        self.assertEqual(self.qoshiqchi.davlat, "O'zbekiston")
