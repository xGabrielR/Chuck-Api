from starlette.routing import Mount, Route
from starlette.staticfiles import StaticFiles
from app.function import endpoints

routes = [ 
    Route('/', endpoint=endpoints.home),
    Mount('/static', app=StaticFiles(directory='app/view/static'), name='static'),
    Mount('/jokes', routes=[
        Route('/search', endpoint=endpoints.get_search_joke),
        Route('/random', endpoint=endpoints.get_random_joke),
        Route('/categories', endpoint=endpoints.get_categories_joke)
    ])
]
