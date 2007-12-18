Summary:	Library of Python code used by some programs made by Red Hat
Summary(pl.UTF-8):	Biblioteka kodu Pythona używana przez niektóre programy Red Hata
Name:		python-rhpl
Version:	0.212
Release:	1
License:	GPL
Group:		Libraries
Source0:	rhpl-%{version}.tar.bz2
# Source0-md5:	1cf6842afd763b6aa16ea4a3e326a4af
Patch0:		%{name}-enc.patch
BuildRequires:	gettext-devel
BuildRequires:	libiw-devel
BuildRequires:	python-devel >= 1:2.5
%pyrequires_eq	python-libs
Conflicts:	glibc-misc < 6:2.7
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

sed -i -e 's#gcc#%{__cc}#g' Makefile */Makefile */*/Makefile

%build
%{__make} \
	PYTHON="%{__python}" \
	PYTHONINCLUDE="%{py_incdir}" \
	CC="%{__cc}" \
	RPM_OPT_FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	PYTHON="%{__python}" \
	PYTHONLIBDIR="%{py_sitedir}" \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang rhpl

%clean
rm -rf $RPM_BUILD_ROOT

%files -f rhpl.lang
%defattr(644,root,root,755)
%doc README
%dir %{py_sitedir}/rhpl
%{py_sitedir}/rhpl/*.egg-info
%{py_sitedir}/rhpl/*.py*
%attr(755,root,root) %{py_sitedir}/rhpl/*.so
