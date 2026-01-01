import yt_dlp
import os

def download_youtube_playlist():
    playlist_url = input("Paste the YouTube Playlist URL: ").strip()
    
    save_folder = 'My_MP3_Collection'
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    ydl_opts = {
        'format': 'bestaudio/best',
        # SKIP ERRORS: This allows the script to keep going if a video is private
        'ignoreerrors': True, 
        # CLEAN FILENAMES: Removes special characters for better SD card compatibility
        'restrictfilenames': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }, {
            'key': 'FFmpegMetadata',
        }],
        'outtmpl': f'{save_folder}/%(title)s.%(ext)s',
        'noplaylist': False,
    }

    print(f"\n--- Starting download into folder: {save_folder} ---")
    print("--- Private or unavailable videos will be skipped automatically ---\n")
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([playlist_url])
        print(f"\n✅ Done! Your songs are in the '{save_folder}' folder.")
    except Exception as e:
        print(f"\n❌ A critical error occurred: {e}")

if __name__ == "__main__":
    download_youtube_playlist()