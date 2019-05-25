%define		kdeframever	5.56
%define		qtver		5.9.0
%define		kfname		syndication

Summary:	syndication
Name:		kf5-%{kfname}
Version:	5.56.0
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/frameworks/%{kdeframever}/%{kfname}-%{version}.tar.xz
# Source0-md5:	1d7c5865589f34626f6f093a39a5e85a
URL:		http://www.kde.org/
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Network-devel >= 5.9.0
BuildRequires:	Qt5Test-devel
BuildRequires:	Qt5Widgets-devel >= 5.9.0
BuildRequires:	Qt5Xml-devel >= 5.9.0
BuildRequires:	cmake >= 2.8.12
BuildRequires:	kf5-extra-cmake-modules >= 5.53.0
BuildRequires:	kf5-kcodecs-devel >= 5.53.0
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	kf5-dirs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt5dir		%{_libdir}/qt5

%description
An RSS/Atom parser library.

%package devel
Summary:	Header files for %{kfname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kfname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kfname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kfname}.

%prep
%setup -q -n %{kfname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
        DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.md
/etc/xdg/syndication.categories
%attr(755,root,root) %ghost %{_libdir}/libKF5Syndication.so.5
%attr(755,root,root) %{_libdir}/libKF5Syndication.so.5.*.*


%files devel
%defattr(644,root,root,755)
%{_includedir}/KF5/Syndication
%{_includedir}/KF5/syndication_version.h
%{_libdir}/cmake/KF5Syndication
%attr(755,root,root) %{_libdir}/libKF5Syndication.so
%{_libdir}/qt5/mkspecs/modules/qt_Syndication.pri
