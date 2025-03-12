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
