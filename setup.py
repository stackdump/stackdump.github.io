from setuptools import setup, find_packages

DESC = "A blog about blockchains and state machines."

setup(
    name="blahchain",
    version="0.1",
    author="Matthew York",
    author_email="myork@stackdump.com",
    description=DESC,
    license='',
    keywords='blog',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Sphinx>=1.6.5',
        'recommonmark>=0.4.0',
        'sphinx-bootstrap-theme>=0.6.0',
        'sphinxcontrib-googleanalytics>=0.1'
    ],
    long_description=DESC,
    url="www.blahchain.com",
    classifiers=[],
)
