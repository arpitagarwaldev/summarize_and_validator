from setuptools import setup, find_packages

setup(
    name="ai-agent-practice",
    version="0.1.0",
    description="A Python-based AI agent system for NLP tasks",
    author="Arpit Agarwal",
    author_email="arpit.dev@outlook.com",
    packages=find_packages(),
    install_requires=[
        "streamlit==1.30.1",
        "ollama==0.1.22",
        "loguru==0.7.2",
        "python-dotenv==1.0.0",
        "watchdog==3.0.0"
    ],
    entry_points={
        'console_scripts': [
            'ai-agent=app:main',
        ],
    },
    python_requires='>=3.8',
)
