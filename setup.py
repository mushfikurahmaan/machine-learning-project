from setuptools import find_packages, setup  # type: ignore
from typing import List


IGNORE = "-e ."

def get_requirements(file_path:str) -> List[str]:    #This function will return the list of requirements
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if IGNORE in requirements:
            requirements.remove(IGNORE)

    return requirements

    

setup(
    name="machine-learning-project",
    version="0.0.1",
    author="Mushfikur R. Mahi",
    author_email="mushfikurahmaan@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)
