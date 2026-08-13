%global tl_name carlito
%global tl_revision 77682

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Support for Carlito sans-serif fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/carlito
License:	ofl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/carlito.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/carlito.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
The package provides LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX support for
the Carlito family of sans serif fonts, designed by Lukasz Dziedzic of
the tyPoland foundry and adopted by Google for ChromeOS as a font-metric
compatible replacement for Calibri.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from carlito:
Map carlito.map
TL_DROPIN_EOF
