%define realname    django-filter
%define name	    python-%{realname}
%define version 0.5.3
%define release %mkrel 1

Name: %{name}
Version: %{version}
Release: %{release}
Summary:        A Django application for allowing users to filter queryset dynamically
Group:          Development/Python
License:        BSD
URL:            http://pypi.python.org/pypi/django-filter
Source:         %{realname}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
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
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{py_puresitedir}/*

