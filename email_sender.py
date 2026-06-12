import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import EMAIL_SENDER, EMAIL_PASSWORD, EMAIL_RECEIVER, SMTP_SERVER, SMTP_PORT
from logger import logger

def send_email(subject, body, is_html=False):
    """
    发送邮件通知
    
    Args:
        subject: 邮件主题
        body: 邮件内容
        is_html: 是否为HTML格式
    
    Returns:
        bool: 发送是否成功
    """
    try:
        # 创建邮件对象
        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = EMAIL_SENDER
        msg['To'] = EMAIL_RECEIVER
        
        # 添加邮件内容
        if is_html:
            msg.attach(MIMEText(body, 'html', 'utf-8'))
        else:
            msg.attach(MIMEText(body, 'plain', 'utf-8'))
        
        # 连接SMTP服务器并发送
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()
        
        logger.info(f"邮件发送成功: {subject}")
        return True
        
    except Exception as e:
        logger.error(f"邮件发送失败: {str(e)}")
        return False

def send_success_notification(course_name):
    """发送抢课成功通知"""
    subject = f"【抢课成功】{course_name}"
    body = f"""
抢课成功！

课程: {course_name}
时间: {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

请立即登录教务系统查看并确认。
    """
    send_email(subject, body)

def send_error_notification(error_msg):
    """发送错误通知"""
    subject = "【抢课工具】发生错误"
    body = f"""
抢课工具发生错误，请检查：

错误信息: {error_msg}
时间: {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

请查看日志文件了解详情。
    """
    send_email(subject, body)