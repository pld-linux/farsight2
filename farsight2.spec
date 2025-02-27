Summary:	Audio/Video Communications Framework
Summary(pl.UTF-8):	Szkielet do komunikacji audio/video
Name:		farsight2
Version:	0.0.31
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	https://www.freedesktop.org/software/farstream/releases/farsight2/%{name}-%{version}.tar.gz
# Source0-md5:	3771d8268f025b28261cc1e977fab27f
Patch0:		%{name}-make.patch
Patch1:		gstreamer-common-gtkdoc.patch
Patch2:		%{name}-gtk-doc.patch
URL:		https://www.freedesktop.org/wiki/Software/Farstream/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	docbook-dtd412-xml
BuildRequires:	glib2-devel >= 1:2.26
BuildRequires:	gstreamer0.10-devel >= 0.10.33
BuildRequires:	gstreamer0.10-plugins-base-devel >= 0.10.33
BuildRequires:	gtk-doc >= 1.8
BuildRequires:	gupnp-devel >= 0.14
BuildRequires:	gupnp-igd-devel
BuildRequires:	libnice-devel >= 0.1.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 1:2.4
BuildRequires:	python-gstreamer0.10-devel >= 0.10.10
BuildRequires:	python-pyobject-devel >= 2.16.0
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpm-pythonprov
Requires:	glib2 >= 1:2.26
Requires:	gstreamer0.10 >= 0.10.33
Requires:	gstreamer0.10-plugins-base >= 0.10.33
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Farsight project is an effort to create a framework to deal with
all known audio/video conferencing protocols. On one side it offers a
generic API that makes it possible to write plugins for different
streaming protocols, on the other side it offers an API for clients to
use those plugins.

The main target clients for Farsight are Instant Messaging
applications. These applications should be able to use Farsight for
all their Audio/Video conferencing needs without having to worry about
any of the lower level streaming and NAT traversal issues.

%description -l pl.UTF-8
Projekt Farsight to próba stworzenia szkieletu do obsługi wszystkich
znanych protokołów konferencji audio/video. Z jednej strony oferuje
generyczne API umożliwiające tworzenie wtyczek do różnych protokołów
strumieniowych, z drugiej strony oferuje API klienckie do używania
tych wtyczek.

Głównym celem klientów Farsighta są komunikatory (aplikacje IM).
Powinny móc używać Farsighta do wszystkich potrzeb konferencji
audio/video bez zagłębiania się w niskopoziomowe szczegóły przesyłania
strumieni czy przechodzenia NAT.

%package devel
Summary:	Header files for farsight2 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki farsight2
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.26
Requires:	gstreamer0.10-devel >= 0.10.33
Requires:	gstreamer0.10-plugins-base-devel >= 0.10.33

%description devel
Header files for farsight2 library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki farsight2.

%package static
Summary:	Static farsight2 library
Summary(pl.UTF-8):	Statyczna biblioteka farsight2
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static farsight2 library.

%description static -l pl.UTF-8
Statyczna biblioteka farsight2.

%package apidocs
Summary:	farsight2 library API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki farsight2
Group:		Documentation
Requires:	gtk-doc-common
BuildArch:	noarch

%description apidocs
farsight2 library API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki farsight2.

%package -n python-farsight2
Summary:	farsight2 Python bindings
Summary(pl.UTF-8):	Wiązania Pythona do farsight2
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
Requires:	python-gstreamer0.10 >= 0.10.10
Requires:	python-pyobject >= 2.16.0

%description -n python-farsight2
farsight2 Python bindings.

%description -n python-farsight2 -l pl.UTF-8
Wiązania Pythona do farsight2.

%prep
%setup -q
%patch0 -p1
cd common
%patch1 -p1
cd ..
%patch2 -p1

%build
%{__gtkdocize}
%{__libtoolize}
%{__aclocal} -I common/m4 -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-gtk-doc \
	--disable-silent-rules \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/farsight2-0.0/*.{a,la}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/gstreamer-0.10/*.{a,la}
%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/*.{a,la}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libgstfarsight-0.10.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgstfarsight-0.10.so.0
%dir %{_libdir}/farsight2-0.0
%attr(755,root,root) %{_libdir}/farsight2-0.0/libmulticast-transmitter.so
%attr(755,root,root) %{_libdir}/farsight2-0.0/libnice-transmitter.so
%attr(755,root,root) %{_libdir}/farsight2-0.0/librawudp-transmitter.so
%attr(755,root,root) %{_libdir}/farsight2-0.0/libshm-transmitter.so
%attr(755,root,root) %{_libdir}/gstreamer-0.10/libfsfunnel.so
%attr(755,root,root) %{_libdir}/gstreamer-0.10/libfsmsnconference.so
%attr(755,root,root) %{_libdir}/gstreamer-0.10/libfsrawconference.so
%attr(755,root,root) %{_libdir}/gstreamer-0.10/libfsrtcpfilter.so
%attr(755,root,root) %{_libdir}/gstreamer-0.10/libfsrtpconference.so
%attr(755,root,root) %{_libdir}/gstreamer-0.10/libfsvideoanyrate.so
%dir %{_datadir}/farsight2
%dir %{_datadir}/farsight2/0.0
%{_datadir}/farsight2/0.0/fsrtpconference

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgstfarsight-0.10.so
%{_libdir}/libgstfarsight-0.10.la
%{_includedir}/gstreamer-0.10/gst/farsight
%{_pkgconfigdir}/farsight2-0.10.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgstfarsight-0.10.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/farsight2-libs-0.10
%{_gtkdocdir}/farsight2-plugins-0.10

%files -n python-farsight2
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/farsight.so
