
import os
import requests
import fileinput
import sys

server_host = "127.0.0.1"
port = "36677"

upload_url = f"http://{server_host}:{port}/upload"

def upload_img(img_path_list):
    body = {
        "list": img_path_list
    }
    res = requests.post(upload_url, json=body).json()
    if res['success'] != True:
        print(f"失败:{res}")
        # print(res)
        return False
    print(f"成功:{res}")
    return res['result']


def read_file(file_path):
    img_list = []
    pwd = os.getcwd()
    with open(file_path, "r", encoding="utf-8") as f:
        while True:
            nstr = f.readline()
            if len(nstr) == 0:
                break
            # print(nstr)
            if "img/" in nstr or "img\\" in nstr:
                path = nstr[nstr.find('(')+1 : nstr.find(')')]
                full_path = (pwd+"/"+path).replace("\\", '/')
                img_list.append(full_path)

    return img_list
        


# 读取整个文件，返回一个img的path列表 绝对路径
def change_file(file_path, img_list):

    i = 0

    try:
        with fileinput.FileInput(file_path, inplace=True, backup=".bak", encoding="utf-8") as file:
            
            for line in file:
                
                if "img/" in line or "img\\" in line:
                    print(img_list[i], end='')
                    i += 1
                else:
                    print(line, end='')
    except Exception as e:
        print(e)
    





if __name__ == '__main__':

    dirname = os.listdir()

    for filename in dirname:
        if ".md" in filename and ".bak" not in filename:
            img_list = read_file(filename)
            print(img_list)

            url_list = upload_img(img_path_list=img_list)
            print(url_list)
            len = len(url_list)

            for i in range(len):
                url_list[i] = f"![]({url_list[i]})"

            print(url_list)
            change_file(filename, url_list)

    