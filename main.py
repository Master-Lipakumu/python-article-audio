#coding:utf-8

# importons nos differents package dans ce fichier
import nltk

nltk.download('punkt')

from newspaper import Article

from gtts import gTTS

#import playsound

import vlc


#insere le liens de l'article

url = "https://christiandev.pythonanywhere.com/Blog/article_detail/26"

article = Article(url)

#télécharger l'article

article.download()

article.parse()

article.nlp()

#convertir le text en audio

print(article.title)

mon_text = article.text

print(mon_text)


langage = 'fr'

my_audio = gTTS(text = mon_text, lang = langage, slow = False)

#sauvegarde du fichier audio

my_audio.save('audio_title.mp3')

#lancer / jouer le fichier audio avec vlc 

playeur = vlc.MediaPlayer("./audio_title.mp3")

playeur.play()

#jouer le fichier audio avec playsound

#playsound.playsound('audio_title.mp3')