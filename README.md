# 自动将 MarkDown 文件中的本地图片地址替换为图床外链地址

## 功能

本脚本可以将 markdown 格式文件中的**本地图片地址**，自动上传图床之后替换为**图床外链地址**。

本脚本使用 [PicGo](https://github.com/Molunerfinn/PicGo) 的服务进行图片上传。保证开启，并配置好PicGo的图床服务。

![image-20220330133228033](https://cdn.jsdelivr.net/gh/relaxcn/repo-img/img/202203301332079.png)

## 用法

> `.md`文件中的图片地址必须单独占一行

### 目录结构

保证目录结构为：

![image-20220330132954391](https://cdn.jsdelivr.net/gh/relaxcn/repo-img/img/202203301329441.png)

`img/`文件夹下是此 `.md`文件图片的储存地址。

![image-20220330133046444](https://cdn.jsdelivr.net/gh/relaxcn/repo-img/img/202203301330489.png)

移动脚本 `main.py` 到此目录下：

![image-20220330133400118](https://cdn.jsdelivr.net/gh/relaxcn/repo-img/img/202203301334154.png)

使用 `python main.py`解析执行。

等待执行完毕，这个过程不会打印其他信息。

之后打开`.md`文件即可发现，图片已经转换为 图床外链地址。

![image-20220330133645521](https://cdn.jsdelivr.net/gh/relaxcn/repo-img/img/202203301336554.png)