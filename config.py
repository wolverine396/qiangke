import os
from dotenv import load_dotenv

# 加载 .env 文件中的环境变量
load_dotenv()

# 正方系统配置
FANGFANG_URL = os.getenv('FANGFANG_URL', 'http://ijw.hzcu.edu.cn/xtgl/index_initMenu.html')
STUDENT_ID = os.getenv('STUDENT_ID')
STUDENT_PASSWORD = os.getenv('STUDENT_PASSWORD')

# 邮件配置
EMAIL_SENDER = os.getenv('EMAIL_SENDER', '2801030489@qq.com')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD', 'aicbhyhipopydfgg')
EMAIL_RECEIVER = os.getenv('EMAIL_RECEIVER', '2801030489@qq.com')

# SMTP 服务器配置（QQ邮箱）
SMTP_SERVER = 'smtp.qq.com'
SMTP_PORT = 587

# 抢课配置
MONITOR_INTERVAL = int(os.getenv('MONITOR_INTERVAL', '30'))  # 监控间隔（秒）

# 日志配置
LOG_DIR = 'logs'
LOG_FILE = os.path.join(LOG_DIR, 'qiangke.log')