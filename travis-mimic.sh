#!/bin/bash
# Shell script that mimics .travis.yml actions

TRAVIS_BUILD_DIR=`pwd`

echo "Getting test cases..."
git clone https://github.com/mikej888/provtoolsuite-testcases testcases
echo "Installing ProvToolbox dependencies..."
# sudo apt-get -qq update > /dev/null
# sudo apt-get -qq install graphviz > /dev/null
# sudo apt-get -qq install rpm > /dev/null
# sudo apt-get -y install libxml2-utils
# sudo apt-get -y install graphviz
echo "Getting ProvToolbox..."
git clone https://github.com/lucmoreau/ProvToolbox.git ProvToolbox
cd ProvToolbox
mvn clean install
./toolbox/target/appassembler/bin/provconvert -version
cd ..
echo "Installing ProvPy dependencies..."
# sudo apt-get -y install zlib1g-dev
# sudo apt-get -y install libxslt1-dev
echo "Getting ProvPy..."
git clone https://github.com/trungdong/prov ProvPy
cd ProvPy
git checkout 1.3.2
python setup.py install
./scripts/prov-convert --version
cd ..
git clone https://github.com/mikej888/provtoolsuite-interop-test-harness test-harness
cd test-harness
pip install -r requirements.txt
echo "Creating local configuration files..."
echo "PROV_TEST_CASES_DIR=$TRAVIS_BUILD_DIR/testcases" > config.properties
echo "PROVPY_SCRIPTS_DIR=$TRAVIS_BUILD_DIR/ProvPy/scripts" >> config.properties
echo "PROVTOOLBOX_SCRIPTS_DIR=$TRAVIS_BUILD_DIR/ProvToolbox/toolbox/target/appassembler/bin" >> config.properties
echo "PROV_LOCAL_CONFIG_DIR=$TRAVIS_BUILD_DIR/test-harness/localconfig" >> config.properties
cat config.properties
mkdir localconfig
python prov_interop/customise-config.py config localconfig config.properties
echo "Test configuration..."
cat localconfig/*

nosetests -v prov_interop.interop_tests.test_provtoolbox
