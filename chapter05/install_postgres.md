
# install 
```shell
# 拉取镜像
docker pull postgres

# docker执行
docker run --name postgres -e POSTGRES_PASSWORD=pg123456 -e ALLOW_IP_RANGE=0.0.0.0/0  -p 5432:5432 -v D:\data\postgres:/var/lib/postgresql/data -d postgres
```