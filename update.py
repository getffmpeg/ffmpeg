
from pathlib import Path
import zipfile
import httpx

version = "7.0.2"
url = "https://github.com/GyanD/codexffmpeg/releases/download/7.0.2/ffmpeg-7.0.2-full_build-shared.zip"

def wirte_setup_file():
    with open("setup.iss", "r") as r:
        with open("default.iss", "w") as w:
            w.write(
                r.read().replace("$version", version).replace("$path", Path(url).stem)
            )

if __name__ == "__main__":
    filename = Path(url).name

    with httpx.stream("GET", url, follow_redirects=True) as client:
        with open(filename, "wb") as fp:
            for chunk in client.iter_bytes():
                fp.write(chunk)

    with zipfile.ZipFile(filename, "r") as fp:
        fp.extractall()
        wirte_setup_file()