# revision 33818
# category TLCore
# catalog-ctan /fonts/utilities/ps2pk
# catalog-date 2014-02-26 23:03:13 +0100
# catalog-license other-free
# catalog-version 1.6 beta 1
Name:		texlive-ps2pkm
Version:	1.6beta1
Release:	13
Summary:	Generate a PK font from an Adobe Type 1 font
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/utilities/ps2pk
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ps2pkm.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ps2pkm.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-ps2pkm.bin

%description
Generates a PK file from an Adobe Type 1 font. PK fonts are (or
used to be) valuable in enabling previewers to view documents
generated that use Type 1 fonts. The program makes use of code
donated to the X consortium by IBM.

#-----------------------------------------------------------------------
%files
%doc %{_mandir}/man1/mag.1*
%doc %{_texmfdistdir}/doc/man/man1/mag.man1.pdf
%doc %{_mandir}/man1/pfb2pfa.1*
%doc %{_texmfdistdir}/doc/man/man1/pfb2pfa.man1.pdf
%doc %{_mandir}/man1/pk2bm.1*
%doc %{_texmfdistdir}/doc/man/man1/pk2bm.man1.pdf
%doc %{_mandir}/man1/ps2pk.1*
%doc %{_texmfdistdir}/doc/man/man1/ps2pk.man1.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdistdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
