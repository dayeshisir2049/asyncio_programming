from typing import Dict, List

from aiohttp import web
from aiohttp.web_request import Request
from aiohttp.web_response import Response
from asyncpg import Record
from asyncpg.pool import Pool

from chapter09 import create_database_pool, destory_database_pool, DB_KEY

routes = web.RouteTableDef()


@routes.get('/brand')
async def brands(request: Request) -> Response:
    # 从Requst中的app字段中，得到全局的app变量，app变量中的DB_KEY作为连接池的key
    conn: Pool = request.app[DB_KEY]
    brand_query = 'select brand_id, brand_name from brand'
    results: List[Record] = await conn.fetch(brand_query)
    result_as_dict: List[Dict] = [dict(brand) for brand in results]

    return web.json_response(result_as_dict)


app = web.Application()
# 添加启动时 执行的协程列表
app.on_startup.append(create_database_pool)
# 添加清理时 执行的协程列表
app.on_cleanup.append(destory_database_pool)
app.router.add_routes(routes)
web.run_app(app)
