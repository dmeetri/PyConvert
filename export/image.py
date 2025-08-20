import os

from PIL import Image as img

class ImageProcessor:
    def __init__(self, path: str):
        self.image = img.open(path)
    
    def resize(self, width, height):
        pass

    def crop(self, width, height):
        pass

    '''def expor(self, format):
        if self.fmt.lower() in ["jpeg", "jpg"] and self.image.mode == "RGBA":
            self.image = self.image.convert("RGB")
        elif self.fmt.lower == "png" and self.image.mode == "RGBA" and not self.alpha:                
            self.image = self.image.convert("RGB")

        if self.resize:
            self.image = self.image.resize((self.width, self.height))
        else:
            self._crop()
            
        self.image.save(f"{self.image}_edit.{self.fmt}", format=self.fmt)'''

    @property
    def get_size(self) -> tuple:
        return self.image.size
    
    @property
    def get_exif(self) -> img.Exif:
        return self.image.getexif()
