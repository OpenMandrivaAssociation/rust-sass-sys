# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate sass-sys

Name:           rust-%{crate}
Version:        0.4.17
Release:        2%{?dist}
Summary:        Low level binding for the Sass library

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/sass-sys
Source:         %{crates_source}
# Initial patched metadata
# * No windows
Patch0:         sass-sys-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Low level binding for the Sass library.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(libsass)

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
rm -vr libsass
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires
echo 'pkgconfig(libsass)'

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 27 2020 Josh Stone <jistone@redhat.com> - 0.4.17-1
- Update to 0.4.17

* Wed Jan 15 2020 Josh Stone <jistone@redhat.com> - 0.4.16-1
- Update to 0.4.16

* Sat Nov 23 2019 Josh Stone <jistone@redhat.com> - 0.4.15-1
- Update to 0.4.15

* Tue Nov 19 2019 Josh Stone <jistone@redhat.com> - 0.4.14-1
- Update to 0.4.14

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 23 10:32:49 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.10-2
- Regenerate

* Mon Jun 03 2019 Josh Stone <jistone@redhat.com> - 0.4.10-1
- Update to 0.4.10

* Fri May 31 13:50:18 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.9-1
- Initial package
