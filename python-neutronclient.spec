#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xFC43F0EE211DFED8 (infra-root@openstack.org)
#
Name     : python-neutronclient
Version  : 6.14.0
Release  : 49
URL      : http://tarballs.openstack.org/python-neutronclient/python-neutronclient-6.14.0.tar.gz
Source0  : http://tarballs.openstack.org/python-neutronclient/python-neutronclient-6.14.0.tar.gz
Source1 : http://tarballs.openstack.org/python-neutronclient/python-neutronclient-6.14.0.tar.gz.asc
Summary  : Python client library for Neutron
Group    : Development/Tools
License  : Apache-2.0
Requires: python-neutronclient-bin = %{version}-%{release}
Requires: python-neutronclient-license = %{version}-%{release}
Requires: python-neutronclient-python = %{version}-%{release}
Requires: python-neutronclient-python3 = %{version}-%{release}
Requires: Babel
Requires: cliff
Requires: debtcollector
Requires: iso8601
Requires: keystoneauth1
Requires: netaddr
Requires: os-client-config
Requires: osc-lib
Requires: oslo.i18n
Requires: oslo.log
Requires: oslo.serialization
Requires: oslo.utils
Requires: pbr
Requires: python-keystoneclient
Requires: requests
Requires: simplejson
Requires: six
BuildRequires : Babel
BuildRequires : buildreq-distutils3
BuildRequires : cliff
BuildRequires : debtcollector
BuildRequires : iso8601
BuildRequires : keystoneauth1
BuildRequires : netaddr
BuildRequires : os-client-config
BuildRequires : osc-lib
BuildRequires : oslo.i18n
BuildRequires : oslo.log
BuildRequires : oslo.serialization
BuildRequires : oslo.utils
BuildRequires : pbr
BuildRequires : python-keystoneclient
BuildRequires : requests
BuildRequires : simplejson
BuildRequires : six

%description
========================
Team and repository tags
========================
.. image:: https://governance.openstack.org/tc/badges/python-neutronclient.svg
:target: https://governance.openstack.org/tc/reference/tags/index.html

%package bin
Summary: bin components for the python-neutronclient package.
Group: Binaries
Requires: python-neutronclient-license = %{version}-%{release}

%description bin
bin components for the python-neutronclient package.


%package license
Summary: license components for the python-neutronclient package.
Group: Default

%description license
license components for the python-neutronclient package.


%package python
Summary: python components for the python-neutronclient package.
Group: Default
Requires: python-neutronclient-python3 = %{version}-%{release}

%description python
python components for the python-neutronclient package.


%package python3
Summary: python3 components for the python-neutronclient package.
Group: Default
Requires: python3-core

%description python3
python3 components for the python-neutronclient package.


%prep
%setup -q -n python-neutronclient-6.14.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1568907777
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/python-neutronclient
cp LICENSE %{buildroot}/usr/share/package-licenses/python-neutronclient/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/neutron

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/python-neutronclient/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
