"""Unit tests for :mod:`prov_interop.provtoolbox.converter`.

These tests rely on the
:mod:`prov_interop.tests.provtoolbox.provconvert_dummy.py` script,
(that mimics ProvToolbox's ``provconvert`` executable 
in terms of parameters and return codes) being available 
in the same directory as this module.
"""
# Copyright (c) 2015 University of Southampton
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions: 
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software. 
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
# BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.  

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import inspect
import os
import tempfile
import unittest

from prov_interop import standards
from prov_interop.component import ConfigError
from prov_interop.converter import ConversionError
from prov_interop.provtoolbox.converter import ProvToolboxConverter

class ProvToolboxConverterTestCase(unittest.TestCase):

  def setUp(self):
    super(ProvToolboxConverterTestCase, self).setUp()
    self.provtoolbox = ProvToolboxConverter()
    self.in_file = None
    self.out_file = None
    self.config = {}  
    self.config[ProvToolboxConverter.EXECUTABLE] = "python"
    script = os.path.join(
      os.path.dirname(os.path.abspath(inspect.getfile(
            inspect.currentframe()))), "provconvert_dummy.py")
    self.config[ProvToolboxConverter.ARGUMENTS] = " ".join(
      [script,
       "-infile", ProvToolboxConverter.INPUT,
       "-outfile", ProvToolboxConverter.OUTPUT])
    self.config[ProvToolboxConverter.INPUT_FORMATS] = standards.FORMATS
    self.config[ProvToolboxConverter.OUTPUT_FORMATS] = standards.FORMATS

  def tearDown(self):
    super(ProvToolboxConverterTestCase, self).tearDown()
    for tmp in [self.in_file, self.out_file]:
      if tmp != None and os.path.isfile(tmp):
        os.remove(tmp)

  def test_init(self):
    self.assertEqual("", self.provtoolbox.executable)
    self.assertEqual([], self.provtoolbox.arguments)
    self.assertEqual([], self.provtoolbox.input_formats)
    self.assertEqual([], self.provtoolbox.output_formats)

  def test_configure(self):
    self.provtoolbox.configure(self.config)
    self.assertEqual(self.config[ProvToolboxConverter.EXECUTABLE].split(), 
                     self.provtoolbox.executable)
    self.assertEqual(self.config[ProvToolboxConverter.ARGUMENTS].split(), 
                     self.provtoolbox.arguments)
    self.assertEqual(self.config[ProvToolboxConverter.INPUT_FORMATS], 
                     self.provtoolbox.input_formats)
    self.assertEqual(self.config[ProvToolboxConverter.OUTPUT_FORMATS], 
                     self.provtoolbox.output_formats)

  def test_configure_no_input(self):
    self.config[ProvToolboxConverter.ARGUMENTS] = \
        "provconvert_dummy.py -outfile " + ProvToolboxConverter.OUTPUT
    with self.assertRaises(ConfigError):
      self.provtoolbox.configure(self.config)

  def test_configure_no_output(self):
    self.config[ProvToolboxConverter.ARGUMENTS] = \
        "provconvert_dummy.py -infile " + ProvToolboxConverter.INPUT 
    with self.assertRaises(ConfigError):
      self.provtoolbox.configure(self.config)

  def test_convert(self):
    self.provtoolbox.configure(self.config)
    (_, self.in_file) = tempfile.mkstemp(suffix="." + standards.JSON)
    self.out_file = "convert." + standards.PROVX
    self.provtoolbox.convert(self.in_file, self.out_file)

  def test_convert_oserror(self):
    self.config[ProvToolboxConverter.EXECUTABLE] = "/nosuchexecutable"
    self.provtoolbox.configure(self.config)
    (_, self.in_file) = tempfile.mkstemp(suffix="." + standards.JSON)
    self.out_file = "convert_oserror." + standards.PROVX
    with self.assertRaises(OSError):
      self.provtoolbox.convert(self.in_file, self.out_file)

  def test_convert_missing_input_file(self):
    self.provtoolbox.configure(self.config)
    self.in_file = "nosuchfile.provx." + standards.PROVX
    self.out_file = "convert_missing_input_file." + standards.PROVX
    with self.assertRaises(ConversionError):
      self.provtoolbox.convert(self.in_file, self.out_file)

  def test_convert_invalid_input_format(self):
    self.provtoolbox.configure(self.config)
    (_, self.in_file) = tempfile.mkstemp(suffix=".nosuchformat")
    self.out_file = "convert_invalid_input_format." + standards.PROVX
    with self.assertRaises(ConversionError):
      self.provtoolbox.convert(self.in_file, self.out_file)

  def test_convert_invalid_output_format(self):
    self.provtoolbox.configure(self.config)
    (_, self.in_file) = tempfile.mkstemp(suffix="." + standards.JSON)
    self.out_file = "convert_invalid_input_format.nosuchformat"
    with self.assertRaises(ConversionError):
      self.provtoolbox.convert(self.in_file, self.out_file)
