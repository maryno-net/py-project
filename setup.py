"""
    PY-PROJ
    =======

    PY-PROJ - каркас пустого проекта на python.

"""

import re

from setuptools import find_packages, setup

install_requires = [
    "gunicorn==19.9.0",
    "Flask==1.0.2",
    "click==7.0"
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
    license="MIT",
    author="ООО \"Экстрим\"",
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
