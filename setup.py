from setuptools import setup

setup(
    name='createazstorage',
    version='0.1.0',
    py_modules=['create-storage-cli'],
    install_requires=[
        'Click',
        'azure-mgmt-resource',
        'azure-identity',
        'azure-mgmt-storage',
        'azure-storage-blob',
    ],
    entry_points={
        'console_scripts': [
            'create-storage-cli = create-storage-cli:create_az_storage',
        ],
    },
)