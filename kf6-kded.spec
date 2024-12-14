%define major %(echo %{version} |cut -d. -f1-2)
%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)

%define devname %mklibname KF6KDED -d
#define git 20240217

Name: kf6-kded
Version: 6.9.0
Release: %{?git:0.%{git}.}1
%if 0%{?git:1}
Source0: https://invent.kde.org/frameworks/kded/-/archive/master/kded-master.tar.bz2#/kded-%{git}.tar.bz2
%else
Source0: https://download.kde.org/%{stable}/frameworks/%{major}/kded-%{version}.tar.xz
%endif
Summary: Central daemon of KDE work spaces
URL: https://invent.kde.org/frameworks/kded
License: CC0-1.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0
Group: System/Libraries
BuildRequires: cmake
BuildRequires: cmake(ECM)
BuildRequires: python
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6QmlTools)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6GuiTools)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: gettext
BuildRequires: doxygen
BuildRequires: cmake(Qt6ToolsTools)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6Service)
BuildRequires: cmake(KF6DocTools)

%description
Central daemon of KDE work spaces

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{name} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

Central daemon of KDE work spaces

%prep
%autosetup -p1 -n kded-%{?git:master}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
%find_lang %{name} --all-name --with-html --with-qt --with-man

%files -f %{name}.lang
%{_datadir}/qlogging-categories6/kded.*
%{_bindir}/kded6
%{_prefix}/lib/systemd/user/plasma-kded6.service
%{_datadir}/applications/org.kde.kded6.desktop
%{_datadir}/dbus-1/interfaces/org.kde.kded6.xml
%{_datadir}/dbus-1/services/org.kde.kded6.service
%{_mandir}/man8/kded6.8*

%files -n %{devname}
%{_libdir}/cmake/KF6KDED
