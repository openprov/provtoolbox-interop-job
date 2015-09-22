# Interoperability Test Harness ProvToolbox Extension

[Southampton Provenance Tool Suite](https://provenance.ecs.soton.ac.uk) interoperability test harness ProvToolbox extension. This package consists of classes that extend the [interoperability test harness framework](https://github.com/prov-suite/interop-test-harness/tree/package) to allow interoperability testing of [ProvToolbox](https://github.com/lucmoreau/ProvToolbox).

The test harness runs under Python 2.7+ and Python 3.

[![Build Status](https://travis-ci.org/prov-suite/provtoolbox-interop-job.svg)](https://travis-ci.org/prov-suite/provtoolbox-interop-job)

---

## Installation

The instructions have been written with reference to the 64-bit [Ubuntu](http://www.ubuntu.com/) 14.04.2 operating system.

Other operating systems, or versions of these, may differ in how packages are istalled, the versions of these packages available from package managers etc. Consult the relevant documentation for your operating system and the products concerned.

Some dependencies require you to have sudo access to install and configure software (or a local system administrator can do this for you).

This page assumes that [pyenv](https://github.com/yyuu/pyenv) is used to manage Python versions.

Install the interoperability test harness framework

* See [interoperability test harness framework](https://github.com/prov-suite/interop-test-harness/blob/package/README.md)

Install dependencies

* The dependencies required by ProvToolbox must be installed. 
* `ubuntu-dependencies.sh` is a simple shell script which both installs these dependencies.
* To run the script:

```
$ git clone https://github.com/prov-suite/provtoolbox-interop-job
$ cd provtooblox-interop-job
$ git checkout package
$ source ubuntu-dependencies.sh 
```

Install package

```
$ python setup.py install
```

Run unit tests

```
$ nosetests prov_interop_provtoolbox.tests
```

---

## Running ProvToolbox interoperability tests

Get and install the latest version of ProvToolbox

```
$ git clone -b development https://github.com/lucmoreau/ProvToolbox.git ProvToolbox
$ cd ProvToolbox
$ mvn clean install -DskipTests
$ export PATH=$PATH:$PWD/toolbox/target/appassembler/bin
$ provconvert -version
$ cd ..
```

Get the interoperability test cases

```
$ git clone https://github.com/prov-suite/testcases
```

Run interoperability tests:

```
$ nosetests -v prov_interop_provtoolbox.interop_tests
```

If you are running on a multi-processor machine then the tests can run in parallel, using nosetests' support for [parallel testing](http://nose.readthedocs.org/en/latest/doc_tests/test_multiprocess/multiprocess.html). Specify the number of processes you want to use using a `--processes` flag e.g.

```
$ nosetests --processes=4 -v prov_interop_provtoolbox.interop_tests
```

---

## Running ProvToolbox interoperability tests under Travis CI

[.travis.yml](./.travis.yml) provides an example Travis CI configuration file

---

## API documentation

To create API documentation in `apidocs/_build/html`:

```
$ pip install sphinx
$ make apidocs
```

---

## Author

Developed by [The Software Sustainability Institute](http://www.software.ac.uk>) and the [Provenance Tool Suite](http://provenance.ecs.soton.ac.uk/) team at [Electronics and Computer Science](http://www.ecs.soton.ac.uk) at the [University of Southampton](http://www.soton.ac.uk).

For more information, see our [document repository](https://github.com/prov-suite/ssi-consultancy/).

---

## License

The code is released under the MIT license.
