Summary:	SAP music input plugin for XMMS
Summary(pl):	Wtyczka wej¶ciowa muzyki w formacie SAP dla XMMS
Name:		xmms-input-sap
Version:	0.4
Release:	1
License:	Freeware
Group:		X11/Applications/Sound
Source0:	http://kunik.republika.pl/sap/dl/insap-%{version}.tar.gz
URL:		http://kunik.republika.pl/sap/
BuildRequires:	libsap-devel
BuildRequires:	xmms-devel >= 1.2.3
Requires:	xmms
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
This plugin allows XMMS to play SAP (Atari XL/XE) music files.

%description -l pl
Ta wtyczka pozwala XMMS-owi odtwarzaæ pliki muzyczne w formacie SAP
(Atari XL/XE).

%prep
%setup -q -n insap-%{version}

%build
%{__make} \
	CC="%{__cc}" \
	OPTS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -D insap.so $RPM_BUILD_ROOT%{_libdir}/xmms/Input/insap.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README TODO
%attr(755,root,root) %{_libdir}/xmms/Input/*.so
