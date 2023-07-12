import requests, os

DB = {
    "1": {
        "area": "图片专区",
        "total_dict": {
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
        },
        "ext": "png",
        "selected": set(),
    },
    "2": {
        "area": "视频专区",
        "total_dict": {
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
        },
        "ext": "mp4",
        "selected": set(),
    },
    "3": {
        "area": "NBA专区",
        "total_dict": {
            "1": {
                "title": "威少奇才首秀三双",
                "url": "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0300fc20000bvi413nedtlt5abaa8tg&ratio=720p&line=0",
            },
            "2": {
                "title": "塔图姆三分准绝杀",
                "url": "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0d00fb60000bvi0ba63vni5gqts0uag&ratio=720p&line=0",
            },
        },
        "ext": "mp4",
        "selected": set(),
    },
}


def path():
    """路径"""
    abs_path = os.path.abspath(__file__)
    dir_path = os.path.dirname(abs_path)
    down_path = os.path.join(dir_path, "file")
    return down_path


def down_load(path, url):
    """下载文件"""
    res = requests.get(
        url=url,
        headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
        },
    )
    # 保存
    with open(path, mode="wb") as file_object:
        file_object.write(res.content)


def handler(area_info):
    summary = "欢迎进入{}专区".format(area_info["area"])
    print(summary)
    while True:
        text_list = []
        for key, value in area_info["total_dict"].items():
            # 判断key是否在selected中
            if key in area_info["selected"]:
                continue
            # value 分为 dict和tuple两种处理
            if type(value) == tuple:
                data = "{}.{}".format(key, value[0])
            elif type(value) == dict:
                data = "{}.{}".format(key, value["title"])
            text_list.append(data)
        # 转换为字符串输出
        if text_list:
            text = ";".join(text_list)
        else:
            print("无可用下载项，自动退出")
            return
        text = "{};Q.退出:".format(text)
        # 输出格式
        user_input = input(text).strip()
        if user_input.upper() == "Q":
            return
        if user_input in area_info["selected"]:
            print("此资源已被下载，无法继续下载")
            continue
        if not area_info["total_dict"].get(user_input):
            print("此序号不存在资源，请重新选择")
            continue
        # 获取路径和url
        lie = area_info["total_dict"].get(user_input)
        if type(lie) == tuple:
            file_path = os.path.join(path(), "{}.mp4".format(lie[0]))
            file_url = lie[1]
        elif type(lie) == dict:
            file_path = os.path.join(path(), "{}.mp4".format(lie["title"]))
            file_url = lie["url"]
        down_load(file_path, file_url)
        area_info["selected"].add(user_input)


print("欢迎使用资源下载器")
while True:
    user_input = input("进入专区选择：1.花瓣网图片专区 2.抖音短视频专区 3.NBA锦集专区 Q:退出 :").strip()
    if user_input.upper() == "Q":
        break
    # 寻找字典
    area_dict = DB.get(user_input)
    if not area_dict:
        print("输入错误，请重新输入")
        continue
    handler(area_dict)
