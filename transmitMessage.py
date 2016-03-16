from pip._vendor.requests.packages import chardet

__author__ = 'zxz'

import urllib.parse
import urllib.request

url="http://ebusiness.coscon.com/NewEBWeb/public/cargoTracking/cargoTracking.xhtml"

values={"cargoTrackingPara":"6114408390"}
data=urllib.parse.urlencode(values)

data=data.encode('ASCII')

#创建请求对象
req=urllib.request.Request(url,data)
#获得服务器返回的数据
response=urllib.request.urlopen(req)
#处理数据
page=response.read()
page = page.decode("UTF-8","ignore")

print(page)