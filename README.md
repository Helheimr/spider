# Python爬虫

学习python爬虫后个人练习项目。


## yhdm_spider
**爬取 "http://www.yhdm.tv/" 下鬼灭之刃全集直链URL**

练习项目。

缘由: 追番之余，一念之下，发现yhdm的资源甚是可以 `1280*720 24帧`，
下载到本地，AMD补帧技术`AMD Fluid Motio`到`60帧`可获得良好视频体验。

未做下载，命名处理，简单的爬取视频直链URL。
原因当然是因为有更好的1080P资源。

## Instagram_spider
**爬取 Instagram 一个博主所有图片视频**

用法： 在代码中加上自己的cookie, 修改图片保存路径, 在命令行运行 python instagram.py user_name # 这里的user_name写上要爬的博主账号名称即可

>原作者：linqingmaoer
>项目地址：https://github.com/linqingmaoer/Instagram_crawler

## jz_txt_spider

自看小说，爬虫。时间短，处理的差，正则表达式去水印比较糟糕。

## hy_spider
**爬取 https://www.agefans.tv/ 下辉夜大小姐全集直链URL，添加下载功能**

相比以前多了you-get模块的下载功能。速度良心，跑满，某雷就不说了。

- 先从网页源码抓取关键参数`pc_play_vid_sign`,re,xpath,soup都行
- 构造异步请求就行，参数基本一样，`episodeidx`为1~集数，num为随机数，可有可无，`pc_play_vid_sign`才是决定请求的url链接。
<img src="https://upload.cc/i1/2019/11/06/prC503.png" alt="UTOOLS1573024963692.png" title="UTOOLS1573024963692.png" />
- 加了you-get下载，想用多线程优化，但总归来说网速一直也是满速，多线程也没必要，而且在实现pool.map函数的时候，传参时`list index out of range error`错误。就舍弃多线程。如下一直满速，比较满意。


<img src="https://upload.cc/i1/2019/11/06/mpbGSs.png" alt="UTOOLS1573024532859.png" title="UTOOLS1573024532859.png" />
