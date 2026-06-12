import requests
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import FANGFANG_URL, STUDENT_ID, STUDENT_PASSWORD
from logger import logger

class FangfangLogin:
    """正方系统登录处理"""
    
    def __init__(self):
        self.session = requests.Session()
        self.cookies = None
        self.driver = None
    
    def login_with_selenium(self):
        """
        使用 Selenium 进行登录（处理JavaScript和验证码）
        
        Returns:
            bool: 登录是否成功
        """
        try:
            # 初始化 Chrome 浏览器
            options = webdriver.ChromeOptions()
            options.add_argument('--headless')  # 后台运行
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            
            self.driver = webdriver.Chrome(options=options)
            self.driver.get(FANGFANG_URL)
            
            logger.info("正在打开正方系统登录页面...")
            time.sleep(2)
            
            # 等待登录表单加载
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "login_txt"))
            )
            
            # 输入学号
            username_input = self.driver.find_element(By.ID, "login_txt")
            username_input.clear()
            username_input.send_keys(STUDENT_ID)
            logger.info(f"已输入学号: {STUDENT_ID}")
            
            # 输入密码
            password_input = self.driver.find_element(By.ID, "passwd")
            password_input.clear()
            password_input.send_keys(STUDENT_PASSWORD)
            logger.info("已输入密码")
            
            # 提交登录
            login_button = self.driver.find_element(By.ID, "submitBtn")
            login_button.click()
            logger.info("已点击登录按钮，等待页面加载...")
            
            # 等待登录完成
            time.sleep(3)
            
            # 获取 cookies
            self.cookies = self.driver.get_cookies()
            
            # 将 cookies 转换为 requests 可用的格式
            for cookie in self.cookies:
                self.session.cookies.set(cookie['name'], cookie['value'])
            
            logger.info("登录成功！")
            return True
            
        except Exception as e:
            logger.error(f"登录失败: {str(e)}")
            return False
        finally:
            if self.driver:
                self.driver.quit()
    
    def get_session(self):
        """获取登录后的 session"""
        return self.session
    
    def is_logged_in(self):
        """检查是否已登录"""
        try:
            response = self.session.get(FANGFANG_URL, timeout=5)
            # 如果返回登录页面，说明未登录
            if '登录' in response.text or 'login' in response.text.lower():
                return False
            return True
        except Exception as e:
            logger.error(f"检查登录状态失败: {str(e)}")
            return False