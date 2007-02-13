# TODO:
# - fixme
# - missing url (propably doesn't exist)
# - extend summary and desc
# - pl
Summary:	NX protocol libraries
Summary(pl.UTF-8):	Biblioteki protokołu NX
Name:		nxc
Version:	0.1.1
Release:	3
License:	GPL
Group:		Applications/Networking
Source0:	http://vm.gwright.org.uk/%{name}-%{version}.tar.bz2
# Source0-md5:	1688999d3d3a4fc01593214c0bcc9ea0
Patch0:		%{name}-nxdir.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NX protocol libraries.

%description -l pl.UTF-8
Biblioteki protokołu NX.

%package devel
Summary:	Header files for nxc
Summary(pl.UTF-8):	Pliki nagłówkowe nxc
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
Header files for nxc.

%description devel -l pl.UTF-8
Pliki nagłówkowe nxc.

%prep
%setup -q
%patch0 -p1

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
# where put that ?
# %{_prefix}/NX/share/client.id_dsa.key

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/*.la
%dir %{_includedir}/nxc
%{_includedir}/nxc/*.h
