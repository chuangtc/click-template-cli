from setuptools import setup, find_packages

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='click_app',
    version='0.1.2',
    author='Jason Chuang',
    author_email='chuangtcee@gmail.com',
    description='A template of Click application CLI',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/chuangtc/click-template-cli',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
    install_requires=[
        'click>=8.0.0',
    ],
    entry_points={
        'console_scripts': [
            'click_app = click_template_cli.cli:main',
        ],
    },
    # This line enables editable installs
    # With 'pip install -e .' equivalent
    # to install your package in editable mode
    # so changes in your source code are immediately reflected
    # without needing to reinstall
    options={'bdist_wheel': {'universal': True}},
    setup_requires=['setuptools>=51.0.0', 'wheel'],
    editable=True
)
