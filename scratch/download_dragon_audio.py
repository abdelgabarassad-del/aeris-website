import subprocess
import sys
import os

def install_and_run():
    print("Installing yt-dlp...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "yt-dlp"])
    except Exception as e:
        print("Failed to install yt-dlp via pip:", e)
        return False
    
    import yt_dlp
    
    # Samuel Kim's HTTYD Epic Medley
    url = "https://www.youtube.com/watch?v=_iLHwp3Kxvw"
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'images/dragon_theme.%(ext)s',
    }
    
    print(f"Downloading {url}...")
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Download completed successfully!")
        return True
    except Exception as e:
        print("Error downloading audio:", e)
        return False

if __name__ == "__main__":
    os.makedirs("images", exist_ok=True)
    install_and_run()
