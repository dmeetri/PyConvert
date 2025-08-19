import os

from PIL import Image as img

class ImageProcessor:
    def __init__(self, path: list, width: int, height: int, fmt: str, resize: bool, alpha: bool):
        self.path = path
        self.width = width
        self.height = height
        self.fmt = fmt.upper()
        self.resize = resize
        self.alpha = alpha
            
        #self.name, self.ext = os.path.splitext(self.img.filename)
        #self.img.save(f"{self.name}.{to}", format=to.upper(), quality=1)
        #self.img.save(f"{self.name}_resized{self.ext}")
    
    def _crop(self):
        pass

    def expor(self):
        all_images = self.path.copy()
        for file in all_images:
            image = img.open(file)

            if self.fmt.lower() in ["jpeg", "jpg"] and image.mode == "RGBA":
                image = image.convert("RGB")
            elif self.fmt.lower == "png" and image.mode == "RGBA" and not self.alpha:
                image = image.convert("RGB")

            if self.resize:
                image = image.resize((self.width, self.height))
            '''else:
                self._crop()'''
