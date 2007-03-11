Summary:	X.org video driver for Glide capable video boards
Summary(pl.UTF-8):	Sterownik obrazu X.org dla kart graficznych obsługujących Glide
Name:		xorg-driver-video-glide
Version:	1.0.0
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-glide-%{version}.tar.bz2
# Source0-md5:	a2d71a92bc92a493579da59ea0324a45
URL:		http://xorg.freedesktop.org/
BuildRequires:	Glide2x_SDK
BuildRequires:	Mesa-libGL-devel
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libdrm-devel >= 2.0
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-proto-fontsproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-proto-renderproto-devel
BuildRequires:	xorg-proto-videoproto-devel
BuildRequires:	xorg-proto-xf86dgaproto-devel
BuildRequires:	xorg-proto-xf86driproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRequires:	xorg-xserver-server-devel >= 1.0.99.901
Requires:	xorg-xserver-server >= 1.0.99.901
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Driver for Glide capable video boards (such as 3Dfx Voodoo boards).

%description -l pl.UTF-8
Sterownik dla kart graficznych obsługujących Glide (jak np. karty 3Dfx Voodoo).

%prep
%setup -q -n xf86-video-glide-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/glide_drv.so
%{_mandir}/man4/glide.4*
