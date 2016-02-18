"""
    PY-PROJ
    =======

    PY-PROJ - каркас пустого проекта на python.

"""
import re

from setuptools import find_packages, setup

install_requires = []

with open("py-proj/__init__.py", "r") as fd:
    version = re.search(r"^__version__\s*=\s*['\"]([^'\"]*)['\"]",
                        fd.read(), re.MULTILINE).group(1)

setup(
    name="py-proj",
    version=version,
    description="",
    long_description=__doc__,
    url="http://",
    license="EULA",
    author="Maryno.net",
    author_email="devel@maryno.net",
    packages=find_packages(exclude=("tests", "tests.*")),
    entry_points={
        "console_scripts": [
            "py-proj = py-proj.cli:cli",
        ]
    },
    zip_safe=False,
    install_requires=install_requires,
    include_package_data=True,
    classifiers=["Private :: Do Not Upload"],
)

