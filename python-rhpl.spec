Summary:	Library of python code used by programs in Red Hat Linux
Name:		python-rhpl
Version:	0.158
Release:	1
License:	GPL
Group:		System Environment/Libraries
Source0:	rhpl-%{version}.tar.gz
# Source0-md5:	6a9545f4bc70ed6ad390a25c08c0d968
BuildRequires:	gettext
BuildRequires:	python-devel
Requires:	python >= %(%{__python} -c "import sys; print sys.version[:3]")
%ifnarch s390 s390x
Requires:	python-xf86config >= 0.3.2
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The rhpl package contains Python code used by programs in Red Hat Linux.

%prep
%setup -q -n rhpl-%{version}

for module in . src/iconvmodule src/ethtool
do
	mv $module/Makefile $module/Makefile.old
	sed -e 's/$(PYTHON) /python /' $module/Makefile.old > $module/Makefile
	rm $module/Makefile.old
done

make

%build

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=${RPM_BUILD_ROOT} install

%find_lang rhpl

%clean
rm -rf $RPM_BUILD_ROOT

%files -f rhpl.lang
%defattr(644,root,root,755)
%doc README ChangeLog 
%{_libdir}/python?.?/site-packages/rhpl
%attr(755,root,root) %{_sbindir}/ddcprobe
%{_datadir}/rhpl
