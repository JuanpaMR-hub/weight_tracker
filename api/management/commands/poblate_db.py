import random
from datetime import date, timedelta

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from ...models import Registro  # models.py de tu app

User = get_user_model()


class Command(BaseCommand):
    help = "Puebla la base de datos con registros de peso de ejemplo"

    def add_arguments(self, parser):
        parser.add_argument("--username", default="demo", help="Usuario dueño de los registros")
        parser.add_argument("--password", default="demo1234", help="Contraseña si el usuario se crea")
        parser.add_argument("--dias", type=int, default=30, help="Cuántos días hacia atrás generar")
        parser.add_argument("--peso", type=float, default=80.0, help="Peso inicial en kg")
        parser.add_argument("--clear", action="store_true", help="Borra antes los registros del usuario")

    def handle(self, *args, **options):
        usuario, creado = User.objects.get_or_create(username=options["username"])
        if creado:
            usuario.set_password(options["password"])
            usuario.save()
            self.stdout.write(f"Usuario '{usuario.username}' creado.")

        if options["clear"]:
            borrados, _ = Registro.objects.filter(usuario=usuario).delete()
            self.stdout.write(f"{borrados} registros anteriores eliminados.")

        hoy = date.today()
        peso = options["peso"]
        registros = []

        for i in range(options["dias"], 0, -1):
            peso = round(peso + random.uniform(-0.4, 0.3), 1)
            registros.append(
                Registro(peso=peso, fecha=hoy - timedelta(days=i), usuario=usuario)
            )

        Registro.objects.bulk_create(registros)

        self.stdout.write(
            self.style.SUCCESS(f"Se insertaron {len(registros)} registros para '{usuario.username}'.")
        )
