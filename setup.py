import setuptools


with open('README.md', 'r') as fh:
    long_description = fh.read()


setuptools.setup(
    name='degas',
    version='0.1.0',
    author='Piotr Rarus',
    author_email='p.rarus@micro-solutions.pl',
    description='Chaining CV methods, logs intermediary results.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='http://msol-git:3000/ai-tools/degas',
    packages=setuptools.find_packages(
        exclude=[
            "tests",
            "examples"
        ]
    ),
    install_requires=[
        'numpy'
    ],
    tests_require=[
        'austen',
        'scikit-image',
        'pytest'
    ]

)
