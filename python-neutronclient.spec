#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xD9631FEAF0CC6227 (infra-root@openstack.org)
#
Name     : python-neutronclient
Version  : 6.0.0
Release  : 31
URL      : http://tarballs.openstack.org/python-neutronclient/python-neutronclient-6.0.0.tar.gz
Source0  : http://tarballs.openstack.org/python-neutronclient/python-neutronclient-6.0.0.tar.gz
Source99 : http://tarballs.openstack.org/python-neutronclient/python-neutronclient-6.0.0.tar.gz.asc
Summary  : CLI and Client Library for OpenStack Networking
Group    : Development/Tools
License  : Apache-2.0
Requires: python-neutronclient-bin
Requires: python-neutronclient-python
Requires: Babel
Requires: cliff
Requires: debtcollector
Requires: iso8601
Requires: keystoneauth1
Requires: netaddr
Requires: os-client-config
Requires: osc-lib
Requires: oslo.i18n
Requires: oslo.serialization
Requires: oslo.utils
Requires: pbr
Requires: requests
Requires: simplejson
Requires: six
BuildRequires : Babel-python
BuildRequires : Sphinx-python
BuildRequires : cliff-python
BuildRequires : cmd2-python
BuildRequires : configparser-python
BuildRequires : coverage-python
BuildRequires : discover-python
BuildRequires : extras
BuildRequires : extras-python
BuildRequires : hacking
BuildRequires : jsonschema-python
BuildRequires : keystoneauth1-python
BuildRequires : msgpack-python-python
BuildRequires : os-client-config-python
BuildRequires : os-testr-python
BuildRequires : osc-lib
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
.. image:: https://img.shields.io/pypi/v/python-neutronclient.svg
:target: https://pypi.python.org/pypi/python-neutronclient/
:alt: Latest Version

%package bin
Summary: bin components for the python-neutronclient package.
Group: Binaries

%description bin
bin components for the python-neutronclient package.


%package python
Summary: python components for the python-neutronclient package.
Group: Default

%description python
python components for the python-neutronclient package.


%prep
%setup -q -n python-neutronclient-6.0.0

%build
export LANG=C
export SOURCE_DATE_EPOCH=1489036369
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python2.7/site-packages python2 setup.py test || :
%install
export SOURCE_DATE_EPOCH=1489036369
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/neutron

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
