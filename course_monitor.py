import requests
import time
from datetime import datetime
from lxml import etree
from logger import logger
from email_sender import send_success_notification, send_error_notification

class CourseMonitor:
    """课程监控和抢课"""
    
    def __init__(self, session):
        """
        初始化课程监控
        
        Args:
            session: 登录后的 requests.Session 对象
        """
        self.session = session
        self.monitored_courses = []
        self.grabbed_courses = set()  # 已抢到的课程
    
    def add_course(self, course_name, course_id):
        """
        添加要监控的课程
        
        Args:
            course_name: 课程名称
            course_id: 课程ID
        """
        self.monitored_courses.append({
            'name': course_name,
            'id': course_id,
            'status': 'monitoring'
        })
        logger.info(f"已添加监控课程: {course_name} (ID: {course_id})")
    
    def check_course_availability(self, course_id):
        """
        检查课程是否有空位
        
        Args:
            course_id: 课程ID
        
        Returns:
            bool: 课程是否有空位
        """
        try:
            # 这里需要根据实际的正方系统接口调整
            # 通常是通过 AJAX 请求获取课程信息
            url = f"http://ijw.hzcu.edu.cn/courseSelect/queryCourse"
            params = {
                'courseId': course_id
            }
            
            response = self.session.get(url, params=params, timeout=5)
            
            if response.status_code == 200:
                # 解析响应，检查是否有空位
                # 这里需要根据实际的响应格式调整
                data = response.json() if response.text else {}
                
                # 示例逻辑，需要根据实际接口调整
                available = data.get('available', False)
                return available
            
            return False
            
        except Exception as e:
            logger.error(f"检查课程可用性失败: {str(e)}")
            return False
    
    def grab_course(self, course_id, course_name):
        """
        抢课
        
        Args:
            course_id: 课程ID
            course_name: 课程名称
        
        Returns:
            bool: 抢课是否成功
        """
        try:
            # 这里需要根据实际的正方系统接口调整
            url = "http://ijw.hzcu.edu.cn/courseSelect/selectCourse"
            data = {
                'courseId': course_id
            }
            
            response = self.session.post(url, data=data, timeout=5)
            
            if response.status_code == 200:
                result = response.json() if response.text else {}
                
                if result.get('success', False):
                    logger.info(f"抢课成功: {course_name}")
                    self.grabbed_courses.add(course_id)
                    send_success_notification(course_name)
                    return True
                else:
                    error_msg = result.get('message', '未知错误')
                    logger.warning(f"抢课失败: {course_name} - {error_msg}")
                    return False
            
            return False
            
        except Exception as e:
            logger.error(f"抢课异常: {str(e)}")
            send_error_notification(str(e))
            return False
    
    def start_monitoring(self, check_interval=30):
        """
        开始监控所有课程
        
        Args:
            check_interval: 检查间隔（秒）
        """
        logger.info(f"开始监控课程，检查间隔: {check_interval}秒")
        
        try:
            while True:
                current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                logger.info(f"[{current_time}] 正在检查课程...")
                
                for course in self.monitored_courses:
                    course_id = course['id']
                    course_name = course['name']
                    
                    # 如果已经抢到过，跳过
                    if course_id in self.grabbed_courses:
                        continue
                    
                    # 检查课程是否有空位
                    if self.check_course_availability(course_id):
                        logger.info(f"检测到课程有空位: {course_name}")
                        # 尝试抢课
                        self.grab_course(course_id, course_name)
                
                # 等待后继续检查
                time.sleep(check_interval)
                
        except KeyboardInterrupt:
            logger.info("停止监控")
        except Exception as e:
            logger.error(f"监控过程发生错误: {str(e)}")
            send_error_notification(str(e))
    
    def get_status(self):
        """获取监控状态"""
        status = {
            'total_courses': len(self.monitored_courses),
            'grabbed_courses': len(self.grabbed_courses),
            'courses': self.monitored_courses
        }
        return status