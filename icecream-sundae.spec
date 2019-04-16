Name:		icecream-sundae
Version:	1.0.0
Release:	1%{?dist}
Summary:	Commandline Monitor for Icecream

License:	GPL-2.0-only
Group:		Development/Tools/Building
URL:		https://github.com/JPEWdev/%{name}
Source0:	https://github.com/JPEWdev/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop

BuildRequires:	gcc-c++
BuildRequires:	meson
%if 0%{?fedora}
BuildRequires:	icecream-devel
BuildRequires:	desktop-file-utils
%else
%if 0%{?suse_version}
BuildRequires:	libicecream-devel
BuildRequires:	update-desktop-files
%endif
%endif
BuildRequires:	glib2-devel
BuildRequires:	ncurses-devel
# FIXME only valid if "libicecc links dynamically" test results to NO
#Checking if "libicecc links dynamically" links: NO
#WARNING: Static library 'icecc' not found for dependency 'icecc', may not be statically linked
#WARNING: Static library 'cap-ng' not found for dependency 'icecc', may not be statically linked
#WARNING: Static library 'lzo2' not found for dependency 'icecc', may not be statically linked
%if 0%{?suse_version}
BuildRequires:	libcap-ng-devel
BuildRequires:	lzo-devel
%endif

%description
%{summary}.

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install

mkdir -p %{buildroot}%{_datadir}/applications
install -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop
%if 0%{?fedora}
	desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
%else
%if 0%{?suse_version}
	%suse_update_desktop_file %{name}
%endif
%endif

%check
%meson_test

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%license LICENSE
%doc README.md

%changelog
* Tue Apr 16 2019 Tomas Novotny <tomas@novotny.cz> - 1.0.0-1
- Initial package
