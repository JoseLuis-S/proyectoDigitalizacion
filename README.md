# 🎵 Adivinador de Canciones con Emojis 🎵

## Descripción:

Este es un juego interactivo en Python donde el usuario debe adivinar canciones basándose en una combinación de emojis. El programa elige aleatoriamente una canción de un artista dado y genera emojis que representan su título. El jugador debe adivinar el nombre de la canción con la posibilidad de recibir pistas adicionales.

## Características:

✅ Obtiene una canción popular de un artista proporcionado por el usuario.
✅ Genera una representación con emojis del título de la canción.
✅ Permite al usuario adivinar el título con un sistema de pistas.
✅ Sistema de puntaje basado en la cantidad de intentos.
✅ Ideal para jugar con amigos y desafiar conocimientos musicales.

## Cómo jugar:

1. Ingresa el nombre de un artista.
2. El programa seleccionará una canción conocida de ese artista.
3. Se mostrarán 5 emojis representando la canción.
4. Intenta adivinar el nombre de la canción.
5. Si fallas, recibirás pistas sobre género, año de lanzamiento y artista.
6. Si adivinas correctamente, ganas puntos según el número de intentos.
7. Puedes jugar tantas veces como quieras.

## Tecnologías utilizadas:

🔹 Python
🔹 API de Groq para obtener canciones y generar respuestas
🔹 Expresiones regulares para el manejo de emojis
🔹 Entrada y salida de datos en consola

## Ejemplo de uso:

```
Elige un artista: Coldplay

Adivina la canción: 🌍💙✨🎶

Tu respuesta: Fix You
Pista: Género: Rock Alternativo

Tu respuesta: Viva La Vida
Pista: Año de lanzamiento: 2008

Tu respuesta: Clocks
Pista: Artista: Coldplay

Tu respuesta: Yellow

¡Correcto! 🎉 Puntos: 80
```

## Preguntas a responder

### 1. Ciclo de vida del dato (5b):

#### Si no trabajas con datos, ¿cómo podrías incluir una funcionalidad que los gestione de forma eficiente?
  Se podría agregar almacenamiento en una base de datos para registrar puntuaciones y estadísticas.

### 2. Almacenamiento en la nube (5f):

#### Si no usas la nube, ¿cómo podrías integrarla en futuras versiones?
  Se podría integrar Firebase o AWS S3 para almacenar datos de jugadores y sesiones de juego.

### 3. Seguridad y regulación (5i):

#### Si no implementaste medidas de seguridad, ¿qué riesgos potenciales identificas y cómo los abordarías en el futuro?
  No almacena información personal, pero si se implementara almacenamiento, habría que considerar las normativas de protección de datos.

### 4. Implicación de las THD en negocio y planta (2e):

#### Si tu proyecto no aplica directamente a negocio o planta, ¿qué otros entornos podrían beneficiarse?
  Puede ser usado en plataformas de entretenimiento o educación musical.
  
### 5. Mejoras en IT y OT (2f):

#### ¿Qué procesos específicos podrían beneficiarse de tu solución en términos de automatización o eficiencia?
  Puede ser usado en plataformas de streaming de musica como Spotify o Apple Music, siendo un entretenimiento extra.
  
### 6. Tecnologías Habilitadoras Digitales (2g):

#### ¿Qué tecnologías habilitadoras digitales (THD) has utilizado o podrías integrar en tu proyecto?
   API de Groq y procesamiento de lenguaje natural.
  
#### ¿Cómo mejoran estas tecnologías la funcionalidad o el alcance de tu software?
  Permiten que se pueda acceder a una gran cantidad de canciones sin la necesidad de implementar una base de datos, haciendo que el software sea mas liviano.
