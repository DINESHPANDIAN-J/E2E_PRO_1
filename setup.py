from setuptools import find_packages, setup
from typing import List

hypen_e_dot = '_e .'
def get_requirements(file_path: str) -> List[str]:
    '''this function will return a list of requirements'''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [requirement.replace("\n","") for requirement in requirements]

        if '_e .' in requirements:
            requirements.remove(hypen_e_dot)

    return requirements


setup(
    name="ml-project",
    version="0.0.1",
    author="dinesh",
    author_email="datadinesh1@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),  # Use the filename as a string
)
