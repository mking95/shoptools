import fire

def clean_description(description):
    '''Parse list of strings / removes formatting'''
    cleaned=[]
    for line in description:
        cleaned.append(line.strip())
    return cleaned

def dl_image(url):
    import requests
    r=requests.get(url)
    r.raise_for_status()

    filename= url.split('/')[-1]
    print("Saving as hs/{}".format(filename))
    with open("hs/" + filename, 'wb') as f:
        f.write(r.content)
def get_img_urls(all_imgs):

    kk,hs=[],[]
    for i,url in enumerate(urls):
        try:
            if "knifekits" in url:
                full="https://knifekits.com/vcom/" + df.loc[i]['main_img']
                kk.append(full)
    
            else:
                full="https://holstersmith.com/vcom/" + df.loc[i]['main_img']
                hs.append(full)
        except:
            print(i)
        return (kk,hs)


if __name__ == "__main__":
    fire.Fire({
        'clean_description': clean_description,
        'dl_img': dl_image,
        'get_img_urls': get_img_url

    })
