import fire

def get_image(urls):
    import requests
    
    for url in urls:
        r=requests.get(url)
        
        try:
            filename=r.url.split('/')[-1]
        except:
            filename = "File1.jpg"
        
        print(filename)
        with open(filename,'wb') as f:
            f.write(r.content)

def load_data():
    import pandas as pd
    import os

    BASE_DIR = os.path.    
    df=pd.read_json('db/mayjune.json')
    return df


if __name__ == '__main__':
    fire.Fire({
        'load_data':load_data,
        'get_image':get_image,
    })