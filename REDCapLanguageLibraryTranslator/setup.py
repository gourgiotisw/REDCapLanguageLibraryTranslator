from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="REDCapLLT",
    version="2.0.0",
    author="William Gourgiotis",
    author_email="william.gourgiotis@umassmed.edu",
    description="A package to translate REDCap language libraries",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/REDCapLLT",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "googletrans==4.0.0-rc1",
    ],
    entry_points={
        'console_scripts': [
            'redcap_translate=redcapllt.translator:main',
        ],
    },
)
