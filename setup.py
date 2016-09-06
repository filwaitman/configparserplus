from setuptools import setup

VERSION = '0.0.4'


setup(
    name='configparserplus',
    packages=['configparserplus', ],
    version=VERSION,
    author='Filipe Waitman',
    author_email='filwaitman@gmail.com',
    install_requires=[x.strip() for x in open('requirements.txt').readlines()],
    url='https://github.com/filwaitman/configparserplus',
    download_url='https://github.com/filwaitman/configparserplus/tarball/{}'.format(VERSION),
    test_suite='tests',
    keywords=['ConfigParser', 'Jinja', 'INI'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Operating System :: OS Independent",
    ],
)
