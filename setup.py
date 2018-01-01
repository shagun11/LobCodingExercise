from setuptools import setup, find_packages
setup(
    name="lob_assignment",
    version="0.0.1",
    packages=find_packages('.'),
    package_dir={'': '.'},
    install_requires=[
        'requests',
        'lob'
    ],)