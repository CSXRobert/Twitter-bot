# Creado por @CSXRobert

import time
import tweepy
import random

# Claves de la API de Twitter (reemplaza con tus propias claves)
API_KEY = 'TU_API_KEY_DE_TWITTER'
API_SECRET_KEY = 'TU_API_SECRET_KEY_DE_TWITTER'
ACCESS_TOKEN = 'TU_ACCESS_TOKEN_DE_TWITTER'
ACCESS_TOKEN_SECRET = 'TU_ACCESS_TOKEN_SECRET_DE_TWITTER'
BEARER_TOKEN = 'TU_BEARER_TOKEN_DE_TWITTER'

# Configura la conexión con Twitter usando la API V2
client = tweepy.Client(bearer_token=BEARER_TOKEN, consumer_key=API_KEY, consumer_secret=API_SECRET_KEY,
                       access_token=ACCESS_TOKEN, access_token_secret=ACCESS_TOKEN_SECRET)

# Función para leer el archivo de texto
def leer_archivo(archivo):
    with open(archivo, 'r', encoding='utf-8') as file:
        contenido = file.readlines()
    return [linea.strip() for linea in contenido]

# Función para publicar un tweet cada 35 minutos
def tweet_diario():
    tweets = leer_archivo('tweets.txt')
    frases = leer_archivo('frases.txt')
    total_tweets = len(tweets)
    total_frases = len(frases)

    while True:
        used_tweets = set()
        used_phrases = set()

        while len(used_tweets) < total_tweets and len(used_phrases) < total_frases:
            if len(used_tweets) == total_tweets:
                used_tweets.clear()  # Reiniciar la lista de tweets usados cuando se hayan publicado todos
            if len(used_phrases) == total_frases:
                used_phrases.clear()  # Reiniciar la lista de frases usadas cuando se hayan usado todas

            # Seleccionar un tweet y una frase aleatoria que no se hayan usado aún
            tweet_index = random.choice([i for i in range(total_tweets) if i not in used_tweets])
            frase_index = random.choice([i for i in range(total_frases) if i not in used_phrases])

            used_tweets.add(tweet_index)
            used_phrases.add(frase_index)

            tweet = f"{frases[frase_index]}\n{tweets[tweet_index]}"

            try:
                client.create_tweet(text=tweet)
                print(f'Tweet publicado: {tweet}')
            except tweepy.TweepyException as e:
                print(f'Error al publicar el tweet: {e}')

            time.sleep(35 * 60)  # Espera 35 minutos (35 * 60 segundos)

if __name__ == "__main__":
    tweet_diario()

