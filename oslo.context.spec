#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xB9069B1335700CDC (infra-root@openstack.org)
#
Name     : oslo.context
Version  : 2.13.0
Release  : 37
URL      : http://tarballs.openstack.org/oslo.context/oslo.context-2.13.0.tar.gz
Source0  : http://tarballs.openstack.org/oslo.context/oslo.context-2.13.0.tar.gz
Source99 : http://tarballs.openstack.org/oslo.context/oslo.context-2.13.0.tar.gz.asc
Summary  : Oslo Context library
Group    : Development/Tools
License  : Apache-2.0
Requires: oslo.context-python
Requires: debtcollector
Requires: pbr
Requires: positional
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
========================
Team and repository tags
========================
.. image:: http://governance.openstack.org/badges/oslo.context.svg
:target: http://governance.openstack.org/reference/tags/index.html

%package python
Summary: python components for the oslo.context package.
Group: Default

%description python
python components for the oslo.context package.


%prep
%setup -q -n oslo.context-2.13.0

%build
export LANG=C
export SOURCE_DATE_EPOCH=1489784211
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1489784211
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python2*/*
/usr/lib/python3*/*
