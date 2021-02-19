from setuptools import setup, find_packages

setup(
    name='hash_code',
    version='1.0.0',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    zip_safe=False,
    python_requires='>=3.8.*',
    install_requires=[
    ],
    tests_require=[
        "pytest==6.2.2",
    ],
    include_package_data=True
)
