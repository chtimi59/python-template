from glob import glob
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import splitext

from setuptools import find_packages
from setuptools import setup


setup(
    name='mystuff',
    version='1.0.0',
    license='BSD',
    description='some description',
    author='you',
    url='https://github.com/',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # eg: 'aspectlib==1.1.1', 'six>=1.7',
        'camelcase'
    ],
    extras_require={
        # eg:
        #   'rst': ['docutils>=0.11'],
        #   ':python_version=="2.6"': ['argparse'],
    },
    setup_requires=[
        # eg: 'pytest-runner',
    ],
    entry_points={
        'console_scripts': [
            # or 'mystuff = mystuff.mypackage:foo',
            'mystuff = mystuff:main',
        ]
    },
)
