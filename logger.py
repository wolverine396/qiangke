import logging
import os
from config import LOG_DIR, LOG_FILE

# 创建日志目录
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# 配置日志
logger = logging.getLogger('qiangke')
logger.setLevel(logging.DEBUG)

# 文件处理器
file_handler = logging.FileHandler(LOG_FILE, encoding='utf-8')
file_handler.setLevel(logging.DEBUG)

# 控制台处理器
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# 日志格式
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# 添加处理器
logger.addHandler(file_handler)
logger.addHandler(console_handler)