import fire

def fetch_image(urls):
    import requests
    
    for url in urls:
        r=requests.get(url)
        filename=r.url.split('/')[-1]
        print(filename)
        with open(filename, 'wb') as f:
            f.write(r.content)