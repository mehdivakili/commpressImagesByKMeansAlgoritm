from PIL import Image
from compressByKMeans import compress_image_by_k_means


def load_image(path):
    image = Image.open(path)
    pixels = list(image.getdata())
    return pixels, image.mode, image.size


def save_image(image_data, path, image_mode, image_size):
    out = Image.new(image_mode, image_size)
    out.putdata(image_data)
    out.save(rf'{path}')
    return out


def main():
    image_data, image_mode, image_size = load_image(input("the path of image: "))
    image_data = compress_image_by_k_means(image_data, int(input("k: ")))
    save_image(image_data, input("the path of image to save: "), image_mode, image_size)


if __name__ == '__main__':
    main()
