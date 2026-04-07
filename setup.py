"""
Setup script for 语嫣AI员工管家
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read README
readme_path = Path(__file__).parent / "README.md"
long_description = readme_path.read_text(encoding="utf-8") if readme_path.exists() else ""

# Read requirements
requirements_path = Path(__file__).parent / "requirements.txt"
requirements = []
if requirements_path.exists():
    requirements = [
        line.strip() 
        for line in requirements_path.read_text().splitlines()
        if line.strip() and not line.startswith("#")
    ]

setup(
    name="yuyan-ai-employee-manager",
    version="1.0.0",
    author="语嫣AI团队",
    author_email="support@yuyan-ai.com",
    description="语嫣AI员工管家 - 零人力公司的开源编排系统",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/yuyan-ai",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Office/Business",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.10",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.3.0",
            "pytest-asyncio>=0.21.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
            "mypy>=1.3.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "yuyan-ai=main:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
