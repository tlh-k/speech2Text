import moviepy.editor as mp
# ID numaralarıyla isimlendirdiğimiz videoları
# bir döngüyle istediğimiz formata dönüştürüyoruz. 
for x in range(1, 101):
    # Videoyu bulunduğu path den ilgili ismiyle alıyoruz
    clip = mp.VideoFileClip(r"D:\Bitirme_2021\Video Data\Pandemi\\"+str(x)+"_pandemi.mp4")
    # Tek bir fonksiyonla, yine bizim aynı isimle belirlediğimiz
    # formatta ilgili yola wav formatında kaydediyoruz
    clip.audio.write_audiofile(r"D:\Bitirme_2021\sounds\pandemi_wav\\"+str(x)+"_pandemi.wav")
