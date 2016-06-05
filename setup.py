from setuptools import setup, find_packages

version = '1.1.0'


setup(
    name = 'hexs',
    version = version,
    description = 'Hex string formatting.',
    url = 'https://github.com/kefkius/hexs',
    author = 'Tyler Willis',
    author_email = 'kefkius@mail.com',
    keywords = [
        'hex',
        'formatting',
    ],
    classifiers = [
        'License :: OSI Approved :: MIT License',
    ],
    packages = find_packages(),
    test_suite = 'hexs.tests'
)
