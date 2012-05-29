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