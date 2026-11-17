# 商品关系分析

容器环境固定在仓库 Dockerfile 的 Python 3.11.14 镜像摘要，数值分析依赖与传递依赖在 requirements.txt 中精确锁定。执行 `docker build -t local-analytics .` 后，`docker run --rm --network none local-analytics` 运行内置例子；`docker run --rm --network none local-analytics python -m unittest discover -s tests -v` 运行测试。构建时安装依赖，运行时无需联网；非容器环境使用 Python 3.11，并先执行 `python -m pip install -r requirements.txt`。

该项目从合成购物篮数据生成共购关系摘要，并关联当前商品目录。

运行 `python -m unittest discover -s tests -v`；运行 `python -m assortment.demo`。共购只描述同时出现，不能单独证明替代或互补关系。

`assortment.merchandising.ShelfPlanner` 按商品宽度和排面数检查货架容量，只有当前在售商品可以预留空间；失败的调整不覆盖之前的计划。`related_candidates` 从现有共购分析中选择指定商品的关联候选。目前订单内重复行不增加共购次数，目录只区分在售状态，不具备商品沿革、库存暴露或替代候选估计。
