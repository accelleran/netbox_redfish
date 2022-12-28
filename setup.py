from setuptools import find_packages, setup

setup(
    name='netbox-redfish',
    version='0.1',
    description='Use netbox in combination with Redfish OOB interfaces',
    install_requires=[],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)