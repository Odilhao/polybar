Name: polybar
Version: 3.4.3
Release: 1%{?dist}
Summary: A fast and easy-to-use tool for creating status bars

Group: System/GUI/Other
License: MIT
URL: https://github.com/jaagr/polybar
Source0: %{url}/releases/download/%{version}/%{name}-%{version}.tar

BuildRequires: alsa-lib-devel
BuildRequires: binutils
BuildRequires: cairo-devel
BuildRequires: clang
BuildRequires: cmake
BuildRequires: cmake-data
BuildRequires: git
BuildRequires: i3
BuildRequires: python3-i3ipc
BuildRequires: jsoncpp-devel
BuildRequires: libcurl-devel
BuildRequires: libmpdclient-devel
BuildRequires: libxcb-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: python2
BuildRequires: python3
BuildRequires: python3-sphinx
BuildRequires: wireless-tools-devel
BuildRequires: xcb-proto
BuildRequires: xcb-util-image-devel
BuildRequires: xcb-util-wm-devel
BuildRequires: xcb-util-xrm-devel
BuildRequires: i3-devel
Requires: cairo
Requires: cairo-devel
Requires: jsoncpp
Requires: python2
Requires: xcb-util-devel
Requires: libxcb-devel
Requires: xcb-proto
Requires: xcb-util-cursor
Requires: xcb-util-image-devel
Requires: xcb-util-image
Requires: xcb-util-wm
Requires: xcb-util-xrm
Requires: xcb-util-wm-devel

%if 0%{?fedora}
BuildRequires:  python2
BuildRequires:  wireless-tools-devel
BuildRequires:  python-i3ipc
%else
BuildRequires:  pkgconfig
BuildRequires:  python-xml
BuildRequires:  pkgconfig(python)
%if 0%{?suse_version} <= 1315
BuildRequires:  i3-devel
%else
BuildRequires:  i3-gaps-devel
%endif
%if 0%{?suse_version}
BuildRequires:  libiw-devel
%else
BuildRequires:  wireless-tools-devel
%endif
%endif

%description
Polybar aims to help users build beautiful and highly customizable status bars for their desktop enclean fullvironment,
 without the need of having a black belt in shell scripting.
The main purpose of Polybar is to help users create awesome status bars. It has built-in functionality to display infor
mation about the most commonly used services.

%global debug_package %{nil}

%prep
%setup -q -n %{name}

%build
mkdir build
cd build
cmake .. \
    -DCMAKE_INSTALL_PREFIX:PATH=/usr \
    -DCMAKE_C_COMPILER="clang" \
    -DCMAKE_CXX_COMPILER="clang++" \
    -DENABLE_ALSA:BOOL="ON" \
    -DENABLE_I3:BOOL="ON" \
    -DENABLE_MPD:BOOL="ON" \
    -DENABLE_NETWORK:BOOL="ON" \
    -DENABLE_CURL:BOOL="ON"
make %{?_smp_mflags}

%install
cd build
chmod +x bin/polybar bin/polybar-msg
%make_install
%check

%files
%{_bindir}/%{name}
%{_bindir}/%{name}-msg
%{_mandir}/man1/%{name}.1.gz
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/zsh/site-functions/_%{name}
%{_datadir}/zsh/site-functions/_%{name}_msg
%config(noreplace) %{_datadir}/doc/%{name}/*
%{_datadir}/doc/%{name}/.buildinfo



%changelog
* Tue Aug 25 2020 - Odilon Junior <odilon@mail.com>
- Version 3.4.3
