from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
    requirements_list : List[str] = []
    return requirements_list

setup(
    name = "Xray",
    version = "0.0.1",
    author = "awais",
    author_email = "awaisraza0731@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements(),
)