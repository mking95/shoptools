import datetime
import subprocess
import os
import re
import requests
from lxml import html
import pandas as pd


def dl_image_and_save(list_of_images, website="https://knifekits.com/vcom/"):
    BASE=website
    for img in list_of_images:
        r=requests.get(BASE+img)
        filename=img.replace('images/','')
        with open(name,'wb') as f:
            print("Saving image as: {}".format(name))
            f.write(r.content)


def save_data(filename):
    with open(filename,'w') as f:
        f.write(json.dumps(test))



def get_data(list_of_urls):
    errors=[]
    items=[]
    for url in list_of_urls:
        r=requests.get(url)
        
        if r.status_code != 200:
            errors.append(url)
        
        tree=html.fromstring(r.content)
        item = {}
        try:
            item["pid"]= tree.xpath(".//input[@name='products_id']/@value")[0]
            item["sku"]= tree.xpath( ".//*[@itemprop='model']/text()")[0]
            item["description"]= tree.xpath( ".//*[@itemprop='description']/descendant-or-self::text()[normalize-space(.)]") # list of strings
            item["metaKeywords"]= tree.xpath( ".//meta[@name='keywords']/@content")
            item["metaDescription"]= tree.xpath( ".//meta[@name='description']/@content")[0]
            item["main_img"]= tree.xpath( ".//div[@class='piGalMain']/img/@src")[0]
            item["main_img_width"]= tree.xpath( ".//div[@class='piGalMain']/img/@width")[0]
            item["main_img_height"]= tree.xpath( ".//div[@class='piGalMain']/img/@height")[0]
            item["images"]= tree.xpath( './/img/@src')
            item["title"]= tree.xpath( ".//title/text()")[0]
            item["name"]= tree.xpath( ".//span[@itemprop='name']/text()")
            item["breadcrumbs"]= tree.xpath( '//*[@class="breadcrumb"]/descendant::text()')[::2]
            item["url"]= tree.xpath( './/link[@rel="canonical"]/@href')[0]
            item["link_rel"]= tree.xpath( './/link[@rel="image_src"]/@href')[0]
            item["listing_page"]= tree.xpath( './/a[@id="btn2"]/@href')[0]
            item["price"] = tree.xpath('//*[@itemprop="price"]/@content')[0]
            
            items.append(item)
        except:
            print("Error! Item was not extracted!")
            items.append(r.url)

        print("items collected: {}".format(len(items)))    
        print("errors collected: {}".format(len(errors)))
        return items


def determine_urls_to_scrape():
    today=datetime.date.today()
    if today.month < 10:
        month="0"+str(today.month)
    else:
        month=str(today.month)
    t = str(today.year) + "-" + month
    
    subprocess.call("curl -o kk.xml https://knifekits.com/vcom/smproducts.xml")
    subprocess.call("curl -o hs.xml https://holstersmith.com/vcom/smproducts.xml")
    
    kk = html.parse('kk.xml')
    hs = html.parse('hs.xml')

    kk_url, kk_lastmod = kk.xpath("//url/loc/text()"), kk.xpath("//url/lastmod/text()")
    hs_url, hs_lastmod = hs.xpath("//url/loc/text()"), hs.xpath("//url/lastmod/text()")

    kk_map=[line for line in zip(kk_url,kk_lastmod)] # [('https://www.knifekits.com/vcom/product_info.php?products_id=3393', '2012-09-24T13:16:12-05:00'), ...]
    hs_map=[line for line in zip(hs_url,hs_lastmod)]

    new_kk = [ [line[0],line[1]] for line in kk_map if "2020-05" in line[1] or t in line[1]]
    new_hs = [ [line[0],line[1]] for line in hs_map if "2020-05" in line[1] or t in line[1]]
    
    
    urls_to_crawl = new_kk + new_hs

    
    return urls_to_crawl # [ url, '2020-05-12']

#########################
# Main
def main():    
    import requests
    import pandas as pd
    from lxml import html
    
    urls = determine_urls_to_scrape()
    
    
    cleaner=[ u[0] for u in urls]
    data=get_data(cleaner)
    filename = store_data(data)

    # report_data()
    # email_data()
    BASE_DIR = os.getcwd()
    db = os.path.join(BASE_DIR, 'db')
    save_data()




if __name__ == "__main__()":
    main()
