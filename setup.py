import setuptools


with open('README.md', 'r') as fh:
    long_description = fh.read()


setuptools.setup(
    name='degas',
    version='0.1.0',
    author='Piotr Rarus',
    author_email='piotr.rarus@gmail.com',
    description='Fluent interface for numpy arrays.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='http://msol-git:3000/ai-tools/degas',
    packages=setuptools.find_packages(
        exclude=[
            'test',
            'data',
            'example'
        ]
    ),
    install_requires=[
        'numpy',
        'scikit-image',
        'austen'
    ],
    tests_require=[
        'pytest',
        'pytest-cov',
        'flake8',
        'pylint'
    ]

)
