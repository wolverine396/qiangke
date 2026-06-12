# 正方教育自动抢课工具

一个为杭州城市大学（HZCU）正方教学系统设计的自动抢课工具。

## 功能特性

- 🔐 自动登录正方系统
- 👀 持续监控指定课程
- ⚡ 有空位立即自动抢课
- 📧 邮件通知（成功/失败）
- 📝 详细日志记录

## 环境要求

- Python 3.8+
- Chrome 浏览器（用于登录处理）
- 网络连接

## 安装步骤

### 1. 克隆仓库
```bash
git clone https://github.com/wolverine396/qiangke.git
cd qiangke
```

### 2. 创建虚拟环境（推荐）
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. 安装依赖
```bash
pip install -r requirements.txt
```

### 4. 配置环境变量

复制 `.env.example` 为 `.env`：
```bash
cp .env.example .env
```

编辑 `.env` 文件，填入你的信息：
```
# 正方系统登录信息
FANGFANG_URL=http://ijw.hzcu.edu.cn/xtgl/index_initMenu.html
STUDENT_ID=你的学号
STUDENT_PASSWORD=你的密码

# QQ邮箱配置
EMAIL_SENDER=你的QQ邮箱
EMAIL_PASSWORD=你的QQ邮箱授权码
EMAIL_RECEIVER=接收通知的邮箱

# 抢课配置
MONITOR_INTERVAL=30  # 监控间隔（秒）
```

### 5. 获取 QQ 邮箱授权码

由于 QQ 邮箱的安全策略，不能直接使用密码，需要生成授权码：

1. 登录 [QQ 邮箱官网](https://mail.qq.com)
2. 点击 **设置** → **账户**
3. 找到 **POP3/IMAP/SMTP/Exchange/CardDAV/CalDAV 服务**
4. 点击 **生成授权码**
5. 按提示操作，复制生成的授权码到 `.env` 文件

## 使用方法

### 1. 配置要监控的课程

编辑 `main.py` 文件，在初始化课程监控后添加课程：

```python
# 步骤2: 初始化课程监控
monitor = CourseMonitor(session)

# 添加要监控的课程
monitor.add_course("课程名称1", "课程ID1")
monitor.add_course("课程名称2", "课程ID2")
```

**获取课程ID的方法**：
1. 登录教务系统
2. 进入选课界面
3. 按 F12 打开开发者工具
4. 找到课程对应的网络请求，查看课程ID

### 2. 运行程序

```bash
python main.py
```

程序会：
1. 登录正方系统
2. 开始监控指定的课程
3. 每隔 30 秒检查一次（可在 `.env` 中配置）
4. 发现有空位立即抢课
5. 发送邮件通知你

### 3. 停止程序

按 `Ctrl+C` 停止监控

## 文件说明

| 文件 | 说明 |
|------|------|
| `main.py` | 主程序入口 |
| `config.py` | 配置文件 |
| `logger.py` | 日志模块 |
| `fangfang_login.py` | 登录模块 |
| `course_monitor.py` | 课程监控和抢课模块 |
| `email_sender.py` | 邮件发送模块 |
| `.env.example` | 环境变量模板 |
| `requirements.txt` | 项目依赖 |

## 注意事项

⚠️ **重要提醒**：
- `.env` 文件包含敏感信息，**不要**上传到 GitHub
- 仅用于学习目的，遵守学校规定
- 使用本工具产生的后果由用户自行承担
- 不要频繁抢课，避免对系统造成压力

## 常见问题

### Q: 为什么登录失败？
A: 检查以下几点：
- 学号和密码是否正确
- 网络连接是否正常
- Chrome 浏览器是否已安装
- 是否需要输入验证码（目前程序不支持自动识别验证码）

### Q: 为什么邮件发送失败？
A: 检查以下几点：
- QQ 邮箱是否开启了 SMTP 服务
- 授权码是否正确
- 网络连接是否正常
- 查看 `logs/qiangke.log` 了解具体错误

### Q: 如何找到课程ID？
A: 1. 登录教务系统 → 2. 进入选课界面 → 3. F12 打开开发者工具 → 4. Network 标签页 → 5. 查看网络请求中的课程ID

### Q: 程序可以长时间运行吗？
A: 可以。建议在云服务器上运行，这样可以 24 小时监控。

## 技术栈

- **Python 3** - 编程语言
- **Selenium** - 自动化登录
- **Requests** - HTTP 请求
- **SMTP** - 邮件发送

## 贡献

欢迎提交 Issue 和 Pull Request！

## 许可证

MIT License

## 免责声明

本工具仅供学习和研究使用，使用者需自行承担使用本工具产生的所有后果。作者不对使用本工具造成的任何问题负责。

---

有问题？欢迎提交 [Issue](https://github.com/wolverine396/qiangke/issues)
