import sys

from os.path import abspath, dirname, join
from setuptools import setup, find_packages
from readability import __version__


CURRENT_DIRECTORY = abspath(dirname(__file__))


with open(join(CURRENT_DIRECTORY, "README.rst")) as readme:
    with open(join(CURRENT_DIRECTORY, "CHANGELOG.rst")) as changelog:
        long_description = "%s\n\n%s" % (readme.read(), changelog.read())


install_requires = [
    "docopt>=0.6.1,<0.7",
    "charade",
    "lxml>=2.0",
]
tests_require = [
    "coverage",
    "nose",
]


if sys.version_info < (2, 7):
    install_requires.append("unittest2")


setup(
    name="readability",
    version=__version__,
    description="Port of Readability HTML parser in Python",
    long_description=long_description,
    keywords=[
        "readability",
        "readable",
        "parsing",
        "HTML",
        "content",
    ],
    author="Michal Belica",
    author_email="miso.belica@gmail.com",
    url="https://github.com/miso-belica/readability.py",
    license="BSD",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Pre-processors",
        "Topic :: Text Processing :: Filters",
        "Topic :: Text Processing :: Markup :: HTML",

    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    tests_require=tests_require,
    test_suite="tests.run_tests.run",
    entry_points={
        "console_scripts": [
            "readability=readability.scripts.client:main",
            "readability_test=readability.scripts.test_helper:main",
        ]
    }
)
