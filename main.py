import uvicorn
from fastapi import FastAPI, Body
from starlette.middleware.cors import CORSMiddleware  # 引入 CORS中间件模块
from database_v1 import collection
from starlette.staticfiles import StaticFiles
# 导入jinja2模板引擎对象，用于后续使用
from starlette.templating import Jinja2Templates
# 导入Request上下文对象，用来在前后台之间传递参数
from starlette.requests import Request
from files.utils.file_content import get_content

app = FastAPI()
# 设置允许访问的域名
origins = [
    "http://127.0.0.1",
    "http://127.0.0.1:9527",
    "http://127.0.0.1:5000",
    "http://127.0.0.1:6000",
    "http://localhost:9527",
    # "http://localhost:9000",
    "*"
    # 也可以设置为"*"，即为所有。
]
# 设置跨域传参
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # 设置允许的origins来源
    allow_credentials=True,
    allow_methods=["*"],  # 设置允许跨域的http方法，比如 get、post、put等。
    allow_headers=["*"])  # 允许跨域的headers，可以用来鉴别来源等作用。

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory='templates')


@app.get("/files")
async def read_item(request: Request):
    return {"status":"True"}

# # 在视图函数中传入request对象，用于在模板对象中传递上下文（同时接收路径参数info，将其传递到上下文中）
@app.get('/files/{info}')
async def index(request: Request, info: str):
    print(info)
    context = {
        "request": request,
        "base_dir": "/",
        "file_name":"",
        "file": {"status": False},
        "info": {},
        'uplist': {"status": True, "url": ".."},
        'content': "",
    }
    context = get_content(context, info)
    # 返回一个模板对象，同时使用上下文中的数据对模板进行渲染
    return templates.TemplateResponse(name='file.html', context=context)

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=9000)
    # get_content({},"fefd")