# 激活虚拟环境（在powershell下执行）
.\venv\Scripts\Activate.ps1

# 安装依赖和Playwright 浏览器内核
(venv) PS> pip install -r requirements.txt  
(venv) PS> playwright install chromium

# 运行脚本
(venv) PS> python main.py
