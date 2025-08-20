import os

from PIL import Image as img

class ImageProcessor:
    def __init__(self, path: str):
        self.image = img.open(path)
        self.image_name, self.format = os.path.splitext(os.path.basename(self.image.filename))
        self.image_format = self.image.format
        self.width, self.height = self.image.size
        self.exif = self.image.getexif()
    
    def resize(self, width, height):
        self.image = self.image.resize((width, height))

    def crop(self, width, height):
        pass

    '''def _expor(self, format):
        if self.fmt.lower() in ["jpeg", "jpg"] and self.image.mode == "RGBA":
            self.image = self.image.convert("RGB")
        elif self.fmt.lower == "png" and self.image.mode == "RGBA" and not self.alpha:                
            self.image = self.image.convert("RGB")

        if self.resize:
            self.image = self.image.resize((self.width, self.height))
        else:
            self._crop()
            
        self.image.save(f"{self.image}_edit.{self.fmt}", format=self.fmt)'''
    
    def save(self, path):
        self.image.save(f'{path}/{self.image_name}{self.format}', format=self.image_format)

    @property
    def get_size(self) -> tuple:
        return self.width, self.height
    
    @property
    def get_exif(self) -> img.Exif:
        return self.exif

    @property
    def get_format(self):
        return self.image_format
    
    @property
    def get_name(self) -> str:
        return str(self.image_name)