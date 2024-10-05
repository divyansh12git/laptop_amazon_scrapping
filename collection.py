import os
from bs4 import BeautifulSoup
import pandas as pd

d={'title':[],'price':[],'link':[]}
for file in os.listdir("data"):
    try:
        with open(f"data/{file}") as f:
            html_doc=f.read()
        soup= BeautifulSoup(html_doc,'html.parser')
        t=soup.find("h2")
        l=t.find("a")
        title=t.get_text()
        link=f"http://amazon.in{l['href']}"
        p=soup.find("span",attrs={"class":"a-price-whole"})
        price=p.get_text()
        # print(soup.prettify())
        # print(title, link, price)
        d["title"].append(title)
        d["link"].append(link)
        d["price"].append(price)
        
    except Exception as e:
        print(e)    


df=pd.DataFrame(d)
df.to_csv('data.csv')