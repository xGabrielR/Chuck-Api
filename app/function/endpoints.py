from os import path
from app.database.databases import database
from starlette.responses import JSONResponse

from starlette.requests import Request
from starlette.templating import Jinja2Templates

print(f'{path.abspath(".")}/app/view')

templates = Jinja2Templates(directory=f'{path.abspath(".")}/app/view')

async def home(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})

async def get_search_joke(requests):
    try:
        r = await database.fetch_all(f"select * from joke where value like '%{requests.query_params['query']}%'")
        r = [dict(i._mapping) for i in r]
        r = {"total": len(r), "result": r}

        return JSONResponse(r, status_code=200)
        
    except:
        return JSONResponse({"error_msg": f"query search term is obrigatory."}, status_code=400)

def get_categories_joke(requests):
    categories = ["animal","career","celebrity","dev","explicit","fashion",
                  "food","history","money","movie","music","political",
                  "religion","science","sport","travel"]
    
    return JSONResponse(categories, status_code=200)

async def get_random_joke(requests):
    try:
        r = await database.fetch_one(f"select * from joke where categories like '%{requests.query_params['category']}%' order by random() limit 1")
        r = dict(r._mapping)

    except:
        r = await database.fetch_one('select * from joke order by random() limit 1')
        r = dict(r._mapping)

    return JSONResponse(r, status_code=200)