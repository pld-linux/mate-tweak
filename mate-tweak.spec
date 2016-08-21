# TODO
# - ubuntu specific multiarch paths for indicators
Summary:	MATE desktop tweak tool
Summary(pl.UTF-8):	Narzędzie do dostrajania środowiska MATE
Name:		mate-tweak
Version:	16.10.4
Release:	3
License:	GPL v2+
Group:		X11/Applications
Source0:	https://bitbucket.org/ubuntu-mate/mate-tweak/get/%{version}.tar.gz?/%{name}-%{version}.tar.gz
# Source0-md5:	1fbfcb3523c98cc4342c61f3f1130dd2
Patch0:		%{name}-use-matemenu.patch
URL:		https://bitbucket.org/ubuntu-mate/mate-tweak
BuildRequires:	gobject-introspection-devel
BuildRequires:	intltool
BuildRequires:	python3-distutils-extra
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	sed >= 4.0
#Requires:	Mesa-demo-x
Requires:	dconf
Requires:	gobject-introspection
Requires:	gtk+3 >= 3.0
Requires:	libnotify >= 0.7
Requires:	mate-panel
Requires:	python3-configobj
Requires:	python3-psutil
Requires:	python3-pygobject3 >= 3.0
Requires:	python3-setproctitle
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_prefix}/lib

%description
Configures some aspects of the MATE desktop not exposed via the MATE
Control Centre applets.

Settings that can be handled via MATE Tweak:
 - Show/hide standard desktop icons.
 - Panel fine-tuning (icon visibility, in menus and on buttons, icon
   size, button labelling, contex menus, etc.).
 - Window manager fine-tuning.

%description -l pl.UTF-8
MATE Tweak to narzędzie do konfiguracji niektórych aspektów środowiska
graficznego MATE, nie udostępniony poprzez aplety MATE Control Centre.

Ustawienia obsługiwane przez MATE Tweak:
- pokazywanie/ukrywanie standardowych ikon pulpitu
- dostrajanie panelu (widoczność ikon w menu i na przyciskach, rozmiar
  ikon, etykiety przycisków, menu kontekstowe itp.)
- dostrajanie zarządcy okien

%prep
%setup -qc
%{__mv} ubuntu-mate-mate-tweak-*/* .
%patch0 -p1

%{__sed} -i -e '1s,/usr/bin/env python3,%{__python3},' util/{disable-mate-volume-applet,mate-panel-backup,install-mate-panel-layout}
%{__sed} -i -e '1s,/usr/bin/env bash,/bin/bash,' marco-{compton,xcompmgr,no-composite} metacity-{compton,xcompmgr,no-composite}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

# Give gi-find-deps.sh a bait.
#ln -s %{_bindir}/%{name} $RPM_BUILD_ROOT%{_libexecdir}/%{name}/%{name}.py

# es_419,zh-Hans are bogus
# frp,jv,ku_IQ,nah,nqo,pms,sco,tpi not supported by glibc
# ur_PK an ampty version or ur
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{es_419,frp,jv,ku_IQ,nah,nqo,pms,sco,tpi,ur_PK,zh-Hans}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database

%postun
%update_desktop_database

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/marco-compton
%attr(755,root,root) %{_bindir}/marco-no-composite
%attr(755,root,root) %{_bindir}/marco-xcompmgr
%attr(755,root,root) %{_bindir}/mate-tweak
%attr(755,root,root) %{_bindir}/metacity-compton
%attr(755,root,root) %{_bindir}/metacity-no-composite
%attr(755,root,root) %{_bindir}/metacity-xcompmgr
%{_mandir}/man1/marco-compton.1*
%{_mandir}/man1/marco-no-composite.1*
%{_mandir}/man1/mate-tweak.1*
%{_mandir}/man1/metacity-compton.1*
%{_mandir}/man1/metacity-no-composite.1*
%{_desktopdir}/mate-tweak.desktop
%{_datadir}/polkit-1/actions/org.mate.mate-tweak.policy

%dir %{_libexecdir}/mate-tweak
%{_libexecdir}/mate-tweak/disable-mate-volume-applet
%{_libexecdir}/mate-tweak/install-mate-panel-layout
%{_libexecdir}/mate-tweak/mate-panel-backup
%{_libexecdir}/mate-tweak/mate-tweak.ui

%dir %{_datadir}/mate-tweak
%{_datadir}/mate-tweak/mate-volume-control-applet.desktop

%dir %{_datadir}/mate/applications
%{_datadir}/mate/applications/marco-compton.desktop
%{_datadir}/mate/applications/marco-no-composite.desktop
%{_datadir}/mate/applications/marco-xcompmgr.desktop
%{_datadir}/mate/applications/metacity-compton.desktop
%{_datadir}/mate/applications/metacity-no-composite.desktop
%{_datadir}/mate/applications/metacity-xcompmgr.desktop

%{py3_sitescriptdir}/mate_tweak-%{version}-py*.egg-info
