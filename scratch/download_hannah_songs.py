import os
import sys
import subprocess

SONGS = {
    "arabella": "ytsearch1:Arctic Monkeys Arabella",
    "do_i_wanna_know": "ytsearch1:Arctic Monkeys Do I Wanna Know",
    "take_me_to_church": "ytsearch1:Hozier Take Me to Church",
    "five_am_in_paris": "ytsearch1:Saint Levant 5am in Paris",
    "comme_cest_beau": "ytsearch1:Saint Levant Comme C'est Beau"
}

def install_ytdlp():
    print("Installing yt-dlp...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "yt-dlp"])
        return True
    except Exception as e:
        print("Failed to install yt-dlp:", e)
        return False

def download_songs():
    import yt_dlp
    
    os.makedirs("images", exist_ok=True)
    
    for name, url in SONGS.items():
        print(f"Downloading {name} from {url}...")
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': f'images/{name}.%(ext)s',
            'ignoreerrors': True,
        }
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            print(f"Finished downloading {name}")
        except Exception as e:
            print(f"Error downloading {name}: {e}")

if __name__ == "__main__":
    if install_ytdlp():
        download_songs()
        
        # List the files downloaded to check extensions
        print("\nDownloaded files in images/:")
        for f in os.listdir("images"):
            if any(name in f for name in SONGS.keys()):
                print(f" - {f}")
