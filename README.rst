Southampton Provenance Tool Suite ProvToolbox Interoperability Tests
====================================================================

`ProvToolbox <https://github.com/lucmoreau/ProvToolbox>`_ interoperability test job.

.. image:: https://travis-ci.org/mikej888/provtoolsuite-provtoolbox-interop-job.svg
  :target: https://travis-ci.org/mikej888/provtoolsuite-provtoolbox-interop-job
  :alt: TravisCI Build Status

The test job:

* Gets ProvToolbox from GitHub (stable master branch).
* Gets ProvPy via 'pip' (most recent release).
* Gets canonical `test cases <https://github.com/mikej888/provtoolsuite-testcases>`_ from GitHub (stable master branch).
* Gets `interoperability test harness <https://github.com/mikej888/provtoolsuite-interop-test-harness>`_ from GitHub (stable master branch).
* Configures interoperability test harness.
* Runs interoperability tests to validate ProvToolbox conversions done using provconvert. Conversions are validated using ProvPy's prov-compare script.

Author
------

Developed by `The Software Sustainability Institute <http://www.software.ac.uk>`_ and the `Provenance Tool Suite <http://provenance.ecs.soton.ac.uk/>`_ team at `Electronics and Computer Science <http://www.ecs.soton.ac.uk>`_ at the `University of Southampton <http://www.soton.ac.uk>`_.

For more information, see our `document repository <https://github.com/prov-suite/ssi-consultancy/>`_.

License
-------

These tests are released under the MIT license.
