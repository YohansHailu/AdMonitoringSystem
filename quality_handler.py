
import imquality.brisque as brisque
import PIL.Image

def calculate_photo_quality(image_path):
    img = PIL.Image.open(image_path)
    return brisque.score(img)




if __name__ == "__main__":
    image_path = "/home/yohansh/Pictures/hewan_photo.jpg" 
    print(calculate_photo_quality(image_path))

