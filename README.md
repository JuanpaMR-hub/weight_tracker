
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
### Sesión 2
---
Para la sesión 2 estaba pensando en que puedo hacer. Encontré una buena idea implementar usuarios a esto

¿por que usuarios? para practicar el uso de JWT

¿Lo usará alguien mas? no. jajaja

Investigando puedo subir este proyecto a railway y para evitar el uso indebido de esto mejor dejarlo con una autenticación para acceder a los datos

Entonces. Trabajo para esta sesión:
- Modelo de Usuario implementado
- Enlazar el Registro con el Usuario
- Crear endpoints que permita revisar el registro del peso por el usuario


Aprendí:

Aprendí como hacer el Nested Serializer:
Se tiene que crear una nueva variable que contenga el serializer del item que necesito. En mi caso el usuario necesitaba una variable llamada "registros". Pero no funcionaba solamente con eso y es que en el models tengo que poner el mismo nombre como "related_name". Es decir, en el modelo de Registro le agrego que con su relación su related_name será el mismo que ocupé en la serialización