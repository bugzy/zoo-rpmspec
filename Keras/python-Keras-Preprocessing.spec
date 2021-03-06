# Created by pyp2rpm-3.3.2
%global pypi_name Keras-Preprocessing

Name:           python-%{pypi_name}
Version:        1.0.5
Release:        1%{?dist}
Summary:        Easy data preprocessing and data augmentation for deep learning models

License:        MIT
URL:            https://github.com/keras-team/keras-preprocessing
Source0:        https://files.pythonhosted.org/packages/source/K/%{pypi_name}/Keras_Preprocessing-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(flake8)
BuildRequires:  python3dist(numpy) >= 1.9.1
BuildRequires:  python3dist(pandas)
BuildRequires:  python3dist(pillow)
BuildRequires:  python3dist(pillow) >= 5.2.0
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(pytest-xdist)
BuildRequires:  python3dist(scipy) >= 0.14
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(six) >= 1.9.0

%description
Keras Preprocessing is the data preprocessing and data augmentation module of
the Keras deep learning library. It provides utilities for working with image
data, text data, and sequence data.Read the documentation at: Preprocessing may
be imported directly from an up-to-date installation of Keras: from keras
import preprocessing Keras Preprocessing is compatible with Python 2.7-3.6 and
is...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3dist(flake8)
Requires:       python3dist(numpy) >= 1.9.1
Requires:       python3dist(pandas)
Requires:       python3dist(pillow)
Requires:       python3dist(pillow) >= 5.2.0
Requires:       python3dist(pytest)
Requires:       python3dist(pytest-cov)
Requires:       python3dist(pytest-xdist)
Requires:       python3dist(scipy) >= 0.14
Requires:       python3dist(six) >= 1.9.0
%description -n python3-%{pypi_name}
Keras Preprocessing is the data preprocessing and data augmentation module of
the Keras deep learning library. It provides utilities for working with image
data, text data, and sequence data.Read the documentation at: Preprocessing may
be imported directly from an up-to-date installation of Keras: from keras
import preprocessing Keras Preprocessing is compatible with Python 2.7-3.6 and
is...


%prep
%autosetup -n Keras_Preprocessing-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
# %license LICENSE
%doc README.md
%{python3_sitelib}/keras_preprocessing
%{python3_sitelib}/Keras_Preprocessing-%{version}-py?.?.egg-info

%changelog
* Thu Aug 08 2019 Grace Petegorsky <grace.petegorsky@yale.edu> - 1.0.5-1
- Downgrade to 1.0.5 for tensorflow
* Fri Jul 26 2019 Grace Petegorsky <grace.petegorsky@yale.edu> - 1.1.0-1
- Initial package.
