from setuptools import setup, find_packages

setup(name="din",
      version="0.1.0",
      packages=find_packages(exclude=["tests"]),
      include_package_data=True,
      entry_points={
            "console_scripts": [
                  "din = din:main"
            ]
      })
