__author__ = 'zxz'
# things i want to do!

import smtplib
from Email.mime.text import MIMEText
mailto_list=["zhaixuezhong@hotmail.com"]
mail_host="smtp.163.com"  #设置服务器
mail_user="zxzzxz_happy"    #用户名
mail_pass="xuezhong1314"   #口令
mail_postfix="163.com"  #发件箱的后缀

def send_mail(to_list,sub,content):
    login_name = mail_user + "@" + mail_postfix
    me="zxz"+"<"+login_name+">"
    msg = MIMEText(content,_subtype='plain',_charset='gb2312')
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    try:
        server = smtplib.SMTP_SSL(mail_host)
        # server.connect(mail_host)
        server.login(login_name,mail_pass)
        server.sendmail(me, to_list, msg.as_string())
        server.close()
        return True
    except Exception as e:
        print(str(e))
        return False
if __name__ == '__main__':
    if send_mail(mailto_list,"hello","hello world！"):
        print("发送成功")
    else:
        print("发送失败")