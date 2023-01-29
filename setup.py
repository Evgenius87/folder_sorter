from setuptools import setup, find_namespace_packages

setup(
        name='folder_sorter',
        version='0.0.1',
        description='folder_sorter script for Python',
        url='',
        author='Yevhen Plotnikov',
        author_email='plotnikov.evgenij@ukr.net',
        include_package_data=True,
        packages=find_namespace_packages(),
        entry_points={'console_scripts': ['start=folder_sorter.sort_dir:main']}
)