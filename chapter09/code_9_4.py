from aiohttp import web
from aiohttp.web_request import Request
from aiohttp.web_response import Response
from asyncpg.pool import Pool

from chapter09 import create_database_pool, destory_database_pool, DB_KEY

routes = web.RouteTableDef()

PRODUCT_NAME = 'product_name'
BRAND_ID = 'brand_id'


@routes.post('/product')
async def create_product(request: Request) -> Response:
    if not request.can_read_body:
        raise web.HTTPBadRequest()

    body = await request.json()
    if PRODUCT_NAME not in body or BRAND_ID not in body:
        raise web.HTTPBadRequest()

    conn: Pool = request.app[DB_KEY]
    await conn.execute('''
        insert into product(product_id, product_name, brand_id) values (DEFAULT, $1, $2)
    ''', body[PRODUCT_NAME], body[BRAND_ID])
    return Response(status=201)


app = web.Application()
# 添加启动时 执行的协程列表
app.on_startup.append(create_database_pool)
# 添加清理时 执行的协程列表
app.on_cleanup.append(destory_database_pool)
app.router.add_routes(routes)
web.run_app(app)
