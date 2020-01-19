%global fontname sil-padauk
%global fontconf 65-%{fontname}
%global archivename padauk-2.8

%global common_desc \
Padauk is a Myanmar font covering all currently used characters \
in the Myanmar block. The font aims to cover all minority language needs. \
At the moment, these do not extend to stylistic variation needs. \
The font is a smart font using a Graphite description.

Name:    %{fontname}-fonts
Version: 2.8
Release: 4%{?dist}
Summary: A font for Burmese and the Myanmar script

Group:   User Interface/X
License: OFL
URL:     http://scripts.sil.org/Padauk
# The source link is a redirect and is not directly accessible
Source0: %{archivename}.zip
Source1: %{name}-fontconfig.conf
Source2: %{name}-book-fontconfig.conf

BuildArch: noarch
BuildRequires: fontpackages-devel
BuildRequires: fonttools
Requires:      fontpackages-filesystem

%description
%common_desc

%_font_pkg -f %{fontconf}.conf Padauk.ttf Padauk-bold.ttf
%doc *.txt

%package -n %{fontname}-book-fonts
Summary:  A font for Burmese and the Myanmar script

%description -n %{fontname}-book-fonts
Padauk Book family font.

%common_desc

%_font_pkg -n book -f %{fontconf}-book.conf Padauk-book*.ttf
%doc *.txt

%prep
%setup -q -n padauk-2.80
sed -i 's/\r//' OFL.txt

%build
# Following is needed to fix the postscript font name
ttx *.ttf
sed -i 's|&#225;&#128;&#149;&#225;&#128;&#173;&#225;&#128;&#144;&#225;&#128;&#177;&#225;&#128;&#172;&#225;&#128;&#128;&#225;&#128;&#186;|Padauk|g' Padauk*.ttx

sed -i 's|&#225;&#128;&#133;&#225;&#128;&#172;&#225;&#128;&#156;&#225;&#128;&#175;&#225;&#128;&#182;&#225;&#128;&#184;&#225;&#128;&#153;&#225;&#128;&#178;|Bold|g' Padauk*.ttx

sed -i 's|&#225;&#128;&#133;&#225;&#128;&#172;&#225;&#128;&#161;&#225;&#128;&#175;&#225;&#128;&#149;&#225;&#128;&#186;|Book|g' Padauk-book*.ttx
rm *.ttf
ttx Padauk*.ttx

rm *.ttx


%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}.conf
install -m 0644 -p %{SOURCE2} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-book.conf

ln -s %{_fontconfig_templatedir}/%{fontconf}.conf \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}.conf

ln -s %{_fontconfig_templatedir}/%{fontconf}-book.conf \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}-book.conf


%changelog
* Wed Mar 13 2013 Parag <paragn AT fedoraproject DOT org> - 2.8-4
- Resolves:rh#907330 - Fix the PostScript name in font files

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Nov 30 2012 Parag <paragn AT fedoraproject DOT org> - 2.8-2
- Package Padauk Book family font in separate subpackage

* Thu Nov 29 2012 Parag <paragn AT fedoraproject DOT org> - 2.8-1
- Resolves:rh#880012 - upstream new release available 2.8

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild


* Mon May 26 2009 Minto Joseph <mvaliyav at redhat.com> - 2.4-6
- Changed the URL

* Mon May 25 2009 Minto Joseph <mvaliyav at redhat.com> - 2.4-5
- Cleaned up the spec file
- Used Obsoletes for upgrade path from padauk-fonts

* Tue Mar 24 2009 Minto Joseph <mvaliyav at redhat.com> - 2.4-4
- Cleaned up the spec file as per new font packaging guidelines
- Replaced padauk-src.ttf and padaukbold-src.ttf with Padauk.ttf and Padauk-Bold.ttf [490583]
- Renamed the package to sil-padauk-fonts

* Sun Feb 22 2009 Minto Joseph <mvaliyav at redhat.com> - 2.4-3
- Changed the package as per new font packaging guidelines 


* Fri Jul 15 2008 Minto Joseph <mvaliyav at redhat.com> - 2.4-2
- Changed setup macro and fontconfig rules
- Changed fontconfig prefix


* Fri Jul 15 2008 Minto Joseph <mvaliyav at redhat.com> - 2.4-1
- Changed versioning
- Added configuration file
- Added more description
- Added license file

* Fri Jul 11 2008 Minto Joseph <mvaliyav at redhat.com> - 20080617-1
- initial package

