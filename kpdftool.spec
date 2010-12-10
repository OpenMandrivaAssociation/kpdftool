
%define name	kpdftool
%define version	0.22
%define rel	4

Summary:	GhostView and ImageMagick GUI for PDF/PS files
Name:		%{name}
Version:	%{version}
Release:	%mkrel %{rel}
License:	GPL+
Group:		Text tools
URL:		http://www.kde-apps.org/content/show.php?content=33194
Source:		33194-kpdftool-%{version}.zip
Patch0:		kpdftool-includes.patch
BuildRoot:	%{_tmppath}/%{name}-root
BuildRequires:	qt3-devel
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
%patch0 -p1

%build
export PATH=%{qt3dir}/bin:$PATH
qmake
%make CXXFLAGS="%{optflags}" LFLAGS="%{ldflags}"

%install
rm -rf %{buildroot}
install -d -m755 %{buildroot}%{_bindir}
install -m755 kpdftool %{buildroot}%{_bindir}

install -d -m755 %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/kpdftool.desktop << EOF
[Desktop Entry]
Name=KPDFTool
Comment=Operate on PDF files
Exec=%{_bindir}/kpdftool
Icon=publishing_section
Terminal=false
Type=Application
Categories=Office;Publishing;KDE;Qt;
EOF

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%files
%defattr(-,root,root)
%doc README
%{_bindir}/kpdftool
%{_datadir}/applications/kpdftool.desktop
