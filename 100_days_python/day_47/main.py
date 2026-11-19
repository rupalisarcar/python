import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
import smtplib

load_dotenv()

# URL = "https://appbrewery.github.io/instant_pot/"
URL = "https://www.amazon.in/Divine-Trends-Antique-Bedroom-Decoration/dp/B0FQCJZMZT/ref=sr_1_3_sspa?_encoding=UTF8&content-id=amzn1.sym.bcff32d0-5f13-487d-a4da-8eb914919de2&crid=KEYJKBMZ2AME&dib=eyJ2IjoiMSJ9.EcvdetIt7PB4x9sYfCqFghvF4vD35FOnuGAvhaYKq-ipoYA30lhrlMDLPE8nK-ifgvIKK5o4N935i7CUAUxs9QfCsv-kMFM_4QgLekgjRdJ-8YtsCGCpkfFrRlhOxXFVxGcxJTWRDeTYftjUrIHTr7kqbacqU8ujQXGmFDaY3f3G1EXHVsEmCP9pJqlAgAYJ7xSf_j8szckT0C5fXfebPmBIquAqo-VbyU2jrmsztdBMkrEnGfhdzW0azzWPAGWgJD5i74Uj01LfKnFj41C0Hcynx5Xxe9taHBbUzqNxE2M.Xc7dXAArg38dxC_1-4aflo6ZsOK4-bVX7udRhhiUdmk&dib_tag=se&keywords=wall%2Blamps&pd_rd_r=2601cad8-fe2c-441f-bb2f-5fe6c1535738&pd_rd_w=vad5L&pd_rd_wg=RIcb1&qid=1794862028&refinements=p_72%3A1318476031&rnid=1318475031&s=kitchen&sprefix=wall%2Blamps%2Ckitchen%2C524&sr=1-3-spons&aref=nQ6Ls6RtPS&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1"
SMTP_ADDRESS = os.getenv("SMTP_ADDRESS")
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
PASSWORD = os.getenv("EMAIL_PASSWORD")

# Full headers would look something like this
header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-GB,de;q=0.8,fr;q=0.6,en;q=0.4,ja;q=0.2",
    "Dnt": "1",
    "Priority": "u=1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Sec-Gpc": "1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0",
}

# A minimal header would look like this:
# header = {
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
#     "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
# }

response = requests.get(url = URL, headers = header)
response.raise_for_status()

content = response.content

soup = BeautifulSoup(content,"html.parser")
price = soup.find(class_="a-price-whole").get_text()
title = soup.find(name="span",id="productTitle").get_text().strip()
print(title)
# price_without_currency = price.split('$')[1]
float_currency = float(price.replace(",", "").replace(".", ""))
print(float_currency)
MESSAGE = f"{title} is on sale for {float_currency}"
BUY_PRICE = 3000
if float_currency<BUY_PRICE:
    with smtplib.SMTP(SMTP_ADDRESS) as connection:
        connection.starttls()
        connection.login(user = EMAIL_ADDRESS, password = PASSWORD)
        connection.sendmail(msg=f"Subject:Amazon Price Alert!\n\n{MESSAGE}\n{URL}".encode("utf-8"), from_addr=EMAIL_ADDRESS, to_addrs="rikirock.012@gmail.com ")