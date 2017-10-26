from setuptools import find_packages
from setuptools import setup


setup(
    include_package_data=True,
    name='tba_pre_commit_hooks',
    description='Some out-of-the-box hooks for pre-commit.',
    url='',
    version='1.1.1',

    author='Eike Schumann',
    author_email='eike.schumann@tba.group',

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],

    packages=find_packages(exclude=('tests*', 'testing*')),
    install_requires=[
        # quickfix to prevent pycodestyle conflicts
        'flake8!=2.5.3',
        'autopep8>=1.3',
        'pyyaml',
        'simplejson',
        'six',
    ],
    entry_points={
        'console_scripts': [
            'beautify_cpp = pre_commit_hooks.beautify_cpp:main',
        ],
    },
    data_files = [('', ['bin/AStyle.exe']),
                  ('',['bin/uncrustify.exe']),
                  ('',['bin/defaults.cfg'])
                 ],
)