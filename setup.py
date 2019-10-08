import setuptools


with open('README.md', 'r') as fh:
    long_description = fh.read()


setuptools.setup(
    name='degas',
    description='Fluent interface for numpy arrays.',

    author='Piotr Rarus',
    author_email='piotr.rarus@gmail.com',

    url='https://github.com/piotr-rarus/degas',
    license='MIT',
    version='0.1.3',

    long_description=long_description,
    long_description_content_type='text/markdown',

    packages=setuptools.find_packages(
        exclude=[
            'test',
        ]
    ),
    install_requires=[
        'numpy',
        'austen',
        'scikit-image',
    ],
    tests_require=[
        'pytest',
        'pytest-cov',
        'flake8',
        'pylint',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
)
