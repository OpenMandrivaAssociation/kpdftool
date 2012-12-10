Summary:	GhostView and ImageMagick GUI for PDF/PS files
Name:		kpdftool
Version:	0.23.1
Release:	%mkrel 1
License:	GPLv3+
Group:		Text tools
URL:		http://www.kde-apps.org/content/show.php?content=33194
Source:		33194-kpdftool-%{version}.zip
BuildRequires:	qt4-devel
Suggests:	imagemagick
Suggests:	ghostscript
Suggests:	kword

%description
KPDFTool is a GUI interface for GhostView and ImageMagick
for performing basic and usefull operations with PDF and
PS (PostScript) files such as merge, extract pages and
protect the text into new files in a simple and practical way.

%prep
%setup -q

%build
%qmake_qt4
%make

%install
rm -rf %{buildroot}
install -d -m755 %{buildroot}%{_bindir}
install -m755 kpdftool %{buildroot}%{_bindir}

install -d -m755 %{buildroot}%{_iconsdir}
cp -r icons/hicolor %{buildroot}%{_iconsdir}/

install -d -m755 %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/kpdftool.desktop << EOF
[Desktop Entry]
Name=KPDFTool
Comment=Operate on PDF files
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Office;Publishing;KDE;Qt;
EOF

%clean
rm -rf %{buildroot}

%files
%doc README
%{_bindir}/kpdftool
%{_datadir}/applications/kpdftool.desktop
%{_iconsdir}/hicolor/*/apps/%{name}*

%changelog
* Tue May 29 2012 Andrey Bondrov <abondrov@mandriva.org> 0.23.1-1mdv2011.0
+ Revision: 801105
- New version 0.23.1, add icons, fix license

* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.22-4mdv2011.0
+ Revision: 620039
- the mass rebuild of 2010.0 packages

* Fri Sep 11 2009 Thierry Vignaud <tv@mandriva.org> 0.22-3mdv2010.0
+ Revision: 438139
- rebuild

* Sat Feb 28 2009 Anssi Hannula <anssi@mandriva.org> 0.22-2mdv2009.1
+ Revision: 345999
- fix build with gcc4.3 (includes.patch)
- use ldflags

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Fri Dec 28 2007 Anssi Hannula <anssi@mandriva.org> 0.22-1mdv2008.1
+ Revision: 138971
- initial Mandriva release

