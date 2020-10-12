import setuptools

with open("readme.md","r", encoding='utf8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='com_sba_api',
    version='1.0',
    description='Python Distribution Utilities',
    author='jongmokchung',
    long_description = long_description,
    author_email='jongmok1031@gmail.com',
    url='https://www.python.org/sigs/distutils-sig/',
    packages=setuptools.find_packages(),
    )