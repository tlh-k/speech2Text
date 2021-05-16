import speech_recognition as sr
import os.path
from os import path

# API kütüphanesinden bir dinleyici tanımlandı
r = sr.Recognizer()
# bu kısım parçalı ses dosyasının
# parça numarasını temsil ediyor
# p0_1_ekonomi, p1_1_pandemi gibi
tmp_part = 0
# Bu döngü parçalı metinlerin ID sınırını koyuyor
# Pandemi için 13 e kadar dönecek --> p13_32_pandemi.wav gibi
for cntr in range(14):
    if (tmp_part < 14):
        # 100 adetlik video döngüsü
        # 'p0' dan sonraki video ID 'si
        # --> p0_1_pandemi.wav
        for x in range(1, 101):
            # belirtilen yolda var olan ses dosyasının kayda alınması
            audio = sr.AudioFile("D:\\Bitirme_2021\splitted_sounds\pandemi_splitted\\"+"p"+str(tmp_part)+"_"+str(x)+"_pandemi.wav")
            if(path.exists("D:\\Bitirme_2021\splitted_sounds\pandemi_splitted\\"+"p"+str(tmp_part)+"_"+str(x)+"_pandemi.wav")):
                with audio as source:
                    audio = r.record(source)
                    print("Recognizing...")
                # Konuşmayı metne çevirme kısmı
                # -Google API servisi ile-
                try:
                    # Bu testin amacı default olarak gelen API key'de problem oluşmasına karşın
                    # `r.recognize_google(audio)` bunun yerine
                    # diğer bir key'in kullanılması
                    # --> `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
                    print("Google Speech Recognition thinks you said in Turkish: -  " + r.recognize_google(audio, language = "tr-tr"))
                    with open('D:\\Bitirme_2021\Splitted Texts\pandemi_Metinleri\\'+'p'+str(tmp_part)+'_'+str(x)+'_pandemi.txt',mode ='w') as file:
                        file.write(r.recognize_google(audio, language = "tr-tr"))
                except sr.UnknownValueError:
                    print("Google Speech Recognition could not understand audio")
                except sr.RequestError as e:
                    print("Could not request results from Google Speech Recognition service; {0}".format(e))
        tmp_part += 1