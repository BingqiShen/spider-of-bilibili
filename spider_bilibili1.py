# -*- coding:UTF-8 -*-
import sys
from you_get import common as you_get       #导入you-get库
import requests
import bilibili_class
import time
from xlutils.copy import copy
import xlrd
import xlwt
import numpy as np


headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36"}


def require_video(video_id):
    URL_VIDinfo = "http://api.bilibili.com/archive_stat/stat?aid="   #b站视频信息api
    PARAMS = {"aid":video_id }
    VID_info = requests.get(url = URL_VIDinfo,params = PARAMS).json()
    if(VID_info["message"] == "0"):
        hot_video = VID_info["data"]["view"]
        if hot_video != "--":
            return hot_video
        else:
            return -1
    else:
        return -1

def main(path,video_id):
    video = require_video(video_id)
    if (video == -1):
        print("video id为：" + str(video_id) + "的视频不存在")
    elif (int(video) >= 1):  # 浏览数判断
        print("video id为：" + str(video_id) + "的视频的播放量为：" + str(video))

        directory = path  # 设置下载目录
        url = 'https://www.bilibili.com/video/av{}/'.format(video_id)  # 需要下载的视频地址
        title = bilibili_class.getVideo_title(url)
        tag = '萌' # 可修改标签，下载不同视频
        result = tag in title
        if result is True:      # 符合标签及浏览数指标，可以下载
            sys.argv = ['you-get', '-o', directory, url]  # sys传递参数执行下载，就像在命令行一样
            you_get.main()
            print('可下载')
            return title,url

    else:
        pass
    time.sleep(1)

if __name__ == "__main__":
    for video_id in range(10000, 20000):
        main('bilibili',video_id)

