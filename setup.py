from setup import setup, find_packages

setup(
    name='mypackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='This is an example of python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/NjengaBen64',
    author='<Benson Kamau>',
    author_email='<njengaben64@gmail.com>'
)