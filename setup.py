from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in server_app/__init__.py
from server_app import __version__ as version

setup(
	name="server_app",
	version=version,
	description="Server Side scripting",
	author="Sunil ",
	author_email="sunilbhave36@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
