# devtool

开发小工具



![image-20241115142607851](http://mark.lightr.cn/mark/image-20241115142607851.png?imageMogr2/auto-orient/blur/1x0/quality/80%7Cwatermark/2/text/QOS5mOmjjuW9kuWOuw==/font/5a6L5L2T/fontsize/260/fill/IzAwMDAwMA==/dissolve/58/gravity/SouthEast/dx/10/dy/10)

## 安装依赖

```bash
pip install "PySide6-Fluent-Widgets[full]" -i https://pypi.tuna.tsinghua.edu.cn/simple
```

兼容WIN7和老版WIN10使用下面安装命令

```bash
pip install PySide6==6.1.3  -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install PySide6-Fluent-Widgets -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install psutil -i https://pypi.tuna.tsinghua.edu.cn/simple
```

## 打包

使用auto-py-to-exe来打包项目

github:https://github.com/brentvollebregt/auto-py-to-exe

1.安装

```bash
pip install auto-py-to-exe -i https://pypi.tuna.tsinghua.edu.cn/simple
```

然后要运行它，请在终端中执行以下命令：

```bash
auto-py-to-exe
```

v1.0.1版本

```bash
pyinstaller --noconfirm --onedir --windowed --icon "E:/Code/Python/devtools/res/favicon.ico" --name "Lightr的小工具" --add-data "E:/Code/Python/devtools/res/log.png;."  "E:/Code/Python/devtools/Start.py"
```

## 启动

运行Start.py 即可

## 开发

敬请期待