import os
from setuptools.command.install import install
from setuptools.command.build_py import build_py
from setuptools import setup
from subprocess import call

base_path = os.path.dirname(os.path.abspath(__file__))
lib_path = os.path.join(base_path, "DescriptorLib")

class CustomInstall(install):
    """
    CustomInstall class
    """
    def run(self):
        install.run(self)

class CustomBuild(build_py):
    """
    CustomBuild class following the suggestion in:
    https://stackoverflow.com/questions/1754966/how-can-i-run-a-makefile-in-setup-py
    """
    def run(self):

        def compile_library():
            call("make", cwd=lib_path)
        self.execute(compile_library, [],  "Compiling shared library")
        build_py.run(self)

setup(
    name="DescriptorLib",
    version="0.1",
    description="Library for description of local atomic environments",
    packages=[
        "DescriptorLib",
        'DescriptorLib.test'
    ],
    package_dir={
        "DescriptorLib": "DescriptorLib",
        'DescriptorLib.test': 'DescriptorLib/test'
    },
    package_data={"DescriptorLib": ["libSymFunSet.so"]},
    include_package_data=True,
    cmdclass={"install": CustomInstall, "build_py": CustomBuild}
)
