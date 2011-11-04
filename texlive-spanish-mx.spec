# revision 15878
# category Package
# catalog-ctan /language/spanish/babel/contrib/mexican
# catalog-date 2009-01-10 16:42:45 +0100
# catalog-license lppl
# catalog-version 1.1a
Name:		texlive-spanish-mx
Version:	1.1a
Release:	1
Summary:	Typeset Spanish as in Mexico
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/spanish/babel/contrib/mexican
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/spanish-mx.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/spanish-mx.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3

%description
The bundle provides files to support typesetting of texts in
Spanish according to Mexican current practices, using babel.
The files merge earlier work on a mexican.ldf, or may be used
to define a configuration that will typeset all documents (that
request babel's spanish option) to use the Mexican language
facilities. (Note that this facility is only available with the
recent (version >=4.2b) releases of the Spanish option.).

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
%{_texmfdistdir}/tex/latex/spanish-mx/esmx.cfg
%{_texmfdistdir}/tex/latex/spanish-mx/spanishmx.ldf
%{_texmfdistdir}/tex/latex/spanish-mx/spanishmx.sty
%doc %{_texmfdistdir}/doc/latex/spanish-mx/README
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
