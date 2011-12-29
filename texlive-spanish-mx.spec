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
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The bundle provides files to support typesetting of texts in
Spanish according to Mexican current practices, using babel.
The files merge earlier work on a mexican.ldf, or may be used
to define a configuration that will typeset all documents (that
request babel's spanish option) to use the Mexican language
facilities. (Note that this facility is only available with the
recent (version >=4.2b) releases of the Spanish option.).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/spanish-mx/esmx.cfg
%{_texmfdistdir}/tex/latex/spanish-mx/spanishmx.ldf
%{_texmfdistdir}/tex/latex/spanish-mx/spanishmx.sty
%doc %{_texmfdistdir}/doc/latex/spanish-mx/README

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
