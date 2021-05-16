# Python - Speech To Text Tutorial

@Talha KIYAK 

Bu belgeyi açıp okuyorsanız Metin Madenciliği alanına giriş yapmışsınız demektir. Öncelikle **Hoşgeldiniz**. 🙂

Bu yazıda, Machine Learning alanında yaptığım biritme tezinin (*"Türkçe Videoların Metin Tabanlı Sınıflandırılması"*) **veri seti oluşturma** kısmıyla ilgili aşama ve bilgiler anlatılacaktır.

İçerik olarak, çeşitli videoların veya ses dosyalarının metin formatına dönüştürülmesiyle ilgili kodlar ve bilgiler bulacaksınız. Kodlar, başlıktan da anlaşıldığı üzere '*Python*' kodları olacak.

Metin Madenciliği nedir, ne işe yarar? gibi soruları geçiyorum. Daha çok sizi, **kod** ve **yaşadığım zorluklar** anlamında kısa ve öz bir şekilde yazılmış bilgilendirici bir yazıyla baş başa bırakmak istiyorum.

# Problemimiz ve Bizden İstenen Nedir?

Sorunun cevabı: **Veri Seti**. Veri setimiz, 4 farklı sınıf altında 100'er Türkçe videodan oluşacak. Tabi ki bunlar video olarak kalmayacak metne dönüştürülecek.  Yani kısacası elimizde toplamda 400 metinli bir veri seti olacak. " Bu küçük bir veri seti " dediğinizi duyar gibiyim. Evet şu an için öyle. Ancak vereceğim bilgiler ve kod parçacıklarıyla sizler bu veri setini kısa bir sürede genişletebileceksiniz 😉

Oluşturulan bu veri setiyle çeşitli makine öğrenimi teknikleri kullanılarak metinlerin sınıflandırılması yapılacak. Sonunda da kullanılan farklı metot ve tekniklerin karşılaştırılması yapılacak. Ancak biz burada sadece veri setinin oluşturulması kısmı ile ilgileneceğiz.

Elimizde bir problem olduğuna göre, geriye mühendislikle bu problemi çözmek kalıyor 😎

Giriş olarak kullandığım teknolojileri tanıtmak istiyorum. Ne kullandığını bilmek ve tanımak çok önemli!

# Hangi Teknolojileri Kullandım?

### IDE

Öncelikle kodlamayı Python dilinde yaptığım için IDE olarak özellikle dosyalara erişim anlamında (sürekli dosyalarla uğraşacağız) kullanımı bana kolay gelen PyCharm platformunu kullandım.

![https://images.sftcdn.net/images/t_app-logo-xl,f_auto/p/70869b34-266c-495d-ba57-d11579a82a6a/759479654/pycharm-community-edition-PyCharm_Logo.svg.png](https://images.sftcdn.net/images/t_app-logo-xl,f_auto/p/70869b34-266c-495d-ba57-d11579a82a6a/759479654/pycharm-community-edition-PyCharm_Logo.svg.png)

(İndirme linkini de bırakıyorum.)

[Download PyCharm: Python IDE for Professional Developers by JetBrains](https://www.jetbrains.com/pycharm/download/#section=windows)

### Videolar

Veri setimizin temelini oluşturan videoları, Youtube video platformundan edindim.

![Python%20-%20Speech%20To%20Text%20Tutorial%20ce08f8bde6be4a8eb7aba0431220cee8/YouTube-Logo.png](Python%20-%20Speech%20To%20Text%20Tutorial%20ce08f8bde6be4a8eb7aba0431220cee8/YouTube-Logo.png)

### Videoyu Metne Dönüştürme (Speech To Text)

Videoları metne çevirmek için çok fazla API servisi var. Ancak ben bunlar arasından Google Cloud Speech API servisini kullandım. Web sitesinde nasıl çeviri yaptığını deneyebilirsiniz.   👇🏽

![Python%20-%20Speech%20To%20Text%20Tutorial%20ce08f8bde6be4a8eb7aba0431220cee8/gcp-speech.png](Python%20-%20Speech%20To%20Text%20Tutorial%20ce08f8bde6be4a8eb7aba0431220cee8/gcp-speech.png)

[Speech-to-Text: Automatic Speech Recognition | Google Cloud](https://cloud.google.com/speech-to-text)

**Veri seti oluştururken bu teknolojiler yeterli olacaktır** 👍🏽

Gelin artık yavaş yavaş giriş yapalım...

# Pekii Nereden ve Nasıl Başlayacağız?

İzleyeceğimiz adımlar TO-DO list'de belirtildiği gibi olacak. 

- [ ]  **Videoların elde edilmesi**
- [ ]  **Videoların isimlendirilmesi ve linklerinin depolanması**
- [ ]  **Videoların ses dosyalarına (.wav) dönüştürülmesi**
- [ ]  **Ses dosyalarının bölümlere ayrılması**
- [ ]  **Sesi metne dönüştürme**
- [ ]  **Parçalı metin dosyalarının ilgili isim altında birleştirilmesi**

Sizde bu aşamaları sırasıyla takip ederseniz sorun çıkmayacaktır. (Sıra önem taşımaktadır!)

# Videoların edinilmesi, isimlendirilmesi ve linkleri

Öncelikle videoların elde edilmesi ile işe koyuluyoruz. Bu aşamada önemli olan nokta, videoların sade ve anlaşılır konuşmaların geçtiği videolar olması. Arka planda konuşulan sesler ve müzik ise Google API servisi için sorun teşkil etmiyor korkmayın.🙂  Bu şekilde videoları tek tek test ederek indiriyoruz. *( İndirme işlemi için Youtube Premium kullanılabilir. )* İndirdiğimiz videolara hangi kategoriye ait olduğu ile birlikte bir de 'ID' numarası veriyoruz. Videoları isimlendirme aşaması çok önemli **!** Her sınıftaki video aynı düzende isimlendirilirse işimiz kolay olacaktır. Bunu ilerideki kodlarda anlayacaksınız. Ben aşağıdaki gibi isimlendirdim, size de bu şekilde tavsiye ederim kodda bana kullanım kolaylığı sağladı.

![Python%20-%20Speech%20To%20Text%20Tutorial%20ce08f8bde6be4a8eb7aba0431220cee8/deprem.png](Python%20-%20Speech%20To%20Text%20Tutorial%20ce08f8bde6be4a8eb7aba0431220cee8/deprem.png)

![Python%20-%20Speech%20To%20Text%20Tutorial%20ce08f8bde6be4a8eb7aba0431220cee8/ekonomi.png](Python%20-%20Speech%20To%20Text%20Tutorial%20ce08f8bde6be4a8eb7aba0431220cee8/ekonomi.png)

![Python%20-%20Speech%20To%20Text%20Tutorial%20ce08f8bde6be4a8eb7aba0431220cee8/pandemi.png](Python%20-%20Speech%20To%20Text%20Tutorial%20ce08f8bde6be4a8eb7aba0431220cee8/pandemi.png)

![Python%20-%20Speech%20To%20Text%20Tutorial%20ce08f8bde6be4a8eb7aba0431220cee8/spor.png](Python%20-%20Speech%20To%20Text%20Tutorial%20ce08f8bde6be4a8eb7aba0431220cee8/spor.png)

Ayrıca videoları edinirken dikkat edeceğimiz bir diğer hususta video linklerini depolamak. Ben, benden sonra çalışacak kişilerin videolara erişimini kolayca sağlaması için linkleri şimdilik text dosyasında tuttum. İlgili isim ve video numarası ile tabii. Daha sonra 'ID'leri ve sınıfları ile beraber linkleri veri tabanına aktaracağım.

# Videoların Ses Dosyasına (.wav) Dönüştürülmesi

Videoları neden ses dosyasına dönüştürüyoruz? diye sorabilirsiniz. Bunun nedeni, Google API servisimizin videoları ***.wav*** uzantısıyla alması. Ancak bu işlem o kadar kolay ki sadece 4 satırlık kodla işimizi hallediyoruz. Buyruun kodumuz...

```python
import moviepy.editor as mp
# ID numaralarıyla isimlendirdiğimiz videoları
# bir döngüyle istediğimiz formata dönüştürüyoruz. 
for x in range(1, 101):
    # Videoyu bulunduğu path den ilgili ismiyle alıyoruz
    clip = mp.VideoFileClip(r"D:\Bitirme_2021\Video Data\Pandemi\\"+str(x)+"_pandemi.mp4")
    # Tek bir fonksiyonla, yine bizim aynı isimle belirlediğimiz
    # formatta ilgili yola wav formatında kaydediyoruz
    clip.audio.write_audiofile(r"D:\Bitirme_2021\sounds\pandemi_wav\\"+str(x)+"_pandemi.wav")
```

Ses dosyaları hazır, artık metne çevirebilir miyiz? Maalesef Hayır. Çünkü bu aşamada Google API servisi ile ilgili bir sorun bizi karşılıyor. 🛑 **STOP**

---

Sorunumuz şu: Google 'ın Speech To Text API servisi, ücretsiz sürüm için sadece **1 dakika** uzunluğundaki videoları metne dönüştürmeye izin veriyor. *(Çoğu API servisinde olduğu gibi burada da karşımıza kısıt çıkıyor)* Bu da bizim videoları metne çevirmemize büyük ölçüde engel oluyor! Ücretli sürümü ne kadarmış ki ? derseniz bu proje geliştirilirken 1 dakikadan sonraki her 15 saniye için 0,006$ idi. [**Şu an ne kadardır bilemem.](https://cloud.google.com/speech-to-text/on-prem/pricing)** Video sayımızın ve uzunluğunun çok olması sebebiyle ücretli kısım bizi zorlayacağı için B planına geçtim.

![Python%20-%20Speech%20To%20Text%20Tutorial%20ce08f8bde6be4a8eb7aba0431220cee8/Untitled.png](Python%20-%20Speech%20To%20Text%20Tutorial%20ce08f8bde6be4a8eb7aba0431220cee8/Untitled.png)

# Ses Dosyalarının Bölümlere Ayrılması

B planımız basit, herbir videonun ses dosyasını 1 dakikalık parçalara ayırmak.🙂 Pekii 400 video veya ses dosyası için bu nasıl olacak? Mühendislikte çareler tükenmez. Bunun için Python kütüphanelerinden olan ***Pydub*** kütüphanesinin ***AudioSegment*** componentini kullandım. Kodu iliştiriyorum..

---

```python
# Gerekli kütüphaneler tanımlanarak eklendi
from pydub import AudioSegment
import math
```

❓Eğer bu kütüphaneler sizde yüklü değilse malum Python hata verecektir. Onun için PyCharm konsol ekranına ***pip install pydub*** yazarak indirmeniz yeterli.

```python
class SplitWavAudioMubin():
    def __init__(self, folder, filename):
        self.folder = folder
        self.filename = filename
        # Dosya yolu oluşturuyoruz
        self.filepath = folder + '\\' + filename
        # AudioSegment ile ses dosyasını alıyoruz
        self.audio = AudioSegment.from_wav(self.filepath)

    # Ses dosyasının uzunluğunu alıyoruz
    def get_duration(self):
        return self.audio.duration_seconds

    # Tekli ayırma fonksiyonu
    # Multiple fonksiyonunda çağrılacak
    def single_split(self, from_min, to_min, split_filename):
        t1 = from_min * 60 * 1000
        t2 = to_min * 60 * 1000
        split_audio = self.audio[t1:t2]
        # kaydedilecek yolun tanımı 
        split_audio.export('D:\Bitirme_2021\splitted_sounds\pandemi_splitted' + '\\' + split_filename, format="wav")

    # ayırılmak istenen dakika miktarını
    # parametre alan çoklu ayırma fonksiyonu
    def multiple_split(self, min_per_split):
        total_mins = math.ceil(self.get_duration() / 60)
        for i in range(0, total_mins, min_per_split):
            # Belirlediğimiz isim formatı
            split_fn = 'p' + str(i) + '_' + self.filename
            self.single_split(i, i + min_per_split, split_fn)
            print(str(i) + ' Done')
            if i == total_mins - min_per_split:
                print('All splited successfully')

# Ayrılmamış Ses dosyalarının olduğu path tanımı
folder = 'D:\\Bitirme_2021\sounds\pandemi_wav'
for x in range(1, 101):
    file = str(x)+'_pandemi.wav'
    split_wav = SplitWavAudioMubin(folder, file)
    split_wav.multiple_split(min_per_split=1)
```

Ses dosyalarımız şu şekilde oluştu:

![Python%20-%20Speech%20To%20Text%20Tutorial%20ce08f8bde6be4a8eb7aba0431220cee8/pandemisplit.png](Python%20-%20Speech%20To%20Text%20Tutorial%20ce08f8bde6be4a8eb7aba0431220cee8/pandemisplit.png)

![Python%20-%20Speech%20To%20Text%20Tutorial%20ce08f8bde6be4a8eb7aba0431220cee8/pandemisplit2.png](Python%20-%20Speech%20To%20Text%20Tutorial%20ce08f8bde6be4a8eb7aba0431220cee8/pandemisplit2.png)

![Python%20-%20Speech%20To%20Text%20Tutorial%20ce08f8bde6be4a8eb7aba0431220cee8/pandemisplit3.png](Python%20-%20Speech%20To%20Text%20Tutorial%20ce08f8bde6be4a8eb7aba0431220cee8/pandemisplit3.png)

![Python%20-%20Speech%20To%20Text%20Tutorial%20ce08f8bde6be4a8eb7aba0431220cee8/pandemisplit4.png](Python%20-%20Speech%20To%20Text%20Tutorial%20ce08f8bde6be4a8eb7aba0431220cee8/pandemisplit4.png)

*"p0, p1, p2 .."* şeklinde giden ön ek ile parçalı sesler elde etmiş olduk. Tabi her video aynı uzunlukta olmadığı için en sağdaki dosyalar gibi video numarasında atlamalar gözlemlenebilir. Örneğin deprem başlığında en uzun video için 11 küsür veya 12 dakikalık bir video olduğunu anlayabiliyoruz. 

Artık elimizdeki her video 1 dakikalık alanlara ayrıldı. Şimdi Google API servisini kullanabiliriz. Buyrun geçelim...

# Videoları Metne Dönüştürme

Artık temel noktamıza ulaşabildik. Şimdi parçalı ses dosyalarımızı metne çevirelim. Bunun için ***speech_recognation*** kütüphanesini kullanacağız. Bu kütüphane bizim Google Speech To Text API servisimizde çalışıyor. İlgili fonksiyonlar yardımıyla API'yi kodumuza gömmüş olacağız. Karşınızda Speech2Text kodu...

```python
# Google API servisini kullancağımız kütüphane
import speech_recognition as sr
# Dosya kontrolü için gerekli kütüphane
import os.path
from os import path
```

❓API kütüphanesini yüklemek için PyCharm konsol ekranına ***pip install SpeechRecognition*** yazmanız yeterli.

```python
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
```

 

Oluşturduğum bu metin veri setinin içeriğini kontrol ettiğimde Google'ın bazı sesleri hiç çevirmediğine rastladım. Ses dosyası mevcut, içerisinde konuşmalarda var ancak metin dosyası oluşmamış. Sorunun tam kaynağını anlamasamda benim şahsi görüşüm, API'nin konuşmaları anlamaması yönünde. Yani videodaki sesleri müzik veya başka bir ses zannediyor olması. Çünkü kimi videolarda da bu tarz eksik çevirimlere rastladım. Ancak genel tabloya baktığımda çok fazla dosyanın kayıp olmadığını gördüm.

 

Bu sorunla karşılaşmamak adına veri setini genişleteceklere -sizlere- önerim, seçilen videoların net konuşmalar olması. Mümkünse resmî bir konuşmanın yapıldığı videolar daha güzel çevriliyor.

Artık elimizde tüm sınıflar için metin dosyaları var. 😎 Ancak bunlar şu an parçalı haldeler ve bunların tek çatı altında birleşmesi gerekiyor.

![Python%20-%20Speech%20To%20Text%20Tutorial%20ce08f8bde6be4a8eb7aba0431220cee8/text.png](Python%20-%20Speech%20To%20Text%20Tutorial%20ce08f8bde6be4a8eb7aba0431220cee8/text.png)

![Python%20-%20Speech%20To%20Text%20Tutorial%20ce08f8bde6be4a8eb7aba0431220cee8/text2.png](Python%20-%20Speech%20To%20Text%20Tutorial%20ce08f8bde6be4a8eb7aba0431220cee8/text2.png)

![Python%20-%20Speech%20To%20Text%20Tutorial%20ce08f8bde6be4a8eb7aba0431220cee8/text3.png](Python%20-%20Speech%20To%20Text%20Tutorial%20ce08f8bde6be4a8eb7aba0431220cee8/text3.png)

![Python%20-%20Speech%20To%20Text%20Tutorial%20ce08f8bde6be4a8eb7aba0431220cee8/text4.png](Python%20-%20Speech%20To%20Text%20Tutorial%20ce08f8bde6be4a8eb7aba0431220cee8/text4.png)

# Parçalı Metin Dosyalarının Birleştirilmesi

Birleştirme işlemi için Python'da basit bir combine işlemi yapacağız. Ben susayım Python konuşsun🙂

```python
import os.path
from os import path

# text dosyalarının isimlerinin tutulduğu list
listOfTextFileNames = []

# Video ID numarasının kontrolü
for x in range(1,102):
	# dosya ilgili klasörde varsa listeye ekle
	for cnt in range(0,14):
		if (path.exists("D:\\Bitirme_2021\Splitted Texts\pandemi_Metinleri\\" + "p" + str(cnt) + "_" + str(x) + "_pandemi.txt")):
			listOfTextFileNames.append("D:\\Bitirme_2021\Splitted Texts\pandemi_Metinleri\\"+"p"+str(cnt)+"_"+str(x)+"_pandemi.txt")

	# 2. Döngü tamamlandıktan sonra
	# aynı isimle açılan .txt dosyasına listedeki metinleri ekle
	with open('D:\\Bitirme_2021\DATASET\\tekparca_pandemi\\' + str(x) + '_pandemi.txt', 'w') as outfile:

		# Listede dolaşıyoruz
		for names in listOfTextFileNames:
			# her bir dosya okuma modunda açılır
			with open(names) as infile:
				# listeden veriyi oku
				# ve açılan dosyaya yaz
				outfile.write(infile.read())

			# boşluk karakteri ile
			# dosyaları ayır
			outfile.write(" ")
	# Birleştirmeden sonra listeyi temizle
	listOfTextFileNames.clear()
```

Veee karşınızda veri seti 👏🏽

![Python%20-%20Speech%20To%20Text%20Tutorial%20ce08f8bde6be4a8eb7aba0431220cee8/dataset1.png](Python%20-%20Speech%20To%20Text%20Tutorial%20ce08f8bde6be4a8eb7aba0431220cee8/dataset1.png)

![Python%20-%20Speech%20To%20Text%20Tutorial%20ce08f8bde6be4a8eb7aba0431220cee8/dataset2.png](Python%20-%20Speech%20To%20Text%20Tutorial%20ce08f8bde6be4a8eb7aba0431220cee8/dataset2.png)

![Python%20-%20Speech%20To%20Text%20Tutorial%20ce08f8bde6be4a8eb7aba0431220cee8/dataset3.png](Python%20-%20Speech%20To%20Text%20Tutorial%20ce08f8bde6be4a8eb7aba0431220cee8/dataset3.png)

![Python%20-%20Speech%20To%20Text%20Tutorial%20ce08f8bde6be4a8eb7aba0431220cee8/dataset4.png](Python%20-%20Speech%20To%20Text%20Tutorial%20ce08f8bde6be4a8eb7aba0431220cee8/dataset4.png)

# Örnek

Örnek olması açısından buraya bir video, ses dosyası ve Google'ın API servisi ile elde ettiğimiz metin dosyasını koyuyorum.

### Video

[https://www.youtube.com/watch?v=AfazSfdP0mg](https://www.youtube.com/watch?v=AfazSfdP0mg)

### Ses Dosyası

[Python%20-%20Speech%20To%20Text%20Tutorial%20ce08f8bde6be4a8eb7aba0431220cee8/4_ekonomi.wav](Python%20-%20Speech%20To%20Text%20Tutorial%20ce08f8bde6be4a8eb7aba0431220cee8/4_ekonomi.wav)

### Metin Dosyası (.txt)

[4_ekonomi.txt](Python%20-%20Speech%20To%20Text%20Tutorial%20ce08f8bde6be4a8eb7aba0431220cee8/4_ekonomi.txt)

# GitHub

Tüm kodlara **GitHub** dan ulaşabilirsiniz.

![Python%20-%20Speech%20To%20Text%20Tutorial%20ce08f8bde6be4a8eb7aba0431220cee8/github-logo.png](Python%20-%20Speech%20To%20Text%20Tutorial%20ce08f8bde6be4a8eb7aba0431220cee8/github-logo.png)

[](https://github.com/tlh-k/speech2Text)

# Sonuç

Sonuç olarak bu yazıda, veri seti oluşturma ile ilgili birkaç yöntem ve karşılaştığım sorunları yazdım. Öğrendik ki, verileri toplamakta isimlendirme formatı çok önemli. Bu sayede birçok iş yükünden kurtulduk. Ayrıca karşılaştığımız çeşitli sorunlar karşısında pes etmeyerek çözüm bulduk. Sonunda verilen problemi çözmüş olduk.

Benim bu yazıyı yazmamdaki asıl amaç, sizlerin bu veri setini genişletirken aynı problemlerle vakit kaybetmemeniz ve geliştirdiğim kodlarla süreci hızlandırmanızdı. Umarım amacıma ulaşmış ve size az da olsa katkı sağlayabilmişimdir. Kusurum olduysa affola 😇

Hepinize Başarılar. İyi çalışmalar.

# Teşekkür

Bana bu süreçte maddi-manevi yardımcı olan herkese şükranlarımı sunuyorum. Bitirme projesi kapsamında yanımda olan Efnan hocama ve Salih hocama da ayrıca teşekkür ediyorum.

# *Yazar*

@Talha KIYAK 

> ***M. Talha KIYAK  -**  152120161021*

`ESOGU /*2021*`