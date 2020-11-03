#!/usr/bin/env python
# coding: utf-8

# In[110]:


import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup
import requests
import pymongo


# In[158]:


executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


# In[4]:


url = 'https://mars.nasa.gov/news/'
browser.visit(url)


# In[5]:


html = browser.html
soup = BeautifulSoup(html, 'html.parser')

slides = soup.find('li', class_='slide')
for slide in slides:
    title = slide.find('div', class_='content_title').text
    news_p = slide.find('div', class_='article_teaser_body').text
    print(title)
    print(news_p)    
    


# In[38]:


url2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url2)


# In[39]:


images = soup.find('div', class_='default floating_text_area ms-layer')
browser.click_link_by_partial_text('FULL IMAGE')


# In[40]:


browser.click_link_by_partial_text('more info')


# In[49]:



html= browser.html
image = BeautifulSoup(html, 'html.parser')
#featured_image_url = image.find('figure', class_='lede').a['href']
featured_image_url = image.select_one('figure.lede a img').get('src')
featured_img_url = "https://www.jpl.nasa.gov" + featured_image_url
print(featured_img_url)


    
    #footer = image.find('footer')
    #link = footer.find('a')
    #featured_image_url = link[data-fancybox-href]
    #print(featured_image_url)
     


# In[10]:


url3 = 'https://space-facts.com/mars/'


# In[11]:


tables = pd.read_html(url3)
tables


# In[12]:


mars_facts = tables[0]
mars_facts


# In[51]:


mars_facts_html = mars_facts.to_html()
#print(mars_facts_html)


# In[159]:


url4 = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(url4)


# In[167]:


hemisphere_image_urls = []

links = browser.find_by_css("a.product-item h3")
for i in range(len(links)):    
    browser.find_by_css("a.product-item h3")[i].click()    
    data = BeautifulSoup(browser.html,'html.parser')
    hemi = {}
    title = data.find('h2', class_='title').get_text()
    img_url = data.find('a').get('href')
    hemi['title']=title
    hemi['img_url']=img_url
    print('Here')
    print(title)
    print(img_url)
    hemisphere_image_urls.append(hemi)
    browser.back()


# In[170]:


print(hemisphere_image_urls)

