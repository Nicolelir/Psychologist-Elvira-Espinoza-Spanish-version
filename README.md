# <p style="text-align: center;">Elvira Espinoza Ahumada</p>

[Click aquí para ver la versión en vivo](https://elvira-espinoza-spanish-v-fe945efbedfa.herokuapp.com/)

![logo](Documentacion/caracteristicas/logo3.png)


This is a Spanish version of one of my projects. As the request of my client, some changes have been incorporated and new elements have been added in this version. You can review the original version in English here [Link to the english version](https://elvira-espinoza-50ffaf8a32fa.herokuapp.com/)

----------------------------------------------------------------------------------------------------------------------------

## Índice - Tabla de contenido

- [Experiencia de usuario (UX)](#experiencia-usuario-ux)
- [Diseño](#diseño)
- [Tecnologías utilizadas](#tecnologías-usadas)
- [Características](#características)
- [Pruebas](#pruebas)
- [Implementación](#implementación)
- [Créditos](#créditos)

# Experiencia de usuario (UX)
El objetivo de este sitio web es crear una plataforma fácil de usar donde los usuarios puedan obtener información sobre Elvira, sus especialidades, enfoques de tratamiento y detalles de contacto. Esto ayuda a los clientes potenciales a comprender la experiencia del terapeuta y decidir si es la persona adecuada para ellos. Al mismo tiempo, el sitio sirve como herramienta de marketing para atraer nuevos clientes gracias a las reseñas que los usuarios pueden publicar, demostrando la experiencia del terapeuta y destacando sus historias de éxito.

## Objetivos del proyecto

## Metodología ágil
Este proyecto se creó utilizando principios ágiles a través de un tablero de proyecto en Github, donde pude seleccionar qué funciones aún estaban por hacer, qué funciones estaban en progreso mientras se trabajaba en ellas y qué funciones cumplían con la definición de terminado. Se agregaron etiquetas para ordenar los problemas según su importancia.
En cuanto a las historias de usuario, las creé en base a una plantilla, que actuó como esqueleto para crear nuevas historias de usuario. Cada historia de usuario seguiría la convención:

**Como (rol) yo puedo (capacidad) para que (beneficio_recibido)**

con sus respectivos "Criterios de aceptación" que deberían cumplirse para que el problema de la Historia de usuario se marque como Listo. Los criterios de aceptación fueron muy útiles para garantizar que se completaran todas las tareas necesarias, ayudándome a organizar y priorizar mi flujo de trabajo. Esto ha sido esencial debido al tiempo muy limitado que teníamos para completar este proyecto.

## Priorización de Moscú
Seguí el método de priorización de MoSCoW para este proyecto, con las siguientes etiquetas:

Debe contener: los componentes críticos 'requeridos' del proyecto. 

Debería tener: los componentes que son valiosos para el proyecto pero que no son absolutamente "vitales" en la etapa MVP. Los "debe contener" deben recibir prioridad sobre los "debería contener".

Podría tener: estas son las características que son una 'bonificación' para el proyecto, sería bueno tenerlas en esta fase, pero solo si las tareas más importantes se han completado primero y el tiempo lo permite.

![img](documentación/características/tablero.PNG)

## Historias de usuarios 

### Épicas

- Registro de usuario e inicio de sesión.
- Página de inicio (formulario de contacto)
- Servicios 
- Reservar citas, editarlas y eliminarlas.
- Publicar una reseña 
- Panel de administración 
- Mantener un diseño consistente teniendo en cuenta la capacidad de respuesta.ç

| Historia de usuario| Prioridad |
|---------------------------------------------------------------------------------------------------------------------------------|-------------|
|  #1 |Como **Usuario** puedo **hacer clic en el enlace Acerca de/servicios** para poder **leer sobre el especialista y los servicios ofrecidos**|**DEBE TENER**|
|  #2 |Como **visitante del sitio web del psicólogo** quiero **navegar fácilmente en la página** para **que pueda tener una idea clara sobre el contenido y el sistema de reservas**|**DEBE TENER**|
|  #3 |Como **Administrador** puedo **actualizar el contenido de la página Acerca de** para que **está disponible en el sitio**|**PODRÍA TENER**|
|  #4 |Como **usuario nuevo** quiero **crear una nueva cuenta** para que **pueda facilitar futuras reservas y dejar una reseña**|**DEBE TENER**|
|  #5 |Como **usuario registrado** quiero **iniciar sesión con mis credenciales** para **poder acceder a mi cuenta.**|**DEBE TENER**|
|  #6 |Como **usuario** quiero **ver la disponibilidad del psicólogo** para **poder elegir y reservar un horario conveniente**|**DEBE TENER**|
|  #7 |Como **usuario** quiero **ver mi lista de reservas** para **poder reprogramar una cita**|**DEBE TENER**|
|  #8 |Como **usuario** quiero **ver mi lista de reservas** para **poder eliminar una cita**|**DEBE TENER**|
|  #9 |Como **usuario** puedo **completar un formulario de contacto** para **poder enviar una solicitud para el especialista**|**DEBE TENER**|
|  #10 |Como **usuario del sitio** puedo **ver una lista paginada de reseñas** para **poder seleccionar qué reseña quiero ver**|**DEBE TENER**|
|  #11 |Como **usuario** puedo **crear reseñas** para que **otros usuarios puedan leer sobre mi experiencia con el especialista**|**DEBE TENER**|
|  #12 |Como usuario puedo **hacer clic en una reseña** para poder leer el texto completo si es un texto muy largo**|**PODRÍA TENER**|
|  #13 |Como **Administrador del sitio que utiliza el sistema de reservas**, quiero **tener un panel de control** para **poder administrar mi disponibilidad, ver las próximas citas y bloquear franjas horarias.**||**PODRÍA TENER**|
|  #14 |Como **administrador del sitio** puedo **aprobar o eliminar reseñas** para **poder filtrar reseñas objetables y administrar el contenido de mi sitio web**||**DEBE TENER**|

# Diseño

## Esquema de colores

Los colores fueron seleccionados con la intención de complementar los colores del logo, en una mezcla de verde y marrón. El logo fue proporcionado por Elvira y el color tiene un significado especial para ella, así que intenté mantener la paleta de colores que ella quería, pero también considerando visibilidad y contrastes para una mejor experiencia de usuario.

## Estructuras (wireframes)
Fueron creados usando Balsamiq. Las secciones siguientes muestran los marcos estructurales individuales para diferentes dispositivos:

- Página de inicio
La página de inicio tiene una imagen principal, una sección de bienvenida y un formulario de contacto, debajo del formulario de contacto hay un botón "¡Lea más sobre mí!" que va directamente a la página de Servicios. 
<detalles>
<summary>Haga clic para ver los wireframes de la página de inicio</summary>

![img]()
</detalles>

- Acerca de/Servicios
Esta página tiene 2 secciones, una sección "Acerca de mí" donde los usuarios pueden leer sobre la misión y visión de Elvira. 
La segunda sección tiene una lista de los servicios prestados al especialista y en la parte inferior de la página hay un botón en el que los usuarios pueden hacer clic si deciden seguir adelante reservando una cita. Para acceder a la página de reservas, los usuarios deben iniciar sesión o registrarse primero. 

<detalles>
<summary>Haga clic para ver los wireframes de la página de servicios</summary>

![img]()
</detalles>

