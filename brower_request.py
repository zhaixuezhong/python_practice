__author__ = 'zxz'

import urllib
import urllib.request, urllib.parse, http.cookiejar
import urllib.parse

def get_html(url):
    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    opener.addheaders = [('User-Agent',
                          'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36'),
                         ('Cookie', '4564564564564564565646540')]

    urllib.request.install_opener(opener)

    html_bytes = urllib.request.urlopen(url).read()
    html_string = html_bytes.decode('utf-8')
    return html_string


def get_html_with_proxy(url_address):
    cj = http.cookiejar.CookieJar()

    try:

        proxy_support = urllib.request.ProxyHandler({'http': 'http://127.0.0.1:8087'})
        cookie_support = urllib.request.HTTPCookieProcessor(cj)
        opener = urllib.request.build_opener(proxy_support,cookie_support)
        opener.addheaders = [('User-Agent',
                      'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36'),
                     ('Cookie', '4564564564564564565646540')]
        urllib.request.install_opener(opener)
        request = urllib.request.Request(url_address)

        with urllib.request.urlopen(request) as url:
            #利用urlopen获取页面代码
            response = url.read()
        #将页面转化为UTF-8编码
        page_code = response.decode('gbk')
        page_code = page_code.encode('utf8')
        return page_code

    except urllib.error.URLError as e:
        if hasattr(e, "reason"):
            print(u"连接caoLiu失败,错误原因", e.reason)
            return None
