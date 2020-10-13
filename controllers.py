#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#レスポンス処理用

from fastapi import FastAPI
from starlette.requests import Request

app = FastAPI(
    title='FastAPIでつくるtoDoアプリケーション',
    description='FastAPIチュートリアル：FastAPI(とstarlette)でシンプルなtoDoアプリを作りましょう．',
    version='0.9 beta'
)


def index(request: Request):
    return {'Hello': 'World'}

