#
# Conditional build:
%bcond_with	glide3	# use glide3x instead of glide2x (drops Voodoo Graphics support)
#
Summary:	X.org video driver for Glide capable video boards
Summary(pl.UTF-8):	Sterownik obrazu X.org dla kart graficznych obsługujących Glide
Name:		xorg-driver-video-glide
Version:	1.2.2
Release:	4
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-glide-%{version}.tar.bz2
# Source0-md5:	3e596591c51f8e276dc3067925992bb3
URL:		http://xorg.freedesktop.org/
%if %{with glide3}
BuildRequires:	Glide3x-devel
%else
BuildRequires:	Glide2x-devel
%endif
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	libtool >= 2:2.0
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	rpmbuild(macros) >= 1.389
BuildRequires:	xorg-proto-fontsproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-proto-renderproto-devel
BuildRequires:	xorg-proto-xextproto-devel >= 7.0.99.1
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xorg-xserver-server-devel >= 1.0.99.901
%{?requires_xorg_xserver_videodrv}
Requires:	xorg-xserver-server >= 1.0.99.901
Provides:	xorg-driver-video
Obsoletes:	X11-driver-glide < 1:7.0.0
Obsoletes:	XFree86-driver-glide < 1:7.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Driver for Glide capable video boards (such as 3Dfx Voodoo boards),
meant for use mainly with Voodoo 1 and Voodoo 2 boards (which don't
have 2D acceleration).

%description -l pl.UTF-8
Sterownik dla kart graficznych obsługujących Glide (jak np. karty 3Dfx
Voodoo), przeznaczony głównie dla kart Voodoo 1 i Voodoo 2 (nie
mających akceleratora 2D).

%prep
%setup -q -n xf86-video-glide-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_glide3:ac_cv_lib_glide3x_grGet=no}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/glide_drv.so
%{_mandir}/man4/glide.4*
