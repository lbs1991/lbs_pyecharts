from pyecharts.charts import Bar

bar1 = Bar()
bar1.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
bar1.add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
# render 会生成本地 HTML 文件，默认会在当前目录生成 render.html 文件
# 也可以传入路径参数，如 bar.render("mycharts.html")
bar1.render(path= "render_demo1.html")

# bar2 = (
#     Bar()
#     .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
#     .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
# )

num1 = (2)

print(bar1)
# print(type(bar2))
print(num1)

