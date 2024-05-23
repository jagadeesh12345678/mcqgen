from setuptools import setup,find_packages

setup(
    name="mcqgenerator",
    version="0.0.1",
    author="jagadeesh12345678",
    author_email="jagadeeshreddyk9@gmail.com",
    install_requires=["openai","langchain","streamlit","pyPDF2"],
    packages=find_packages()
)