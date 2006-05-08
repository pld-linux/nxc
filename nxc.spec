# TODO:
# - fixme
# - missing url (propably don't exist)
# - extendet summary and desc
# - pl
Summary:	nxc
Name:		nxc
Version:	0.1.1
Release:	1
License:	GPL
Group:		Applications/Networking
Source0:	http://vm.gwright.org.uk/%{name}-%{version}.tar.bz2
# Source0-md5:	1688999d3d3a4fc01593214c0bcc9ea0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
nxc

%package devel
Summary:	Header files for nxc
Summary(pl):	Pliki nag³ówkowe nxc
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
Header files for nxc.

%description devel -l pl
Pliki nag³ówkowe nxc.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub admin
%{__make} -f admin/Makefile.common cvs

%configure \
	--enable-new-ldflags \
	--enable-final \
	--disable-debug \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*.so.*.*.*
%{_prefix}/NX/share/client.id_dsa.key
#where put that ? ^^^^^^^^^^^^^^^^^^^

%files devel
%defattr(644,root,root,755)
%{_libdir}/*.la
%dir %{_includedir}/nxc
%{_includedir}/nxc/*.h
