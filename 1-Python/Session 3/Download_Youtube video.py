#!/usr/bin/python3

from pytube import YouTube

def download_youtube_video(url, resolution='720p'):
    try:
        video = YouTube(url)
        stream = video.streams.filter(res=resolution).first()
        stream.download()
        print("Download complete!")
    except Exception as e:
        print("An error occurred:", str(e))

# Example usage
video_url = 'https://www.youtube.com/watch?v=IXgw_2LJmGE&list=PLkH1REggdbJpFXAzQqpjZgV1oghPsf9OH&index=1'  # Replace with the actual YouTube video URL
desired_resolution = '720p'  # Specify the desired resolution, e.g., '720p', '480p', '360p', etc.

download_youtube_video(video_url, desired_resolution)
