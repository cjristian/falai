import requests
import fal_client

MODEL = "fal-ai/flux/schnell"   

def generate_image_bytes(prompt: str) -> bytes:
    handler = fal_client.submit(MODEL, arguments={"prompt": prompt})
    result = handler.get()

    image_url = result["images"][0]["url"]
    r = requests.get(image_url, timeout=60)
    r.raise_for_status()
    return r.content
