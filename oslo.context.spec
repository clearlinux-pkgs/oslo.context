#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xC12B8E73B30F2FC8 (infra-root@openstack.org)
#
Name     : oslo.context
Version  : 3.1.1
Release  : 58
URL      : http://tarballs.openstack.org/oslo.context/oslo.context-3.1.1.tar.gz
Source0  : http://tarballs.openstack.org/oslo.context/oslo.context-3.1.1.tar.gz
Source1  : http://tarballs.openstack.org/oslo.context/oslo.context-3.1.1.tar.gz.asc
Summary  : Oslo Context library
Group    : Development/Tools
License  : Apache-2.0
Requires: oslo.context-license = %{version}-%{release}
Requires: oslo.context-python = %{version}-%{release}
Requires: oslo.context-python3 = %{version}-%{release}
Requires: debtcollector
Requires: pbr
BuildRequires : buildreq-distutils3
BuildRequires : debtcollector
BuildRequires : pbr

%description
Oslo Context Library
        ====================
        
        The Oslo context library has helpers to maintain useful information
        about a request context. The request context is usually populated in
        the WSGI pipeline and used by various modules such as logging.

%package license
Summary: license components for the oslo.context package.
Group: Default

%description license
license components for the oslo.context package.


%package python
Summary: python components for the oslo.context package.
Group: Default
Requires: oslo.context-python3 = %{version}-%{release}

%description python
python components for the oslo.context package.


%package python3
Summary: python3 components for the oslo.context package.
Group: Default
Requires: python3-core
Provides: pypi(oslo.context)
Requires: pypi(debtcollector)
Requires: pypi(pbr)

%description python3
python3 components for the oslo.context package.


%prep
%setup -q -n oslo.context-3.1.1
cd %{_builddir}/oslo.context-3.1.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1600109193
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/oslo.context
cp %{_builddir}/oslo.context-3.1.1/LICENSE %{buildroot}/usr/share/package-licenses/oslo.context/294b43b2cec9919063be1a3b49e8722648424779
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/oslo.context/294b43b2cec9919063be1a3b49e8722648424779

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
