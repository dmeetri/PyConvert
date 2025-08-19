import os

from PIL import Image as img

class Image:
    def __init__(self, image_path: str):
        self.img = img.open(image_path)
        self.name, self.ext = os.path.splitext(self.img.filename)
    
    def convert(self, to: str):
        if to.lower() in ["jpeg", "jpg"] and self.img.mode == "RGBA":
            self.img = self.img.convert("RGB")

        self.img.save(f"{self.name}.{to}", format=to.upper(), quality=1)

    def resize(self, width: int, height: int):
        self.img = self.img.resize((width, height))
        self.img.save(f"{self.name}_resized{self.ext}")
    
    def crop(self):
        pass
    