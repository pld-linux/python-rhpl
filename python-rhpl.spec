Summary:	Library of Python code used by some programs made by Red Hat
Summary(pl.UTF-8):	Biblioteka kodu Pythona używana przez niektóre programy Red Hata
Name:		python-rhpl
Version:	0.176
Release:	4
License:	GPL
Group:		Libraries
Source0:	rhpl-%{version}.tar.gz
# Source0-md5:	9ebe9200e71b07dae9b0a6e5a198dbe6
Patch0:		%{name}-enc.patch
BuildRequires:	gettext-devel
BuildRequires:	libiw-devel
BuildRequires:	python-devel >= 1:2.5
%pyrequires_eq	python-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The rhpl package contains Python code used by some programs made by
Red Hat.

%description -l pl.UTF-8
Pakiet rhpl zawiera kod Pythona używany w niektórych programach
stworzonych przez Red Hata.

%prep
%setup -q -n rhpl-%{version}
%patch0 -p1

# remove deprecated modules
# moved into python-rhpxl
rm -f src/{xserver,videocard,monitor,mouse,guesslcd,xhwstate}.py
# moved into firstboot
rm -f src/firstboot_gui_window.py

rm -f po/no.po

sed -i -e 's#gcc#%{__cc}#g' Makefile */Makefile */*/Makefile
sed -i -e 's/$(PYTHON) /python /' Makefile src/iconvmodule/Makefile src/ethtool/Makefile

%build
%{__make} \
	PYTHONINCLUDE="%{py_incdir}" \
	CC="%{__cc}" \
	RPM_OPT_FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	PYTHONLIBDIR="%{py_sitedir}" \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang rhpl

%clean
rm -rf $RPM_BUILD_ROOT

%files -f rhpl.lang
%defattr(644,root,root,755)
%doc ChangeLog README
%dir %{py_sitedir}/rhpl
%{py_sitedir}/rhpl/*.egg-info
%{py_sitedir}/rhpl/*.py*
%attr(755,root,root) %{py_sitedir}/rhpl/*.so
