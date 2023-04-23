from setuptools import setup, find_packages

setup(name='address_separator',
      version='1.0',
      description='Address parser',
      author='Ehsan Maiqani',
      author_email='ehsan.maiqani@gmail.com.com',
      packages=find_packages(),
      install_requires=[
          "numpy==1.24.2",
          "pandas==2.0.0",
          "python-dateutil==2.8.2",
          "pytz==2023.3",
          "six==1.16.0",
          "tzdata==2023.3"
      ],
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
      ])
