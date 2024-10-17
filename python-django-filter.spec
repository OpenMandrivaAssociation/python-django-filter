%define realname    django-filter
%define name	    python-%{realname}
%define version 0.5.4
%define release 2

Name: %{name}
Version:	2.2.0
Release:	1
Summary:        A Django application for allowing users to filter queryset dynamically
Group:          Development/Python
License:        BSD
URL:            https://pypi.python.org/pypi/django-filter
Source0:	https://files.pythonhosted.org/packages/dc/75/af3f0c2682d2603617ee3061b36395a64fb9d70c327bb759de43e643e5b3/django-filter-2.2.0.tar.gz
BuildArch:      noarch
BuildRequires:  python-devel python-setuptools
Requires:       python-django

%description
Django-filter provides a simple way to filter down a queryset based on
parameters a user provides.


%prep
%setup -q -n %{realname}-%{version}
find . -name \*._* -exec rm {} +
find . -name \*.buildinfo* -exec rm {} +

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%files
%{py_puresitedir}/*

