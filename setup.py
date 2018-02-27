# coding=utf-8
"""
EMFT setup file
"""

from setuptools import find_packages, setup

CLASSIFIERS = filter(None, map(str.strip,
                               """
Development Status :: 1 - Planning
Environment :: Console
Environment :: Win32 (MS Windows)
Intended Audience :: End Users/Desktop
License :: OSI Approved :: MIT License
Natural Language :: English
Operating System :: Microsoft :: Windows
Operating System :: Microsoft :: Windows :: Windows 7
Operating System :: Microsoft :: Windows :: Windows 8
Operating System :: Microsoft :: Windows :: Windows 8.1
Operating System :: Microsoft :: Windows :: Windows 10
Programming Language :: Python
Programming Language :: Python :: 3.6
Programming Language :: Python :: 3.7
Programming Language :: Python :: 3 :: Only
Programming Language :: Python :: Implementation :: CPython
Topic :: Desktop Environment :: File Managers
Topic :: Games/Entertainment :: Simulation
Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Content Management System
Topic :: Utilities
""".splitlines()))

entry_points = '''
[console_scripts]
hello=pvnhxgmgiq.__main__:main
'''

setup(
    name='pvnhxgmgiq',
    package_dir={'pvnhxgmgiq': 'pvnhxgmgiq'},
    use_scm_version=True,
    install_requires=['elib'],
    tests_require=[],
    entry_points=entry_points,
    setup_requires=['setuptools_scm'],
    test_suite='pytest',
    packages=find_packages(),
    python_requires='>=3.6',
    license='MIT',
    classifiers=CLASSIFIERS,
)
