from pytube import YouTube
from collections.abc import Iterable

def downloadyoutubeaudio(videourl, outputpath):
    try:
        yt = YouTube(video_url)
        stream = yt.streams.filter(only_audio=True).first()
        print(f"Downloading: {yt.title}...")
        stream.download(output_path)
        print("Download completed.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")



# Replace 'VIDEO_URL' with the URL of the YouTube video you want to download audio from
video_url = "https://www.youtube.com/watch?v=oy2zDJPIgwc"
#Replace 'OUTPUT_PATH' with the path where you want to save the downloaded audio file
output_path = "./TrainingMusic/classical"
downloadyoutubeaudio(video_url, output_path)


