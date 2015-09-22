#!/bin/bash
# Install prerequisites for ProvToolbox.

sudo apt-get -qq update
sudo apt-get -y install openjdk-7-jdk
java -version
javac -version
sudo apt-get -y install maven
mvn -v
sudo apt-get -y install graphviz
dot -V
sudo apt-get -y install libxml2-utils
xmllint --version
sudo apt-get -y install rpm
sudo apt-get -y install genisoimage
