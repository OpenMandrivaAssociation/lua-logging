%define luaver 5.1
%define lualibdir %{_libdir}/lua/%{luaver}
%define luapkgdir %{_datadir}/lua/%{luaver}
%define oname lualogging

Name:           lua-logging
Version:        1.1.4
Release:        %mkrel 1
Summary:        A simple API to use logging features in Lua

Group:          Development/Other
License:        MIT
URL:            http://www.keplerproject.org/lualogging/
Source0:        http://luaforge.net/frs/download.php/2693/%{oname}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:  lua-devel >= %{luaver}
Requires:       lua >= %{luaver}

%description
LuaLogging provides a simple API to use logging features
in Lua. Its design was based on log4j. LuaLogging currently
supports, through the use of appenders, console, file, email,
socket and sql outputs.

%prep
%setup -q -n %{oname}-%{version}

%build
%make

%install
rm -rf %{buildroot}
make install PREFIX=$RPM_BUILD_ROOT/%{_prefix} LUA_LIBDIR=$RPM_BUILD_ROOT/%{lualibdir} LUA_DIR=$RPM_BUILD_ROOT/%{luapkgdir} SYS_BINDIR=$RPM_BUILD_ROOT/%{_bindir} LUA_INTERPRETER=%{_bindir}/lua


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc doc/us/*
%doc README
%{luapkgdir}/*
