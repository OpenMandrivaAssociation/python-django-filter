%define module django-filter
%define oname django_filter

Name:		python-django-filter
Version:	25.2
Release:	1
Summary:	A Django application for allowing users to filter queryset dynamically
Group:		Development/Python
License:	BSD-3-Clause
URL:		https://github.com/carltongibson/django-filter
Source0:	%{URL}/archive/%{version}/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:		noarch
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(flit-core)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(django)

%description
Django-filter is a reusable Django application allowing users to
declaratively add dynamic QuerySet filtering from URL parameters.

%files
%doc README.rst
%license LICENSE
%{py_puresitedir}/%{oname}s
%{py_puresitedir}/%{oname}-%{version}.dist-info
