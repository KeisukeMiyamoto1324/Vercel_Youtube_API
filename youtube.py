from langchain_community.document_loaders import YoutubeLoader
import requests
import base64

def getCaption(videoID: str) -> str:
    try:
        loader = YoutubeLoader.from_youtube_url(
            f"https://www.youtube.com/watch?v={videoID}", language=["en", "ja"]
        )

        return loader.load()[0].page_content
    except:
        return None
    
def getThumbnail(videoID: str) -> bytes:
    url = f"https://img.youtube.com/vi/{videoID}/maxresdefault.jpg"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.content
    else:
        return None

def encode_image_to_base64(image_bytes):
    base64_bytes = base64.b64encode(image_bytes)
    base64_string = base64_bytes.decode('utf-8')

    return base64_string

def save_base64_image_to_jpeg(base64_string, output_path="test.jpeg"):
    image_bytes = base64.b64decode(base64_string)

    with open(output_path, 'wb') as image_file:
        image_file.write(image_bytes)