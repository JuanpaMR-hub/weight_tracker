from django.db import models

# Si vamos a trackear el peso, deberia guardar cada entrada...
# No se como llamar a este modelo... es basicamente la entrada diaria del peso
# 
class Registro(models.Model):
    peso = models.FloatField(null = False, blank = False , default=0.0)
    fecha = models.DateField(default=None)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Mi peso el {self.fecha} fue de {self.peso}"
