import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-sagii',
    version='0.5',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',  # example license
    description='Sistema Aberto de Gestão Institucional Integrado.',
    long_description=README,
    url='https://www.sagii.com/',
    author='Jorge Vilaça',
    author_email='jorge.vilaca@gmail.com',
    install_requires = [
        "Django>=2.1",
        "django-localflavor>=2.1",
        # "cached-property==1.5.1", # TODO: Interessante, estudar uso!
        "pytz==2018.9",
        "PyYAML>=3.13",
        "sqlparse>=0.2.4",
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.1',  # replace "X.Y" as appropriate
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',  # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)