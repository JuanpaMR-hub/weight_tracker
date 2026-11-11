from django.test import SimpleTestCase
from api.serializers import RegistroSerializer

class RegistroSerializerTest(SimpleTestCase):
    def test_serializer_rejects_invalid_weight(self):
        """ 
        Bastante self explanatory, pero revisa si el peso rechaza un numero negativo
        """
        data = {"peso":-1.0}
        serializer = RegistroSerializer(data = data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("peso",serializer.errors)
