"""
-   获得一个拥有smtp功能的邮箱
    -   基本所有的邮箱都有，可以在设置中打开smtp
    -   得到smtp服务器的地址
        -   -   smtp.exmail.qq.com(使用SSL，端口号465)
-   发送邮件的代码# 1.将python内置的模块（功能导入）

# 2.构建邮件内容
# 3.发送邮件 -   smtp.exmail.qq.com(使用SSL，端口号465) -   smtp.exmail.qq.com(使用SSL，端口号465)
-  
"""
# 1.将python内置的模块（功能导入）
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

# 2.构建邮件内容
msg = MIMEText("早知道就不问了，好尴尬啊！！！", "html", "utf-8")  # 内容
msg["From"] = formataddr(["li", "hq_yyk@126.com"])  # 自己名字/自己邮箱
msg["to"] = "1850115720@qq.com"  # 目标邮箱
msg["Subject"] = "害他们不会理我了。"

# 3.发送邮件 发送邮件的代码
server = smtplib.SMTP_SSL("smtp.126.com")
server.login("hq_yyk@126.com", "HBLDNWEWDJRSIDGL")  # 账号/授权码
server.sendmail("hq_yyk@126.com", "1850115720@qq.com", msg.as_string())  # 自己邮箱/目标邮箱/内容
server.quit()


"利用函数"

# 1.将python内置的模块（功能导入）
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

def send_mail():
    # 2.构建邮件内容
    msg = MIMEText("早知道就不问了，好尴尬啊！！！", "html", "utf-8")  # 内容
    msg["From"] = formataddr(["li", "hq_yyk@126.com"])  # 自己名字/自己邮箱
    msg["to"] = "1850115720@qq.com"  # 目标邮箱
    msg["Subject"] = "害他们不会理我了。"

    # 3.发送邮件 发送邮件的代码
    server = smtplib.SMTP_SSL("smtp.126.com")
    server.login("hq_yyk@126.com", "HBLDNWEWDJRSIDGL")  # 账号/授权码
    server.sendmail(
        "hq_yyk@126.com", "1850115720@qq.com", msg.as_string()
    )  # 自己邮箱/目标邮箱/内容
    server.quit()
send_mail()


"给多个对象发邮件 相当于一个循环，一个一个发，不是集体发送"
def send_mail(user_mail):
    msg = MIMEText("测试", "html", "utf-8")
    msg["From"] = formataddr(["li", "hq_yyk@126.com"])
    # msg["To"] = "1850115720@qq.com" 
    msg["Subject"] = "happy new year"

    # 3.发送邮件 发送邮件的代码
    server = smtplib.SMTP_SSL("smtp.126.com")
    server.login("hq_yyk@126.com", "HBLDNWEWDJRSIDGL")  # 账号/授权码
    server.sendmail(
        "hq_yyk@126.com", user_mail, msg.as_string()
    )  # 自己邮箱/目标邮箱/内容
    server.quit()

user_mail_list = ['1850115720@qq.com','hqyyk@163.com']
for user_mail in user_mail_list:
    send_mail(user_mail)
