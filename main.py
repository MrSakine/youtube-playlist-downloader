import yt_dlp


def download_playlist(playlist_url, download_folder="downloads"):
    # Options for yt-dlp
    ydl_opts = {
        'format': 'best',  # Download the best quality
        # Save files to the specified folder
        'outtmpl': f'{download_folder}/%(title)s.%(ext)s',
        'noplaylist': False,  # Ensure that playlists are allowed
        'ignoreerrors': True,  # Continue downloading even if errors occur
        'progress_hooks': [download_hook],  # Hook for progress tracking
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])


def download_hook(d):
    if d['status'] == 'finished':
        print(f"Downloaded: {d['filename']}")
    elif d['status'] == 'downloading':
        print(f"Downloading: {d['_percent_str']} of {
              d['total_bytes']/(1024**2):.2f} MB")


if __name__ == "__main__":
    playlist_url = input("Enter YouTube playlist URL: ")
    download_folder = input(
        "Enter download folder (default is 'downloads'): ") or "downloads"
    download_playlist(playlist_url, download_folder)
