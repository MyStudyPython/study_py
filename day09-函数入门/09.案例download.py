"""
案例：
资源下载管理器，系统有三大专区：图片专区、NBA专区、短视频专区
- 每个专区定义一个函数
- 用户去选择
  - 选择对了进入专区
  - 选择错了重复选择（错误提示）
  - 用户选择是输入Q/q，终止程序。
- 图片专区（NBA和短视频专区功能相同）
  - 罗列出来所有的序号和图片。
  - 让用户选择序号，用户选择哪个序号，则内部帮用户把这个图片下载下来。
  - 再次提示用户输入是否继续（n/N），返回上一级（让用户重新选择专区）



下载功能实现：
 - 需要参数 title 和 url
 - 安装第三方模块
  - python安装目录/Scripts/pip.exe install requests
  - pip3 install requests
 - 基于第三方模块进行下载

实现用户选择序号，图片/视频下载并报错
 - 图片，png为后缀
 - 视频，mp4为后缀

"""
import requests, os


def image_area():
    print("===================进入专区选择=======================")
    image_dict = {
        "1": (
            "吉他男神",
            "https://hbimg.huabanimg.com/51d46dc32abe7ac7f83b94c67bb88cacc46869954f478-aP4Q3V",
        ),
        "2": (
            "漫画美女",
            "https://hbimg.huabanimg.com/703fdb063bdc37b11033ef794f9b3a7adfa01fd21a6d1-wTFbnO",
        ),
        "3": (
            "游戏地图",
            "https://hbimg.huabanimg.com/b438d8c61ed2abf50ca94e00f257ca7a223e3b364b471-xrzoQd",
        ),
        "4": (
            "alex媳妇",
            "https://hbimg.huabanimg.com/4edba1ed6a71797f52355aa1de5af961b85bf824cb71-px1nZz",
        ),
    }
    for k, v in image_dict.items():
        print(k, v[0], v[1])

    while True:
        choice = input(">>>>>>>>>>>>请选择下载序号(n/N):")
        if choice.upper() == "N":
            return
        choice_item = image_dict.get(choice)
        if not choice_item:
            print("\n选择错误，请重新选择")
            continue
        # 下载需要title和url
        title, url = choice_item
        title = f"{title}.png"
        download_item(title, url)


def nba_area():
    nba_dict = {
        "1": {
            "title": "威少奇才首秀三双",
            "url": "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0300fc20000bvi413nedtlt5abaa8tg&ratio=720p&line=0",
        },
        "2": {
            "title": "塔图姆三分准绝杀",
            "url": "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0d00fb60000bvi0ba63vni5gqts0uag&ratio=720p&line=0",
        },
    }
    mp4_area(nba_dict)


def video_area():
    video_dict = {
        "1": {
            "title": "东北F4模仿秀",
            "url": "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0300f570000bvbmace0gvch7lo53oog",
        },
        "2": {
            "title": "卡特扣篮",
            "url": "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0200f3e0000bv52fpn5t6p007e34q1g",
        },
        "3": {
            "title": "罗斯mvp",
            "url": "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0200f240000buuer5aa4tij4gv6ajqg",
        },
    }
    mp4_area(video_dict)


def mp4_area(dict):
    print("===================进入专区选择=======================")
    for k, v in dict.items():
        print(k, v["title"], v["url"])

    while True:
        choice = input(">>>>>>>>>>>>请选择下载序号(n/N):")
        if choice.upper() == "N":
            return
        choice_item = dict.get(choice)
        if not choice_item:
            print("\n选择错误，请重新选择")
            continue
        # 下载需要title和url
        title, url = choice_item["title"], choice_item["url"]
        title = f"{title}.mp4"
        download_item(title, url)


def download_item(title, url):
    # 代码伪造浏览器的行为进行下载
    res = requests.get(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
        },
    )

    file_abs = os.path.abspath(__file__)
    file_dir = os.path.dirname(file_abs)
    file_path = os.path.join(file_dir, "file", title)

    # 创建文件路径的目录部分
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    # 保存到本地

    file_object = open(file_path, mode="wb")
    file_object.write(res.content)
    file_object.close()


fun_dist = {"1": image_area, "2": nba_area, "3": video_area}


def main():
    while True:
        print("1.图片专区;2.NBA专区;3.短视频专区")
        choice = input(">>>>>>>>>>>请选择专区(q/Q):")

        # 用户选择是输入Q/q，终止程序。
        if choice.upper() == "Q":
            break

        choice_item = fun_dist.get(choice)
        # 选择错了重复选择（错误提示）
        if not choice_item:
            print("\n选择错误，请重新选择")
            continue

        # 选择对了进入专区
        choice_item()


main()
