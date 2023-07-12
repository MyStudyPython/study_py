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
"""


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
        print(title, url)


def nba_area():
    print("===================进入专区选择=======================")
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
    for k, v in nba_dict.items():
        print(k, v["title"], v["url"])

    while True:
        choice = input(">>>>>>>>>>>>请选择下载序号(n/N):")
        if choice.upper() == "N":
            return
        choice_item = nba_dict.get(choice)
        if not choice_item:
            print("\n选择错误，请重新选择")
            continue
        # 下载需要title和url
        title, url = choice_item["title"], choice_item["url"]
        print(title, url)


def video_area():
    print("===================进入专区选择=======================")
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
    for k, v in video_dict.items():
        print(k, v["title"], v["url"])

    while True:
        choice = input(">>>>>>>>>>>>请选择下载序号(n/N):")
        if choice.upper() == "N":
            return
        choice_item = video_dict.get(choice)
        if not choice_item:
            print("\n选择错误，请重新选择")
            continue
        # 下载需要title和url
        title, url = choice_item["title"], choice_item["url"]
        print(title, url)


FUN_DIST = {"1": image_area, "2": nba_area, "3": video_area}


def main():
    while True:
        print("1.图片专区;2.NBA专区;3.短视频专区")
        choice = input(">>>>>>>>>>>请选择专区(q/Q):")

        # 用户选择是输入Q/q，终止程序。
        if choice.upper() == "Q":
            break

        choice_item = FUN_DIST.get(choice)
        # 选择错了重复选择（错误提示）
        if not choice_item:
            print("\n选择错误，请重新选择")
            continue

        # 选择对了进入专区
        choice_item()


main()
