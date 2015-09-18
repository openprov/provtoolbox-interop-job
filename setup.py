#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

requirements = [
    'prov_interop',
]

test_requirements = [
]

setup(
    name='prov_interop_provtoolbox',
    version='0.0.1',
    description='Provenance Tool Suite interoperability test harness ProvToolbox extension',
    author='Mike Jackson',
    author_email='michaelj@epcc.ed.ac.uk',
    url='https://github.com/prov-suite/provtoolbox-interop-job',
    packages=find_packages(),
    package_dir={
        'prov_interop_provtoolbox': 'prov_interop_provtoolbox'
    },
    include_package_data=True,
    install_requires=requirements,
    license="Apache Software License",
    zip_safe=False,
    keywords=[
        'provenance', 'graph', 'model', 'PROV', 'PROV-DM', 'PROV-JSON', 'JSON',
        'PROV-XML', 'PROV-N'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        "Programming Language :: Python :: 3",
        'Programming Language :: Python :: 3.4',
        'Topic :: Scientific/Engineering :: Information Analysis',
    ],
    test_suite='prov_interop_provtoolbox.tests',
    tests_require=test_requirements
)
