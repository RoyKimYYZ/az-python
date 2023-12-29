from setuptools import setup

setup(
    name='create_azstorage',
    version='0.1.0',
    py_modules=['create_azstorage_cli'],
    install_requires=[
        'Click',
        'azure-mgmt-resource',
        'azure-identity',
        'azure-mgmt-storage',
        'azure-storage-blob',
    ],
    entry_points={
        'console_scripts': [
            'create_azstorage_cli = create_azstorage_cli:create_az_storage',
        ],
    },
)