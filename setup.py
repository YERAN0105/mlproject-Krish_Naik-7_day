from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ." #if this is in the requirements.txt file, it will connect that file direcly with the setup.py
def get_requirements(file_path:str)->list[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        [req.replace("\n","") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name='mlproject-Krish_Naik-7_day',
    version='0.0.1',
    author='Yeran',
    author_email='yeranfernando2002@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)