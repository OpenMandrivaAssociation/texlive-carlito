Name:		texlive-carlito
Version:	64624
Release:	2
Summary:	Support for Carlito sans-serif fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/carlito
License:	ofl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/carlito.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/carlito.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX
support for the Carlito family of sans serif fonts, designed by
Lukasz Dziedzic of the tyPoland foundry and adopted by Google
for ChromeOS as a font-metric compatible replacement for
Calibri.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/carlito
%{_texmfdistdir}/fonts/vf/google/carlito
%{_texmfdistdir}/fonts/type1/google/carlito
%{_texmfdistdir}/fonts/truetype/google/carlito
%{_texmfdistdir}/fonts/tfm/google/carlito
%{_texmfdistdir}/fonts/map/dvips/carlito
%{_texmfdistdir}/fonts/enc/dvips/carlito
%doc %{_texmfdistdir}/doc/fonts/carlito

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
