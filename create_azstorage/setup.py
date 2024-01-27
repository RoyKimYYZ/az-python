from setuptools import setup

# configuration for the distribution of this Python package
setup(
    name='create_azstorage', # name of the package
    version='0.1.0', # version of the package
    py_modules=['create_azstorage_cli'], # modules to include
    install_requires=[ # package dependencies
        'Click',
        'azure-mgmt-resource',
        'azure-identity',
        'azure-mgmt-storage',
        'azure-storage-blob',
    ],
    entry_points={
        'console_scripts': [ # command line interface (CLI) entry points
            'create_azstorage_cli = create_azstorage_cli:create_az_storage', # command = module:function
        ],
    },
)