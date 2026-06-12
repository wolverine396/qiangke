#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
正方教育自动抢课工具
主程序入口
"""

import sys
from logger import logger
from config import MONITOR_INTERVAL, STUDENT_ID, STUDENT_PASSWORD
from fangfang_login import FangfangLogin
from course_monitor import CourseMonitor

def main():
    """主程序"""
    
    logger.info("=" * 50)
    logger.info("正方教育自动抢课工具启动")
    logger.info("=" * 50)
    
    # 检查必要的配置
    if not STUDENT_ID or not STUDENT_PASSWORD:
        logger.error("错误：未设置学号或密码，请在 .env 文件中配置")
        sys.exit(1)
    
    # 步骤1：登录正方系统
    logger.info("步骤1: 登录正方系统...")
    login = FangfangLogin()
    
    if not login.login_with_selenium():
        logger.error("登录失败，程序退出")
        sys.exit(1)
    
    session = login.get_session()
    
    # 步骤2: 初始化课程监控
    logger.info("步骤2: 初始化课程监控...")
    monitor = CourseMonitor(session)
    
    # 添加要监控的课程
    # 例子：monitor.add_course("高等数学", "12345")
    # 你需要替换成你自己想要抢的课程
    
    logger.info("请在 main.py 中配置要监控的课程")
    logger.info("示例:")
    logger.info('    monitor.add_course("课程名称", "课程ID")')
    logger.info('    monitor.add_course("高等数学", "12345")')
    
    # 临时示例（演示用）
    # monitor.add_course("示例课程1", "10001")
    # monitor.add_course("示例课程2", "10002")
    
    # 如果没有添加任何课程，提示用户
    if len(monitor.monitored_courses) == 0:
        logger.warning("未添加任何监控课程")
        logger.info("请编辑 main.py，在初始化课程监控后添加课程")
        sys.exit(0)
    
    # 步骤3: 开始监控
    logger.info("步骤3: 开始监控课程...")
    logger.info(f"监控间隔: {MONITOR_INTERVAL} 秒")
    logger.info("按 Ctrl+C 停止监控")
    
    monitor.start_monitoring(check_interval=MONITOR_INTERVAL)

if __name__ == '__main__':
    main()