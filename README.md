# 语嫣AI员工管家 (Yuyan AI Employee Manager)

> 🌟 **零人力公司的开源编排系统** —— 赛博朋克风格中文版

<p align="center">
  <img src="assets/logo.png" alt="语嫣AI员工管家" width="400" />
</p>

<p align="center">
  <a href="#快速开始"><strong>快速开始</strong></a> ·
  <a href="#功能介绍"><strong>功能介绍</strong></a> ·
  <a href="#安装指南"><strong>安装指南</strong></a> ·
  <a href="#使用文档"><strong>使用文档</strong></a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue.svg" alt="Python 3.10+" />
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="MIT License" />
  <img src="https://img.shields.io/badge/UI-PyQt6-cyan.svg" alt="PyQt6" />
  <img src="https://img.shields.io/badge/Theme-Cyberpunk-purple.svg" alt="Cyberpunk Theme" />
</p>

---

## 🎯 项目简介

**语嫣AI员工管家** 是一款基于 Python + PyQt6 开发的桌面应用程序，采用未来科技赛博朋克风格设计。它是 [Paperclip](https://github.com/paperclipai/paperclip) 项目的中文重构版本，专为中文用户打造。

> "如果 OpenClaw 是一名**员工**，那么语嫣AI员工管家就是**整个公司**"

### 核心理念

语嫣AI员工管家是一个 AI 代理编排系统，帮助您管理一支由 AI 员工组成的团队来运营业务。您可以：
- 🏢 创建虚拟公司架构
- 👔 招聘各类 AI 员工（CEO、CTO、工程师、设计师、市场专员）
- 🎯 设定公司目标和任务
- 💰 监控成本和预算
- 📊 通过可视化仪表板追踪工作进度

---

## ✨ 功能特点

### 🎨 视觉设计

| 特性 | 描述 |
|------|------|
| **赛博朋克主题** | 霓虹灯效果、渐变边框、科技感配色 |
| **暗色/亮色模式** | 支持一键切换，适配不同使用场景 |
| **动态效果** | 脉冲动画、扫描线、发光效果 |
| **中文优化** | 完整中文化界面，符合中文用户习惯 |

### 🏢 公司管理

| 特性 | 描述 |
|------|------|
| **多公司支持** | 一个实例管理多个公司，数据完全隔离 |
| **组织架构** | 可视化组织架构图，清晰展示汇报关系 |
| **目标管理** | 层级目标设定，从公司使命到具体任务 |
| **预算控制** | 月度预算设置，超支自动预警 |

### 🤖 AI 员工管理

| 特性 | 描述 |
|------|------|
| **多种代理类型** | 支持 OpenClaw、Claude Code、Codex、Cursor 等 |
| **心跳机制** | 代理按计划唤醒，检查工作并执行 |
| **任务委派** | 上下级之间的任务自动委派 |
| **状态监控** | 实时查看代理运行状态 |

### 📋 任务系统

| 特性 | 描述 |
|------|------|
| **工单系统** | 每个对话都有完整追踪记录 |
| **优先级管理** | 高/中/低优先级设置 |
| **状态追踪** | 待办/进行中/已完成/阻塞状态 |
| **审批流程** | 重要操作需要审批才能执行 |

### 💰 成本控制

| 特性 | 描述 |
|------|------|
| **实时花费** | 实时监控 API 调用成本 |
| **预算设置** | 为每个代理和项目设置预算上限 |
| **超支保护** | 预算耗尽自动暂停代理 |
| **成本报表** | 详细的成本分析和报表 |

---

## 🚀 快速开始

### 环境要求

- Python 3.10 或更高版本
- Windows 10/11、macOS 或 Linux
- 至少 4GB 内存
- 500MB 磁盘空间

### 安装步骤

#### 方法一：使用安装包（推荐）

1. 下载最新版本的安装包
2. 运行安装程序
3. 启动应用，完成初始化设置

#### 方法二：从源码安装

```bash
# 1. 克隆仓库
git clone https://github.com/yourusername/yuyan-ai.git
cd yuyan-ai

# 2. 创建虚拟环境
python -m venv venv

# 3. 激活虚拟环境
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 4. 安装依赖
pip install -r requirements.txt

# 5. 启动应用
python main.py
```

### 首次使用

1. **创建管理员账号**
   - 首次启动时会提示创建 CEO 账号
   - 设置用户名和密码

2. **创建公司**
   - 点击"新建公司"
   - 输入公司名称和简称
   - 设置公司使命

3. **招聘第一个 AI 员工**
   - 进入"员工管理"
   - 点击"招聘员工"
   - 选择代理类型并配置

4. **创建第一个任务**
   - 进入"任务中心"
   - 点击"新建任务"
   - 分配给 AI 员工

---

## 📖 使用文档

### 界面概览

```
┌─────────────────────────────────────────────────────────────┐
│  语嫣AI员工管家                                    [_][□][X] │
├──────────┬──────────────────────────────────────────────────┤
│          │                                                  │
│  公司    │              主工作区                            │
│  导航栏  │                                                  │
│          │  ┌──────────────────────────────────────────┐   │
│  ┌───┐   │  │           数据仪表板                      │   │
│  │ A │   │  │  ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐       │   │
│  ├───┤   │  │  │ 12  │ │ 5   │ │ ¥2K │ │ 3   │       │   │
│  │ B │   │  │  │员工 │ │任务 │ │花费 │ │审批 │       │   │
│  ├───┤   │  │  └─────┘ └─────┘ └─────┘ └─────┘       │   │
│  │ C │   │  │                                          │   │
│  └───┘   │  │  ┌──────────────────────────────────┐   │   │
│          │  │  │        活动日志                   │   │   │
│          │  │  │  ● 员工A 完成了任务 #123          │   │   │
│          │  │  │  ● 员工B 开始处理任务 #124        │   │   │
│          │  │  │  ● 系统 检测到预算预警            │   │   │
│          │  │  └──────────────────────────────────┘   │   │
│          │  └──────────────────────────────────────────┘   │
├──────────┴──────────────────────────────────────────────────┤
│  状态栏: 已连接 | 公司: 示例科技 | 本月花费: ¥1,234         │
└─────────────────────────────────────────────────────────────┘
```

### 功能模块

#### 1. 仪表板 (Dashboard)
- 公司整体概况
- 实时数据卡片
- 活动日志
- 快捷操作

#### 2. 员工管理 (Agents)
- 查看所有 AI 员工
- 招聘新员工
- 配置员工参数
- 暂停/恢复员工

#### 3. 任务中心 (Issues)
- 任务列表
- 创建新任务
- 分配任务
- 跟踪进度

#### 4. 项目管理 (Projects)
- 项目列表
- 项目详情
- 工作空间
- 预算配置

#### 5. 目标管理 (Goals)
- 目标树
- 目标详情
- 进度追踪

#### 6. 审批中心 (Approvals)
- 待审批列表
- 审批历史
- 审批配置

#### 7. 成本中心 (Costs)
- 花费概览
- 预算管理
- 成本报表
- 预算预警

#### 8. 组织架构 (Org Chart)
- 可视化架构图
- 汇报关系
- 部门管理

---

## 🔧 配置说明

### 配置文件

配置文件位于 `config/settings.yaml`：

```yaml
# 应用设置
app:
  name: "语嫣AI员工管家"
  version: "1.0.0"
  theme: "cyberpunk"  # cyberpunk | light | dark
  language: "zh-CN"

# 数据库设置
database:
  type: "sqlite"
  path: "data/yuyan.db"

# API 设置
api:
  host: "127.0.0.1"
  port: 8080
  
# 代理适配器
adapters:
  openclaw:
    enabled: true
    gateway_url: "http://localhost:8080"
  claude:
    enabled: true
    api_key: "${CLAUDE_API_KEY}"
  codex:
    enabled: false
```

### 环境变量

| 变量名 | 说明 | 必需 |
|--------|------|------|
| `YUYAN_DATA_DIR` | 数据目录路径 | 否 |
| `YUYAN_CONFIG_DIR` | 配置文件目录 | 否 |
| `CLAUDE_API_KEY` | Claude API 密钥 | 否 |
| `OPENAI_API_KEY` | OpenAI API 密钥 | 否 |

---

## 🛠️ 开发指南

### 项目结构

```
yuyan-ai/
├── src/                    # 源代码
│   ├── core/              # 核心模块
│   │   ├── __init__.py
│   │   ├── company.py     # 公司管理
│   │   ├── agent.py       # 代理管理
│   │   ├── task.py        # 任务管理
│   │   ├── budget.py      # 预算管理
│   │   └── database.py    # 数据库
│   ├── ui/                # UI 模块
│   │   ├── __init__.py
│   │   ├── main_window.py # 主窗口
│   │   ├── dashboard.py   # 仪表板
│   │   ├── agents.py      # 员工管理
│   │   ├── issues.py      # 任务中心
│   │   ├── projects.py    # 项目管理
│   │   ├── goals.py       # 目标管理
│   │   ├── approvals.py   # 审批中心
│   │   ├── costs.py       # 成本中心
│   │   ├── org_chart.py   # 组织架构
│   │   ├── widgets/       # 自定义控件
│   │   │   ├── __init__.py
│   │   │   ├── cyberpunk_styles.py  # 赛博朋克样式
│   │   │   ├── neon_button.py       # 霓虹按钮
│   │   │   ├── holographic_card.py  # 全息卡片
│   │   │   └── data_table.py        # 数据表格
│   │   └── dialogs/       # 对话框
│   │       ├── __init__.py
│   │       ├── new_company.py
│   │       ├── new_agent.py
│   │       └── new_issue.py
│   ├── adapters/          # 代理适配器
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── openclaw.py
│   │   ├── claude.py
│   │   ├── codex.py
│   │   └── cursor.py
│   ├── utils/             # 工具函数
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── logger.py
│   │   └── helpers.py
│   └── main.py            # 入口文件
├── assets/                # 资源文件
│   ├── icons/            # 图标
│   ├── fonts/            # 字体
│   ├── images/           # 图片
│   └── themes/           # 主题文件
├── docs/                  # 文档
├── tests/                 # 测试
├── config/                # 配置
├── data/                  # 数据目录
├── requirements.txt       # 依赖
├── setup.py              # 安装脚本
└── README.md             # 本文件
```

### 开发环境搭建

```bash
# 1. 克隆仓库
git clone https://github.com/yourusername/yuyan-ai.git
cd yuyan-ai

# 2. 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. 安装开发依赖
pip install -r requirements-dev.txt

# 4. 运行测试
pytest

# 5. 启动开发模式
python main.py --dev
```

### 添加新的代理适配器

1. 在 `src/adapters/` 创建新的适配器文件
2. 继承 `BaseAdapter` 类
3. 实现必需的方法
4. 在配置中注册

示例：

```python
# src/adapters/my_adapter.py
from .base import BaseAdapter

class MyAdapter(BaseAdapter):
    name = "my_adapter"
    display_name = "我的适配器"
    
    async def execute(self, task: dict) -> dict:
        # 实现任务执行逻辑
        pass
    
    async def get_status(self) -> dict:
        # 实现状态查询逻辑
        pass
```

---

## 🤝 贡献指南

我们欢迎所有形式的贡献！

### 如何贡献

1. **Fork** 本仓库
2. 创建你的 **Feature Branch** (`git checkout -b feature/AmazingFeature`)
3. **Commit** 你的更改 (`git commit -m 'Add some AmazingFeature'`)
4. **Push** 到分支 (`git push origin feature/AmazingFeature`)
5. 创建 **Pull Request**

### 代码规范

- 遵循 PEP 8 规范
- 使用类型注解
- 编写单元测试
- 更新相关文档

---

## 📜 开源协议

本项目基于 [MIT License](LICENSE) 开源。

---

## 🙏 致谢

- 本项目基于 [Paperclip](https://github.com/paperclipai/paperclip) 重构
- 感谢所有贡献者的付出
- 特别感谢开源社区的支持

---

## 📞 联系我们

- **GitHub Issues**: [提交问题](https://github.com/yourusername/yuyan-ai/issues)
- **邮箱**: 294945908@qq.com
- **文档**: https://www.wangmingsen.cn/

---

<p align="center">
  <sub>Built with ❤️ by 语嫣AI团队</sub>
</p>
