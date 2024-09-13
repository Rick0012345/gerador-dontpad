from spellchecker import SpellChecker
import random
from time import sleep
# Inicializa o verificador de palavras em português
spell = SpellChecker(language='pt')
link = 'http://dontpad.com/'
# Lista de palavras do dicionário em português
palavras_portugues = list(spell.word_frequency.keys())
while True:
# Gerar uma palavra aleatória
    palavra_gerada = random.choice(palavras_portugues)
   
    url = link + palavra_gerada
    print(url)
    sleep(1)


