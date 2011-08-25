Summary:	X.org video driver for Glide capable video boards
Summary(pl.UTF-8):	Sterownik obrazu X.org dla kart graficznych obsługujących Glide
Name:		xorg-driver-video-glide
Version:	1.1.0
Release:	3
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-glide-%{version}.tar.bz2
# Source0-md5:	83a5df9af1efeb077e9f21a7b421a01f
URL:		http://xorg.freedesktop.org/
BuildRequires:	Glide2x_SDK
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	rpmbuild(macros) >= 1.389
BuildRequires:	xorg-proto-fontsproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-proto-renderproto-devel
BuildRequires:	xorg-proto-xextproto-devel >= 7.0.99.1
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xorg-xserver-server-devel >= 1.0.99.901
%{?requires_xorg_xserver_videodrv}
#Requires:	Glide2x (virtual for: Glide_VG/V2/V3(?))
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
%configure

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
