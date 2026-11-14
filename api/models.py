from django.db import models
from django.contrib.auth.models import AbstractUser


# Siguiendo el tutorial que estoy viendo, está usando el AbstractUser
# Crea una clase en base a esto, pero no la modifica, simplemente le hace "pass"
# No creo que esto sea necesario de implementar, pero lo dejaré aqui ya que me hace sentido que posteriormente se quiera customizar o ampliar los campos del usuario


class User(AbstractUser):
    pass





# Este pudo quedar como RegistroPeso. Pero ya que la app solo hará esto, no queda mal
class Registro(models.Model):
    peso = models.FloatField(null = False, blank = False , default=0.0)
    fecha = models.DateField(default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE,related_name='registros') # Si se elimina un usuario, se elimina el registro asociado


    def __str__(self):
        return f"Mi peso el {self.fecha} fue de {self.peso}"
