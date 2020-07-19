from pytube import YouTube
import ffmpeg

def save_audio(search_list):
    print("音声保存")
    for ID in search_list:
        query = 'https://www.youtube.com/watch?v=' + ID
        print(query+"を保存")
        yt = YouTube(query)
        stream = yt.streams.get_audio_only()
        stream.download("./videos")
        file_name = stream.default_filename
        print(file_name)

        # 音声取り出し→mp3化
        stream = ffmpeg.input("./videos/" + file_name)
        audio_stream = stream.audio
        output_name = "./audios/" + file_name.replace(".mp4","") + ".mp3"
        print("out/" + output_name)

        stream = ffmpeg.output(audio_stream, output_name)
        ffmpeg.run(stream)