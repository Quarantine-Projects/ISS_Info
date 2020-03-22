from setuptools import find_packages, setup

# read the contents of your README file
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
  name = 'ISS_Info',
  packages = find_packages(include=["ISS_Info"]),
  version = '1.0.0',
  license='MIT',
  description = 'Python wrapper for tracking information about International Space Station via http://open-notify.org/',
  long_description=long_description,
  long_description_content_type="text/markdown",
  author = 'Salil Gautam & Prakhar Dixit',
  url = 'https://github.com/Quarantine-Projects/ISS_Info',
  keywords = ['ISS', 'Space', 'Station','API'],
  install_requires=["requests>=2.23.0"],
  classifiers=[
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Operating System :: OS Independent',
  ],
  python_requires='>=3, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*'
)
