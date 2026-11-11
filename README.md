

![Project logo](/weight-tracker-logo.svg)

# Proyecto de seguimiento de peso


## Descripción del proyecto
Es simplemente una página que trackea el peso, se hace un formulario que ingresa un peso en numero decimal y este queda registrado en la BD
Se puede ampliar esto haciendo un gráfico de seguimiento y quizás mas adelante generar una especie de "recap" o algo por el estilo
Es un proyecto básico que estoy haciendo para CREAR PROYECTOS TERMINADOS

En django se realizará la API para que mas adelante se pueda hacer cualquier frontend 


## Material util usado para el desarrollo
Estuve usando la playlist de DRF que está bastante buena
- [DRF - API Development with Django](https://www.youtube.com/watch?v=BMym71Dwox0&t=1212s)

Obviamente la documentación de DRF, especificamente la parte de serializers
- [Django Documentation](https://www.django-rest-framework.org/api-guide/serializers/#field-level-validation])

---
### Sesión 1
---
Para esta sesión me metí desde el computador de escritorio, me costó un poco acostumbrarme a los comandos de windows pero se pudo jajaja
Estuve haciendo un poco con mis propios conocimientos pero despues me veia en la necesidad de retomar los videos que vi de la playlist
lo genial es que en el mismo video nos enseña en que parte de la documentación de Django se puede encontrar mas información

#### Hice:

- La base del proyecto de django
- Uso de gitignore
- .env con otro llamado example
- Creación del modelo Registro
- Creación del serializador
- Una View simple
- Test del peso que sea positivo

#### Aprendí:

La verdad es mas sencillo de lo que pensaba, me demoré mas en elegir un buen nombre al modelo jajaja

Lo unico nuevo que aprendí fue el uso del validate en los serializers. Lo demas si lo sabía pero me falta emplearlo

 
#### Debo/Quiero hacer:

Quiero usar una view generica mejor, pero ahora estoy siguiendo el video para ver a donde va todo esto. Hablando de eso no seguí todo el video

Quedé en el segundo de la playlist casi a mitad de su duración

Ademas de la view... creo que estaría listo con eso para hacer el MVP

Con esa view generica me permite hacer el CRUD completo y ahí cualquier request que llegue va a ser manejada por una sola view

Podría usar la IA para que me genere un HTML sencillo que consuma mi API. Dandome un formulario simple para ingresar el peso y su fecha ademas de un gráfico que me muestre el seguimiento