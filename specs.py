specs = [
    "Texture",
    "Thickness",
    "Size: ",
    "Color -",
    
]
IMG=[img for img in imgs if '.jpg' in img and img.startswith("images")]
prices: pattern=r'([\d|.]+)'
descriptions: pattern=r'(["\r|\n|\t|\s]+)'

def dl_image(list_of_images):
    BASE="https://knifekits.com/vcom/"
    for img in list_of_images:
        r=requests.get(BASE+img)
        filename=img.replace('images/','')
        with open(name,'wb') as f:
            print("Saving image as: {}".format(name))
            f.write(r.content)