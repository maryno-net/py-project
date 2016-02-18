"""
    PY-PROJ
    =======

    PY-PROJ - каркас пустого проекта на python.

"""

import re

from setuptools import find_packages, setup

install_requires = [
    "gunicorn==19.3.0",
    "aiohttp==0.17.3",
    "Flask==0.10.1",
    "click==6.2"
]

with open("py_proj/__init__.py", "r") as fd:
    version = re.search(r"^__version__\s*=\s*['\"]([^'\"]*)['\"]",
                        fd.read(), re.MULTILINE).group(1)

setup(
    name="py_proj",
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
            "py_proj = py_proj.cli:cli",
        ]
    },
    zip_safe=False,
    install_requires=install_requires,
    include_package_data=True,
    classifiers=["Private :: Do Not Upload"],
)
