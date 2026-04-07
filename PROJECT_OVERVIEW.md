# 语嫣AI员工管家 - 项目概览

## 📁 项目结构

```
yuyan-ai/
├── .github/workflows/          # GitHub Actions 工作流
│   ├── build.yml              # 构建和发布工作流
│   └── ci.yml                 # 持续集成工作流
├── assets/                     # 资源文件（图标、图片等）
├── config/                     # 配置文件
│   └── settings.example.yaml  # 配置示例
├── docs/                       # 文档
│   ├── FEATURES.md            # 功能介绍文档
│   └── INSTALL.md             # 安装操作说明
├── src/                        # 源代码
│   ├── adapters/              # 适配器模块
│   │   └── __init__.py        # 适配器基类和实现
│   ├── core/                  # 核心模块
│   │   ├── __init__.py
│   │   ├── company.py         # 公司管理
│   │   ├── agent.py           # AI员工管理
│   │   ├── task.py            # 任务管理
│   │   ├── budget.py          # 预算管理
│   │   └── database.py        # 数据库
│   ├── ui/                    # UI模块
│   │   ├── __init__.py
│   │   ├── main_window.py     # 主窗口
│   │   ├── dashboard.py       # 仪表板
│   │   ├── agents.py          # 员工管理
│   │   ├── issues.py          # 任务中心
│   │   ├── costs.py           # 成本中心
│   │   ├── org_chart.py       # 组织架构
│   │   ├── widgets/           # 自定义控件
│   │   │   ├── __init__.py
│   │   │   └── cyberpunk_styles.py  # 赛博朋克样式
│   │   └── dialogs/           # 对话框
│   │       └── __init__.py
│   └── utils/                 # 工具模块
│       └── __init__.py
├── tests/                      # 测试
│   ├── __init__.py
│   └── test_core.py           # 核心模块测试
├── main.py                     # 主入口
├── setup.py                    # 安装脚本
├── yuyan-ai.spec              # PyInstaller 配置
├── requirements.txt            # 依赖列表
├── requirements-dev.txt        # 开发依赖
├── README.md                   # 项目说明
├── LICENSE                     # 许可证
├── CHANGELOG.md               # 更新日志
├── CONTRIBUTING.md            # 贡献指南
└── .gitignore                 # Git忽略文件
```

## 🎯 核心功能

### 1. 公司管理 (Company)
- 多公司支持
- 公司信息配置
- 数据隔离

### 2. AI员工管理 (Agent)
- 多种角色：CEO、CTO、工程师、设计师等
- 多种适配器：OpenClaw、Claude、Codex、Cursor、Bash
- 状态管理：空闲、运行中、暂停、错误、离线
- 预算控制

### 3. 任务管理 (Task)
- 任务生命周期：待办 → 准备就绪 → 进行中 → 已完成
- 优先级：低、中、高、紧急
- 负责人分配
- 成本统计

### 4. 预算管理 (Budget)
- 多周期支持：日、周、月、年
- 预警机制
- 成本追踪

## 🎨 UI设计

### 赛博朋克风格
- 深色主题 (#0A0A0F)
- 霓虹强调色 (#00F0FF 青色, #FF00FF 洋红)
- 发光效果
- 中文优化

### 主要页面
1. **仪表板** - 数据概览、活动日志、最近任务
2. **员工管理** - 员工列表、招聘、配置
3. **任务中心** - 任务列表、创建、分配
4. **成本中心** - 预算管理、成本统计
5. **组织架构** - 可视化架构图

## 🛠️ 技术栈

- **Python 3.10+**
- **PyQt6** - GUI框架
- **SQLite** - 数据库
- **PyYAML** - 配置管理

## 📦 安装方式

### 方式一：源码安装
```bash
git clone https://github.com/yourusername/yuyan-ai.git
cd yuyan-ai
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
python main.py
```

### 方式二：打包安装
```bash
pip install pyinstaller
pyinstaller yuyan-ai.spec
```

## 🚀 快速开始

1. 启动应用
2. 创建管理员账号
3. 创建公司
4. 招聘AI员工
5. 创建任务并分配

## 📝 文档

- **README.md** - 项目说明和功能介绍
- **docs/INSTALL.md** - 详细安装指南
- **docs/FEATURES.md** - 功能详细介绍
- **CONTRIBUTING.md** - 贡献指南

## 🧪 测试

```bash
pip install -r requirements-dev.txt
pytest tests/
```

## 📄 许可证

MIT License - 详见 LICENSE 文件

## 🙏 致谢

本项目基于 [Paperclip](https://github.com/paperclipai/paperclip) 架构重构，感谢开源社区的支持。

---

**版本**: 1.0.0  
**作者**: 语嫣AI团队  
**日期**: 2026-04-07
