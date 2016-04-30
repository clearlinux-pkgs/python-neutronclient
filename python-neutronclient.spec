#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-neutronclient
Version  : 4.2.0
Release  : 24
URL      : http://tarballs.openstack.org/python-neutronclient/python-neutronclient-4.2.0.tar.gz
Source0  : http://tarballs.openstack.org/python-neutronclient/python-neutronclient-4.2.0.tar.gz
Summary  : CLI and Client Library for OpenStack Networking
Group    : Development/Tools
License  : Apache-2.0
Requires: python-neutronclient-bin
Requires: python-neutronclient-python
BuildRequires : Babel-python
BuildRequires : Jinja2
BuildRequires : Sphinx-python
BuildRequires : cliff-python
BuildRequires : cmd2-python
BuildRequires : coverage-python
BuildRequires : discover-python
BuildRequires : docutils-python
BuildRequires : extras
BuildRequires : extras-python
BuildRequires : hacking
BuildRequires : jsonschema-python
BuildRequires : keystoneauth1-python
BuildRequires : msgpack-python-python
BuildRequires : os-client-config-python
BuildRequires : os-testr-python
BuildRequires : oslo.log-python
BuildRequires : oslo.serialization-python
BuildRequires : oslo.utils-python
BuildRequires : oslosphinx-python
BuildRequires : oslotest-python
BuildRequires : paramiko-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : positional-python
BuildRequires : prettytable
BuildRequires : py-python
BuildRequires : pyparsing-python
BuildRequires : pyrsistent-python
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python-mimeparse-python
BuildRequires : python-mock-python
BuildRequires : python3-dev
BuildRequires : reno-python
BuildRequires : requests-mock-python
BuildRequires : requests-python
BuildRequires : setuptools
BuildRequires : simplejson
BuildRequires : six
BuildRequires : six-python
BuildRequires : tempest-lib-python
BuildRequires : testrepository-python
BuildRequires : testscenarios
BuildRequires : testtools
BuildRequires : testtools-python
BuildRequires : tox
BuildRequires : traceback2-python
BuildRequires : unittest2-python
BuildRequires : virtualenv

%description
Python bindings to the Neutron API
==================================
This is a client library for Neutron built on the Neutron API. It
provides a Python API (the ``neutronclient`` module) and a command-line tool
(``neutron``).

%package bin
Summary: bin components for the python-neutronclient package.
Group: Binaries

%description bin
bin components for the python-neutronclient package.


%package python
Summary: python components for the python-neutronclient package.
Group: Default
Requires: Babel-python
Requires: cliff-python
Requires: keystoneauth1-python
Requires: os-client-config-python
Requires: oslo.serialization-python
Requires: oslo.utils-python
Requires: requests-python
Requires: simplejson
Requires: six-python

%description python
python components for the python-neutronclient package.


%prep
cd ..
%setup -q -n python-neutronclient-4.2.0

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/neutron

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
