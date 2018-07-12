"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

import codecs
import os
import re
import setuptools
from setuptools.command.test import test as TestCommand
from setuptools import Command

__author__ = "shawkins"
__email__ = "devs.mtgatracker@gmail.com"


PACKAGE_NAME = "mtga"
INSTALL_REQUIRES = []
DEPENDENCY_LINKS = []
TESTS_REQUIRE = []
LONG_DESCRIPTION = ''


def read_requirements_file(path):
    """
    reads requirements.txt file and handles PyPI index URLs
    :param path: (str) path to requirements.txt file
    :return: (tuple of lists)
    """
    last_pypi_url = None
    with open(path) as f:
        requires = []
        pypi_urls = []
        for line in f.readlines():
            if not line:
                continue
            if '--' in line:
                match = re.match(r'--index-url\s+([\w\d:/.-]+)\s', line)
                if match:
                    last_pypi_url = match.group(1)
                    if not last_pypi_url.endswith("/"):
                        last_pypi_url += "/"
            else:
                if last_pypi_url:
                    package = line.split("=")[0].split(">")[0].split("<")[0]
                    pypi_urls.append(last_pypi_url + package.strip().lower())
                requires.append(line)
    return requires, pypi_urls


if __name__ == "__main__":
    """
    BEGIN: DO NOT MODIFY
    The following lines allow for automatic versioning by Jenkins. Do not modify them!

    The third number in the version triple of all jenkins-managed modules will always be the jenkins build number.
    The first two numbers can be modified by changing the variable "major_version" of the "update_version.py" file.

    
    """
    VERSION_FILE = os.path.join("source", "mtga", "_version.py")
    __version__ = None
    # Check first for version in VERSION_FILE
    if os.path.isfile(VERSION_FILE):
        with open(VERSION_FILE) as f:
            lines = f.read()
        version_regex = "^__version__ = ['\"]([^'\"]*)['\"]"
        search_result = re.search(version_regex, lines, re.M)
        if search_result:
            __version__ = search_result.group(1)
        else:
            if os.environ.get('JENKINS_HOME'):
                raise RuntimeError("Unable to find version string in %s." % (VERSION_FILE,))
    else:
        # Check for version in 'major_version' file
        with open("major_version") as f:
            __version__ = f.read().strip() + '.0'
    assert __version__ is not None, "Version not found in _version.py nor major_version"
    """ END: DO NOT MODIFY """
    """ END: DO NOT MODIFY """

    _install_requires, _pypi_urls = read_requirements_file('requirements.txt')
    INSTALL_REQUIRES.extend(_install_requires)
    DEPENDENCY_LINKS.extend(_pypi_urls)

    if os.path.isfile('tests/requirements.txt'):
        _tests_require, _pypi_urls = read_requirements_file('tests/requirements.txt')
        TESTS_REQUIRE.extend(_tests_require)
        DEPENDENCY_LINKS.extend(_pypi_urls)

    # Get the long description from the relevant file
    if os.path.isfile('README.md'):
        with codecs.open('README.md', encoding='utf-8') as f:
            LONG_DESCRIPTION = f.read()
    
    setuptools.setup(
        name=PACKAGE_NAME,

        # Versions should comply with PEP440.  For a discussion on single-sourcing
        # the version across setup.py and the project code, see
        # https://packaging.python.org/en/latest/single_source_version.html
        version=__version__,

        description="python-mtga: a python-accessible interface for MTGA cards",
        long_description=LONG_DESCRIPTION,

        # The project's main homepage.
        url="https://github.com/mtgatracker/mtgatracker",

        # Author details
        author=__author__,
        author_email=__email__,

        # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
        classifiers=[
            # How mature is this project? Common values are
            #   1 - Planning
            #   3 - Alpha
            #   4 - Beta
            #   5 - Production/Stable
            'Development Status :: 3 - Alpha',

            # Indicate who your project is intended for
            'Intended Audience :: Testers',
            'Topic :: Software Development :: Testing',
            'Topic :: Software Development :: Quality Assurance',

            # Specify the Python versions you support here. In particular, ensure
            # that you indicate whether you support Python 2, Python 3 or both.
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.7',
            #'Programming Language :: Python :: 3',
            #'Programming Language :: Python :: 3.5',
        ],

        # What does your project relate to?
        keywords="pip artifactory installer",

        # You can just specify the packages manually here if your project is
        # simple. Or you can use find_packages().
        # In the case of this repo. We aren't installing anyting but the pre-requisites
        # But if you want any packages to be installed here, use the following example as a guide:
        # packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
        package_dir={'': 'source'},
        packages=["mtga", "mtga.models", "mtga.set_data"],

        # List any additional sources that should be included when searching for dependencies
        # https://pythonhosted.org/setuptools/setuptools.html#declaring-extras-optional-features-with-their-own-dependencies
        # Here is an example of how to do this:
        dependency_links=DEPENDENCY_LINKS,

        # List run-time dependencies here.  These will be installed by pip when
        # your project is installed. For an analysis of "install_requires" vs pip's
        # requirements files see:
        # https://packaging.python.org/en/latest/requirements.html
        install_requires=INSTALL_REQUIRES,
        tests_require=TESTS_REQUIRE,
        test_suite='tests',

        # List additional groups of dependencies here (e.g. development or test
        # dependencies). You can install these using the following syntax,
        # for example:
        # $ pip install -e .[dev,test]
        extras_require={
            'dev': INSTALL_REQUIRES,
            'test': TESTS_REQUIRE,
        },

        # If there are data files included in your packages that need to be
        # installed, specify them here.  If using Python 2.6 or less, then these
        # have to be included in MANIFEST.in as well.
        package_data={},

        # Although 'package_data' is the preferred approach, in some case you may
        # need to place data files outside of your packages. See:
        # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
        # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
        # data_files=[('my_data', ['data/data_file'])],

        # To provide executable scripts, use entry points in preference to the
        # "scripts" keyword. Entry points provide cross-platform support and allow
        # pip to create the appropriate form of executable for the target platform.
        entry_points={
            'console_scripts': [],
        },
    )
