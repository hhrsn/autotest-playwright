"""
配置模块 —— 统一读取 .env
"""
import os
from pathlib import Path
from dotenv import load_dotenv

# 项目根目录（config.py 在 utils/ 里，往上两级就是项目根）
ROOT_DIR = Path(__file__).resolve().parent.parent

# 加载 .env 文件 —— 之后 os.getenv 就能读到里面的值了
load_dotenv(ROOT_DIR / ".env")

# os.getenv("BASE_URL", "默认值")	
class Config:
    """全局配置，所有代码都从这里取值"""

    BASE_URL: str = os.getenv("BASE_URL", "https://www.saucedemo.com")

    STANDARD_USER: str = os.getenv("STANDARD_USER", "standard_user")
    LOCKED_USER: str = os.getenv("LOCKED_USER", "locked_out_user")
    PROBLEM_USER: str = os.getenv("PROBLEM_USER", "problem_user")
    PASSWORD: str = os.getenv("PASSWORD", "secret_sauce")
    
config = Config()
