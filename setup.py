from setuptools import setup, find_packages

setup(
    name="dnsinformer",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "dnspython",
        "requests",
        "python-whois"
    ],
    entry_points={
        "console_scripts": [
            "dnsinformer=dnsinformer.main:main",
        ],
    },
    author="Bakhtawar",  # Add your name here
    author_email="bakhtawarr080@gmail.com",  # Add your email here
    description="A tool to fetch DNS information for a given domain.",
    url="https://github.com/yourusername/dnsinformer",  # Add your project's URL here
    python_requires='>=3.6',
)
