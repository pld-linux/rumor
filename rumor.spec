Summary:	Really Unintelligent Music transcriptOR
Name:		rumor
Version:	1.0.3b
Release:	2
License:	GPL v2
Group:		Applications/Sound
Source0:	http://www.volny.cz/smilauer/rumor/src/%{name}-%{version}.tar.bz2
# Source0-md5:	c95917356659b77bb83505cb2512ad1b
URL:		http://www.volny.cz/smilauer/rumor
BuildRequires:	alsa-lib-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	guile-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Rumor is a realtime monophonic (with chords) MIDI keyboard to Lilypond
converter. It receives MIDI events, quantizes them according to its
metronome on the fly and outputs handwritten-like corresponding
Lilypond notation. Tempo, meter, key and other parameters can be set
via command-line options.

%prep
%setup -q
%{__sed} -i '/CXXFLAGS=.*-O[0-3].*/d' configure.ac

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?debug:--disable-debug}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/rumor
%{_infodir}/rumor.info*
