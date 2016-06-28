Summary:	MATE desktop tweak tool
Name:		mate-tweak
Version:	16.10.0
Release:	0.3
License:	GPL v2.0+
Group:		X11/Applications
Source0:	https://bitbucket.org/ubuntu-mate/mate-tweak/get/%{version}.tar.gz?/%{name}-%{version}.tar.gz
# Source0-md5:	176ad94494b065d03a085130b7be2b1d
URL:		https://bitbucket.org/ubuntu-mate/mate-tweak
Patch0:		%{name}-use-matemenu.patch
BuildRequires:	gobject-introspection-devel
BuildRequires:	intltool
BuildRequires:	python3-distutils-extra
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	Mesa-demo-x
Requires:	dconf
Requires:	mate-panel
Requires:	python3-configobj
Requires:	python3-pygobject
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

%prep
%setup -qc
mv ubuntu-mate-mate-tweak-*/* .
%patch0 -p1

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT
%py3_install

# Give gi-find-deps.sh a bait.
#ln -s %{_bindir}/%{name} $RPM_BUILD_ROOT%{_libexecdir}/%{name}/%{name}.py

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/frp
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/jv
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/shn
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/tpi

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

%{_datadir}/mate/applications/marco-compton.desktop
%{_datadir}/mate/applications/marco-no-composite.desktop
%{_datadir}/mate/applications/marco-xcompmgr.desktop
%{_datadir}/mate/applications/metacity-compton.desktop
%{_datadir}/mate/applications/metacity-no-composite.desktop
%{_datadir}/mate/applications/metacity-xcompmgr.desktop

%{py3_sitescriptdir}/mate_tweak-%{version}-py*.egg-info
