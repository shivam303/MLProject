from setuptools import find_packages,setup

from typing import List

HYPHEN = '-e .'

def get_requirements(file_path:str)-> List[str]:
    '''
    This finction will return the list of requiremets 
    '''

    requirements = []

    with open(file_path) as file_obj:
        file_obj.readline()
        requirements = [req.replace("\n","") for req in requirements] ## relpacing "\n" witn ""
    
    if HYPHEN in requirements:
        requirements.remove(HYPHEN)

    return requirements



setup(
    name='MLProject',
    version = '0.0.1',
    author= 'Shivam',
    author_email='shivamsachan303@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt'),  ## Whatever libraries are needed to be installed for this to be used as package

)
