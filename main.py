import groq
import re
import json

# Configurar clave de API de Groq
groq_api_key = "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"

def obtener_cancion(artista):
    client = groq.Client(api_key=groq_api_key)
    prompt = (f"Dime una canción de las mas conocidas del artista {artista} en formato JSON. "
              "Asegúrate de que la respuesta sea un JSON válido sin texto adicional. "
              "Ejemplo: {\"titulo\": \"Ejemplo\", \"artista\": \"{artista}\", \"genero\": \"Pop\", \"anio\": 2023}")
    
    response = client.chat.completions.create(
        model="mixtral-8x7b-32768",
        messages=[{"role": "system", "content": prompt}]
    )
    
    if response and response.choices:
        try:
            respuesta_texto = response.choices[0].message.content.strip()
            json_inicio = respuesta_texto.find("{")
            json_fin = respuesta_texto.rfind("}")
            if json_inicio != -1 and json_fin != -1:
                respuesta_json = respuesta_texto[json_inicio:json_fin + 1]
                cancion_data = json.loads(respuesta_json)
                return cancion_data
            else:
                print("Error: No se encontró un JSON válido en la respuesta.")
        except json.JSONDecodeError:
            print("Error al parsear la respuesta de Groq. La cadena no es un JSON válido.")
    else:
        print("Error obteniendo canción.")
    return None

def extraer_emojis(texto):
    pattern = re.compile("["  
                         u"\U0001F600-\U0001F64F"  # Emojis
                         u"\U0001F300-\U0001F5FF"  # Símbolos 
                         u"\U0001F680-\U0001F6FF"  # Transporte y mapas
                         u"\U0001F1E0-\U0001F1FF"  # Banderas (iOS)
                         "]+", flags=re.UNICODE)
    return ''.join(pattern.findall(texto))

def generar_emojis(titulo):
    client = groq.Client(api_key=groq_api_key)
    prompt = f"Devuelve únicamente 5 emojis, sin texto ni explicaciones, que representen el título de la canción '{titulo}'."
    response = client.chat.completions.create(
        model="mixtral-8x7b-32768",
        messages=[{"role": "system", "content": prompt}]
    )
    
    if response and response.choices:
        texto_generado = response.choices[0].message.content
        return extraer_emojis(texto_generado)
    else:
        print("Error generando emojis")
        return "❓❓❓"

def pedir_artista():
    while True:
        artista = input("Elige un artista (¡no puede estar vacío!): ").strip()
        if artista:  
            return artista
        else:
            print("¡El nombre del artista no puede estar vacío! Por favor, ingresa un nombre.")

def jugar():
    while True:
        artista = pedir_artista()
        cancion = obtener_cancion(artista)

        if cancion is None:
            print("No se pudo obtener la canción. Intentemos nuevamente.")
            continue

        titulo = cancion.get("titulo", "Desconocido")
        print("\nAdivina la canción:", generar_emojis(titulo))

        pistas = [
            f"Género: {cancion.get('genero', 'N/A')}",
            f"Año de lanzamiento: {cancion.get('anio', 'N/A')}",
            f"Artista: {cancion.get('artista', 'N/A')}",
            f"Iniciales: {''.join([w[0] for w in titulo.split()])}"
        ]
        
        intentos = 0
        puntos = 100  
        
        while intentos < len(pistas) + 1:
            respuesta = input("\nTu respuesta: ").strip()
            if respuesta.lower() == titulo.lower():
                print(f"¡Correcto! 🎉 Puntos: {puntos}")
                break
            elif intentos < len(pistas):
                print("Pista:", pistas[intentos])
                puntos -= 20  
            intentos += 1
        
        if intentos > len(pistas):
            print(f"\nPerdiste. La canción era: {titulo} de {cancion.get('artista', 'N/A')}. Puntos: 0")

        repetir = input("\n¿Quieres jugar otra vez? (s/n): ").strip().lower()
        if repetir != 's':
            break

if __name__ == "__main__":
    jugar()
