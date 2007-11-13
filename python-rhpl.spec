Summary:	Library of Python code used by some programs made by Red Hat
Summary(pl):	Biblioteka kodu Pythona u¿ywana przez niektóre programy Red Hata
Name:		python-rhpl
Version:	0.176
Release:	3
License:	GPL
Group:		Libraries
Source0:	rhpl-%{version}.tar.gz
# Source0-md5:	9ebe9200e71b07dae9b0a6e5a198dbe6
BuildRequires:	gettext-devel
BuildRequires:	libiw-devel
BuildRequires:	python-devel
%pyrequires_eq	python-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The rhpl package contains Python code used by some programs made by
Red Hat.

%description -l pl
Pakiet rhpl zawiera kod Pythona u¿ywany w niektórych programach
stworzonych przez Red Hata.

%prep
%setup -q -n rhpl-%{version}

# remove deprecated modules
# moved into python-rhpxl
rm -f src/{xserver,videocard,monitor,mouse,guesslcd,xhwstate}.py
# moved into firstboot
rm -f src/firstboot_gui_window.py

rm -f po/no.po

for module in . src/iconvmodule src/ethtool
do
	mv $module/Makefile $module/Makefile.old
	sed -e 's/$(PYTHON) /python /' $module/Makefile.old > $module/Makefile
	rm $module/Makefile.old
done

%build
%{__make} \
	CC="%{__cc}" \
	RPM_OPT_FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang rhpl

%clean
rm -rf $RPM_BUILD_ROOT

%files -f rhpl.lang
%defattr(644,root,root,755)
%doc ChangeLog README
%dir %{py_sitedir}/rhpl
%{py_sitedir}/rhpl/*.py*
%attr(755,root,root) %{py_sitedir}/rhpl/*.so
