#!/venv/bin/python3

import requests
from lxml import html
import subprocess
from datetime import datetime
# subprocess.call('curl','https://knifekits.com/vcom/smproducts.xml', '-o', 'knifekits.xml')
# subprocess.call('curl','https://holstersmith.com/vcom/smproducts.xml', '-o', 'holstersmith.xml')

today=datetime.now()


def load_sitemap_local():
    kk = html.parse('knifekits.xml')
    hs = html.parse('holstersmith.xml')
        
    kk_url, kk_lastmod = kk.xpath("//url/loc/text()"), kk.xpath("//url/lastmod/text()")
    hs_url, hs_lastmod = hs.xpath("//url/loc/text()"), hs.xpath("//url/lastmod/text()")

    kk_map=[line for line in zip(kk_url,kk_lastmod)] # [('https://www.knifekits.com/vcom/product_info.php?products_id=3393', '2012-09-24T13:16:12-05:00'), ...]
    hs_map=[line for line in zip(hs_url,hs_lastmod)]

    new_kk = [line[0] for line in kk_map if "2020-05" in line[1] or "2020-06" in line[1]]
    new_hs = [line[0] for line in hs_map if "2020-05" in line[1] or "2020-06" in line[1]]
    urls_to_crawl = new_kk + new_hs
    return urls_to_crawl