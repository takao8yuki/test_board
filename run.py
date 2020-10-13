#!/usr/bin/env python
# coding: utf-8

# In[8]:


#サーバ立ち上げ用

from urls import app
import uvicorn

if __name__ == '__main__':
    #コンソールで[$ uvicorn run:app --reload]でも可
    uvicorn.run(app=app)


# In[9]:


jupyter lab --generate-config


# In[ ]:




