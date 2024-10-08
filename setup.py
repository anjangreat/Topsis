from setuptools import setup, find_packages

setup(
    name='topsis-102218085-anjan',
    version='0.1',
    author='Anjan Gupta',
    author_email='guptaanjan046@gmail.com',
    description='A Python package for TOPSIS method',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'topsis-102218085-anjan = topsis_102218085_anjan.topsis:main'
        ],
    },
    install_requires=[
        'numpy',
        'pandas',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

