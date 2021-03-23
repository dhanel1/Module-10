#!/usr/bin/env python
# coding: utf-8

# ### Visit the NASA Mars News Site

# In[1]:


# Import Splinter, BeautifulSoup, and Pandas
from selenium import webdriver
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
import webdriver_manager
drivervariable = webdriver.Chrome()
# Path to chromedriver
#!which chromedriver
# Set the executable path and initialize the chrome browser in splinter
executable_path = {'executable_path': r'C:\Users\DLH\Documents\Module 10\chromedriver'}
browser = Browser('chrome', **executable_path)


# In[2]:


# Visit the mars nasa news site
url = 'https://mars.nasa.gov/news/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)


# In[3]:


# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('ul.item_list li.slide')


# In[4]:


slide_elem.find("div", class_='content_title')


# In[5]:


# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find("div", class_='content_title').get_text()
news_title


# In[6]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_="article_teaser_body").get_text()
news_p


# ### JPL Space Images Featured Image

# In[7]:


# Visit URL
url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)


# In[8]:


# Find and click the full image button
full_image_elem = browser.find_by_id('full_image')
full_image_elem.click()


# In[9]:


# Find the more info button and click that
browser.is_element_present_by_text('more info', wait_time=1)
more_info_elem = browser.links.find_by_partial_text('more info')
more_info_elem.click()


# In[ ]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[ ]:


# find the relative image url
img_url_rel = img_soup.select_one('figure.lede a img').get("src")
img_url_rel


# In[10]:


# Use the base url to create an absolute url
img_url = f'https://www.jpl.nasa.gov{img_url_rel}'
img_url


# ### Mars Facts

# In[11]:


df = pd.read_html('http://space-facts.com/mars/')[0]

df.head()


# In[12]:


df.columns=['Description', 'Mars']
df.set_index('Description', inplace=True)
df


# In[13]:


df.to_html()


# ### Mars Weather

# In[14]:


# Visit the weather website
url = 'https://mars.nasa.gov/insight/weather/'
browser.visit(url)


# In[15]:


# Parse the data
html = browser.html
weather_soup = soup(html, 'html.parser')


# In[16]:


# Scrape the Daily Weather Report table
weather_table = weather_soup.find('table', class_='mb_table')
print(weather_table.prettify())


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres

# In[17]:


# 1. Use browser to visit the URL 
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)


# In[26]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []
html = browser.html
img_soup = soup(html,'html.parser')
imgs = img_soup.find_all('img')
for im in imgs:
    hemisphere_image_urls.append(im['src'])
#imgs = img_soup.find('img').get('src')
#print(imgs)
#print(hemisphere_image_urls)


          
# 3. Write code to retrieve the image urls and titles for each hemisphere.

for i in imgs:
    print('title: '+ i['alt'])
    print('image_url: '+url+i['src'])


# In[27]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[28]:


# 5. Quit the browser
browser.quit()


# In[ ]:




