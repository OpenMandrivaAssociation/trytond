Name:		trytond
Summary:	The server of the Tryton application platform
Version:	2.2.2
Release:	2
License:	GPLv3+
Group:		Development/Python
Source0:	http://pypi.python.org/packages/source/t/trytond/%{name}-%{version}.tar.gz
%py_requires -d
BuildArch:	noarch
BuildRequires:  python-setuptools

%description
The server of the Tryton application platform.
A three-tiers  high-level general purpose application platform
written in Python and use Postgresql as main database engine.
It is the core base of an Open Source ERP.
It provides modularity, scalability and security.

%package -n python-%{name}
Summary:	Python modules for %{name}
Group:		Development/Python

%description -n python-%{name}
Python modules for %{name}

%prep
%setup -q

%build
python setup.py build

%install
NDONTWRITEBYTECODE=  python setup.py install --root=%{buildroot}
cp -a etc %{buildroot}

%files
%{_bindir}/%{name}
%doc CHANGELOG COPYRIGHT README TODO
%config(noreplace) %{_sysconfdir}/%{name}.conf

%files -n python-%{name}
%doc CHANGELOG COPYRIGHT README TODO
%{py_sitedir}/*


%changelog
* Thu Apr 19 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 2.2.2-1
+ Revision: 792127
- imported package trytond

