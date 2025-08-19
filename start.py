from image import Image

def run():
    img = Image("test_img.png")
    img.resize(100, 500)

if __name__ == "__main__":
    run()
