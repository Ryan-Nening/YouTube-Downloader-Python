from pytubefix import YouTube
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

try:
    url = input("Enter your YouTube URL:")
    yt = YouTube(url)

    print(f"Title: {yt.title}")
    print(f"Views: {yt.views}")

    print("Please select a folder to save the video...")
    save_path = filedialog.askdirectory()

    if not save_path:
        print("No folder selected. Download cancelled.")
    else:
        print("Downloading...")
        yd = yt.streams.get_highest_resolution()
        yd.download(output_path=save_path)
        
        print(f"Download complete! Saved to: {save_path}")

except Exception as e:
    print(f"An error occurred: {str(e)}")