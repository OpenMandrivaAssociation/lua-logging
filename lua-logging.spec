%define luaver 5.1
%define lualibdir %{_libdir}/lua/%{luaver}
%define luapkgdir %{_datadir}/lua/%{luaver}
%define oname lualogging

Name:           lua-logging
Version:        1.3.0
Release:        1
Summary:        A simple API to use logging features in Lua

Group:          Development/Other
License:        MIT
URL:            http://www.keplerproject.org/lualogging/
Source0:        https://github.com/Neopallium/lualogging/archive/v%{version}/%{oname}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:       lua >= %{luaver}
Requires:       lua-socket
Requires:       lua-sql
BuildArch:      noarch

%description
LuaLogging provides a simple API to use logging features
in Lua. Its design was based on log4j. LuaLogging currently
supports, through the use of appenders, console, file, email,
socket and sql outputs.

%prep
%setup -q -n %{oname}-%{version}

%build
%make_build

%install
rm -rf %{buildroot}
%make_install PREFIX=$RPM_BUILD_ROOT/%{_prefix} LUA_LIBDIR=$RPM_BUILD_ROOT/%{lualibdir} LUA_DIR=$RPM_BUILD_ROOT/%{luapkgdir} SYS_BINDIR=$RPM_BUILD_ROOT/%{_bindir} LUA_INTERPRETER=%{_bindir}/lua


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc doc/us/*
%doc README
%{luapkgdir}/*


%changelog
* Wed Dec 08 2010 Rémy Clouard <shikamaru@mandriva.org> 1.1.4-4mdv2011.0
+ Revision: 616182
- rebuild for the mass rebuild

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 1.1.4-3mdv2010.0
+ Revision: 439643
- rebuild

* Sun Dec 28 2008 Jérôme Soyer <saispo@mandriva.org> 1.1.4-2mdv2009.1
+ Revision: 320488
- Add Requires

* Sun Dec 28 2008 Jérôme Soyer <saispo@mandriva.org> 1.1.4-1mdv2009.1
+ Revision: 320487
- Remove dot in Summary
- import lua-logging


