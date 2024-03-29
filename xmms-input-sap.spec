Summary:	SAP music input plugin for XMMS
Summary(pl.UTF-8):	Wtyczka wejściowa dla XMMS-a odtwarzająca muzykę w formacie SAP
Name:		xmms-input-sap
Version:	0.4
Release:	4
License:	Freeware
Group:		X11/Applications/Sound
Source0:	http://kunik.republika.pl/sap/dl/insap-%{version}.tar.gz
# Source0-md5:	d92c9ec6cc0312dd86376134f758a1eb
URL:		http://kunik.republika.pl/sap/
BuildRequires:	libsap-devel
BuildRequires:	rpmbuild(macros) >= 1.125
BuildRequires:	xmms-devel >= 1.2.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This plugin allows XMMS to play SAP (Atari XL/XE) music files.

%description -l pl.UTF-8
Ta wtyczka pozwala XMMS-owi odtwarzać pliki muzyczne w formacie SAP
(Atari XL/XE).

%prep
%setup -q -n insap-%{version}

%build
%{__make} \
	CC="%{__cc} -fPIC" \
	OPTS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{xmms_input_plugindir}

install insap.so $RPM_BUILD_ROOT%{xmms_input_plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README TODO
%attr(755,root,root) %{xmms_input_plugindir}/*.so
