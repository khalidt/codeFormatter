from setuptools import setup, find_packages

setup(
    name="codeFormatter",  
    version="0.1",  
    packages=find_packages(),  
    description="A library for punctuation spacing normalization in Python code",
    author="Khalid Alkhaldi",  
    author_email="k.t.alkhaldi@gmail.com",  
    url="https://github.com/khalidt/codeFormatter",  
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPL v3 License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  
)
