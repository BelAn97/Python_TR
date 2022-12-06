from setuptools import setup, find_packages

setup(
    name='HTML-Tags-Counter',
    version='1.0',
    description='Программа для подсчета количества html-тэгов на странице.',
    author='Andrei Belousov',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    package_data={'tags_counter': ['*.yaml']},
    include_package_data=True,
    entry_points={'console_scripts': [
        'tagcounter = tags_counter.main:run']},
    install_requires=['requests', 'tldextract', 'pyyaml'],
)
