import whisper
import pytube

def youtubeTranscription():
    videoId = str(input("Ingresa la Url => "))
    name = str(input('Ingresa nombre de la salida => ')) 
    model = whisper.load_model('small')

    youtubeVideo = pytube.YouTube(videoId)
    audio = youtubeVideo.streams.get_audio_only()
    audio.download(filename=f'files/{name}.mp4')
    result = model.transcribe(f'files/{name}.mp4')
    with open(f'files/outputs/{name}.txt', 'w') as f:
        f.write(result["text"])
        print(f)
youtubeTranscription()