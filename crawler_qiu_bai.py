import re
import time
import brower_request



html = brower_request.getHtml("http://www.qiushibaike.com/hot/page/1")
pattern = re.compile(
    '<div.*?author clearfix">.*?<a.*?<h2>(.*?)</h2>.*?content">(.*?)<!--(.*?)-->.*?</div>(.*?)<div class="stats.*?class="number hidden">(.*?)</span>',
    re.S)
items = re.findall(pattern, html)
for item in items:
    haveImg = re.search("img", item[3])
    if haveImg == None:
        nickName = item[0]
        content = item[1]
        content = content.replace("\n","").replace("<br/>","\n");
        timeStamp = item[2]
        x_data = time.localtime(int(item[2]))
        res_data = time.strftime('%Y-%m-%d %H:%M:%S',x_data)
        uproveCount = item[4]
        print("昵称:" + nickName, "\n内容：\n" + content, "\n发布时间：" + res_data, "\n点赞数：" + uproveCount,"\n\n\n")