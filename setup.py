"""
    py_proj
    =======

    py_proj - каркас пустого Flask-приложения на python.

"""

import re

from setuptools import find_packages, setup

install_requires = [
    'gunicorn==19.9.0',
    'Flask==1.0.2',
    'Werkzeug==0.15.1',
    'click==7.0'
]

dev_install_requires = [
    'yapf==0.26.0',
    'isort==4.3.16',
]

test_install_requires = [
    'pytest==4.3.1',
    'pytest-flask==0.14.0',
    'pytest-cov==2.6.1',
    'flake8==3.7.7',
    'flake8-debugger==3.1.0',
    'flake8-isort==2.7.0',
    'flake8-print==3.1.0',
    'flake8-quotes==1.0.0',
]

with open('py_proj/__init__.py', 'r') as fd:
    version = re.search(r"^__version__\s*=\s*['\"]([^'\"]*)['\"]",
                        fd.read(), re.MULTILINE).group(1)

setup(
    name='py_proj',
    version=version,
    description='',
    long_description=__doc__,
    url='http://',
    license='MIT',
    author="ООО \"Экстрим\"",
    author_email='devel@maryno.net',
    packages=find_packages(exclude=('tests', 'tests.*')),
    entry_points={
        'console_scripts': [
            'py_proj = py_proj.cli:cli',
        ]
    },
    zip_safe=False,
    install_requires=install_requires,
    extras_require={
        'dev': dev_install_requires,
        'test': test_install_requires,
    },
    include_package_data=True,
    classifiers=['Private :: Do Not Upload'],
)
