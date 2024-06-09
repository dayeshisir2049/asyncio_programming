from aiohttp import web
from aiohttp.web_request import Request
from aiohttp.web_response import Response
from asyncpg import Record
from asyncpg.pool import Pool

from chapter09 import create_database_pool, destory_database_pool, DB_KEY

routes = web.RouteTableDef()


@routes.get('/product/{id}')
async def product_detail(request: Request) -> Response:
    try:
        # 路由如果命中，id的值从match_info中获取 NOTE，参数都是字符串形式
        product_id = int(request.match_info['id'])
        query = 'select product_id, product_name, brand_id from product where product_id=$1'
        conn: Pool = request.app[DB_KEY]
        result: Record = await conn.fetchrow(query, product_id)
        if result is not None:
            return web.json_response(dict(result))
        else:
            return web.HTTPNotFound()
    except ValueError:
        raise web.HTTPBadRequest()


app = web.Application()
# 添加启动时 执行的协程列表
app.on_startup.append(create_database_pool)
# 添加清理时 执行的协程列表
app.on_cleanup.append(destory_database_pool)
app.router.add_routes(routes)
web.run_app(app)
