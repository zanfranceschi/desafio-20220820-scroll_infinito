import random
import requests
import lorem

def generate(qty):
    items = []
    for i in range(qty):
        t = lorem.paragraph()
        has_image = random.choice([True, False, False, False, False, False])
        image = None
        if has_image:
            r_img = requests.get("https://picsum.photos/100", allow_redirects=False)
            image = r_img.headers["location"]
        
        items.append({ "text" : t, "image" : image })

    return items