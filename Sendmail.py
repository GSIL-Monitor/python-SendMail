#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header

class SendMail():
    def SendMailFun(self,sender,receivers,messageCon,subject):
        mail_host="smtp.qiye.163.com"                                 #设置服务器
        mail_user="fsd_ah_warning@vixtel.com"                         #用户名
        mail_pass="Vixtel205"                                         #口令 
 
        message = MIMEText(messageCon, 'plain', 'utf-8')              #邮件正文       
        message['From'] = Header(sender, 'utf-8')                     #邮件发送者名称
        message['To'] =  Header(','.join(receivers))                  #邮件接收者名称
        message['Subject'] = Header(subject, 'utf-8')
         
         
        try:
            smtpObj = smtplib.SMTP() 
            smtpObj.connect(mail_host, 25)                            # 25 为 SMTP 端口号
            smtpObj.login(mail_user,mail_pass)
            smtpObj.sendmail(sender, receivers, message.as_string())
            print ("邮件发送成功")
            smtpObj.quit()	
        except smtplib.SMTPException:
            print ("Error: 无法发送邮件")

if __name__ == "__main__":
    SendMailObj = SendMail()
    sender = 'fsd_ah_warning@vixtel.com'
    receivers = ['wenting.tang@vixtel.com','1160359812@qq.com']       #接收邮件，可设置为你的QQ邮箱或者其他邮箱     
    messageCon = 'Python 邮件发送测试...'                              #邮件正文
    subject = 'Python SMTP 邮件测试'                                   #邮件主题
    SendMailObj.SendMailFun(sender,receivers,messageCon,subject)
