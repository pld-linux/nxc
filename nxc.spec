# TODO:
# - fixme
# - -devel subpackage
Summary:	nxc
Name:		nxc
Version:	0.1.1
Release:	1
License:	GPL
Group:		Applications/Networking
Source0:	http://vm.gwright.org.uk/nxc-0.1.1.tar.bz2
# Source0-md5:	1688999d3d3a4fc01593214c0bcc9ea0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
nxc

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub admin
%{__make} -f admin/Makefile.common cvs

%configure \
	--enable-new-ldflags \
	--enable-final
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

%files -f %{name}.lang
%defattr(644,root,root,755)
