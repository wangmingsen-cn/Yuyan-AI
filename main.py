"""
语嫣AI员工管家 - 主入口
Yuyan AI Employee Manager - Main Entry

基于 Paperclip 架构重构的中文版 AI 员工管理系统
"""

import sys
import os
from pathlib import Path

# 添加 src 到路径
sys.path.insert(0, str(Path(__file__).parent))

from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

from src.core import init_database
from src.ui import MainWindow


def main():
    """主函数"""
    # 启用高DPI支持
    if hasattr(Qt, 'AA_EnableHighDpiScaling'):
        QApplication.setAttribute(Qt.ApplicationAttribute.AA_EnableHighDpiScaling, True)
    if hasattr(Qt, 'AA_UseHighDpiPixmaps'):
        QApplication.setAttribute(Qt.ApplicationAttribute.AA_UseHighDpiPixmaps, True)
    
    # 创建应用
    app = QApplication(sys.argv)
    app.setApplicationName("语嫣AI员工管家")
    app.setApplicationVersion("1.0.0")
    app.setOrganizationName("YuyanAI")
    
    # 设置字体
    font = QFont("Microsoft YaHei", 10)
    font.setStyleHint(QFont.StyleHint.SansSerif)
    app.setFont(font)
    
    # 确保数据目录存在
    data_dir = Path("data")
    data_dir.mkdir(exist_ok=True)
    
    # 初始化数据库
    db = init_database(str(data_dir / "yuyan.db"))
    
    # 创建主窗口
    window = MainWindow(db)
    window.show()
    
    # 运行应用
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
