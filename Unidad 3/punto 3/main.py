from textblob import TextBlob
from googletrans import Translator

def analizar_sentimiento(texto):
    # Traducir al inglés usando googletrans
    texto_ingles = translator.translate(texto, src='es', dest='en').text

    # Crea un objeto TextBlob con el texto traducido
    blob_ingles = TextBlob(texto_ingles)

    # Análisis de sentimiento
    sentimiento = blob_ingles.sentiment

    # Interpretar el sentimiento basado en la polaridad
    if sentimiento.polarity > 0.05:
        interpretacion = "positivo"
    elif sentimiento.polarity < -0.05:
        interpretacion = "negativo"
    else:
        interpretacion = "neutral"

    return sentimiento.polarity, sentimiento.subjectivity, interpretacion

# Inicializa el traductor de googletrans
translator = Translator()

# Conjunto de textos a analizar
textos = [
    "Este es un día maravilloso.",
    "Realmente odio este lugar.",
    "No tengo una opinión al respecto.",
    "Ese fue el mejor concierto al que he asistido."
]

# Analizar y imprimir los resultados para cada texto
for texto in textos:
    polaridad, subjetividad, interpretacion = analizar_sentimiento(texto)
    print(f"Texto: {texto}")
    print(f"Polaridad: {polaridad}")
    print(f"Subjetividad: {subjetividad}")
    print(f"El texto es {interpretacion}.\n")
