# revision 29764
# category TLCore
# catalog-ctan /fonts/utilities/ps2pk
# catalog-date 2012-07-20 20:39:39 +0200
# catalog-license other-free
# catalog-version 1.6 beta 1
Name:		texlive-ps2pkm
Version:	1.6beta1
Release:	6
Summary:	Generate a PK font from an Adobe Type 1 font
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/utilities/ps2pk
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ps2pkm.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires:	texlive-ps2pkm.bin

%description
Generates a PK file from an Adobe Type 1 font. PK fonts are (or
used to be) valuable in enabling previewers to view documents
generated that use Type 1 fonts. The program makes use of code
donated to the X consortium by IBM.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_mandir}/man1/mag.1*
%{_texmfdistdir}/doc/man/man1/mag.man1.pdf
%{_mandir}/man1/pfb2pfa.1*
%{_texmfdistdir}/doc/man/man1/pfb2pfa.man1.pdf
%{_mandir}/man1/pk2bm.1*
%{_texmfdistdir}/doc/man/man1/pk2bm.man1.pdf
%{_mandir}/man1/ps2pk.1*
%{_texmfdistdir}/doc/man/man1/ps2pk.man1.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdistdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
