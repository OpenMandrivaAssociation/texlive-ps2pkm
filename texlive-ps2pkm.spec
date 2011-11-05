# revision 23089
# category TLCore
# catalog-ctan /fonts/utilities/ps2pk
# catalog-date 2011-05-31 11:59:42 +0200
# catalog-license other-free
# catalog-version 1.6 beta 1
Name:		texlive-ps2pkm
Version:	1.6beta1
Release:	1
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
Conflicts:	texlive-texmf <= 20110705-3

%description
Generates a PK file from an Adobe Type 1 font. PK fonts are (or
used to be) valuable in enabling previewers to view documents
generated that use Type 1 fonts. The program makes use of code
donated to the X consortium by IBM.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_mandir}/man1/mag.1*
%{_texmfdir}/doc/man/man1/mag.man1.pdf
%{_mandir}/man1/pfb2pfa.1*
%{_texmfdir}/doc/man/man1/pfb2pfa.man1.pdf
%{_mandir}/man1/pk2bm.1*
%{_texmfdir}/doc/man/man1/pk2bm.man1.pdf
%{_mandir}/man1/ps2pk.1*
%{_texmfdir}/doc/man/man1/ps2pk.man1.pdf
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
