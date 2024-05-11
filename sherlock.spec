%global pkg_norm_name sherlock
%global sherlock_version 0.10.0
%global python3_pkgversion 3
%global scm_ref feature/rpm-poc

Name: python-%{pkg_norm_name}
Version: %{sherlock_version}
Release: 1%{sherlock_release}%{?dist}
Summary: Hunt down social media accounts by username across social networks
Vendor: Sherlock Project
Packager: Paul Pfeister <rh-bugzilla@pfeister.dev>
License: MIT
URL: https://sherlock-project.github.io/
Source0: https://github.com/ppfeister/sherlock/archive/%{scm_ref}.tar.gz

BuildRequires: python%{python3_pkgversion}-devel
BuildRequires: python%{python3_pkgversion}-setuptools
BuildArch: noarch

%global _description %{expand:
Hunt down social media accounts by username across social networks}

%description %_description

%package -n python3-sherlock
Summary: %{summary}

%description -n python3-sherlock %_description

%prep
%autosetup -n %{pkg_norm_name}-%{scm_ref}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l sherlock

%files -n python3-sherlock -f %{pyproject_files}
%doc README.md

%changelog
* Tue May 31 2016 Paul Pfeister <rh-bugzilla@pfeister.dev>
- Sherlock RPM Proof of Concept