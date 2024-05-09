Name: python-sherlock
Summary: Social media username hunter
Version: 0.1.2
Release: 1%{?dist}
License: MIT
URL: https://github.com/ppfeister/sherlock
Source: ${url}/archive/v%{version}/sherlock-%{version}.tar.gz

BuildArch: noarch
BuildRequires: python3-devel

%global _description %{expand:
Social media account username search}

%description %_description

%package -n python3-sherlock
Summary: %{summary}

%description -n python3-sherlock %_description

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
* Tue May 31 2016 Paul Pfeister <code@pfeister.dev>
- Send help