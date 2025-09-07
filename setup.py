from setuptools import find_packages,setup

setup(name="agentic-RAG-trading-system",
       version="0.0.1",
       author="suman",
       author_email="svemula52@gmail.com",
       packages=find_packages(),
       install_requires=['lancedb','langchain','langgraph','tavily-python','polygon']
       )