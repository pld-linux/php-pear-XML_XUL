%define		status		alpha
%define		pearname	XML_XUL
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - class to build Mozilla XUL applications
Summary(pl.UTF-8):	%{pearname} - klasa to budowania aplikacji Mozilli w XUL
Name:		php-pear-%{pearname}
Version:	0.9.0
Release:	3
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{pearname}-%{version}.tgz
# Source0-md5:	ba835b36572b0afee9248e2e9874eb93
URL:		http://pear.php.net/package/XML_XUL/
BuildRequires:	php-pear-PEAR >= 1:1.4.0-0.b1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.580
Requires:	php-pear
Requires:	php-pear-PEAR-core
Requires:	php-pear-XML_Parser2 >= 0.1.0
Requires:	php-pear-XML_Util2 >= 0.5.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The XML User Interface Language (XUL) is a markup language for
describing user interfaces. With XUL you can create rich,
sophisticated cross-platform web applications easily. XML_XUL provides
a API similar to DOM to create XUL applications. There's a PHP object
for each XUL element, and the more complex widgets like grids, trees
and tabboxes can easily be created with these objects.

In PEAR status of this package is: %{status}.

%description -l pl.UTF-8
Język Interfejsu Użytkownika w XML (XML User Interface Language lub
XUL) jest korzystającym ze znaczników językiem do opisu interfejsu
użytkownika. Z pomocą XUL możliwe jest łatwe stworzenie rozbudowanych
międzyplatformowych aplikacji internetowych. XML_XUL dostarcza API
zbliżonego do DOM w celu tworzeniu aplikacji XUL. Dla każdego elementu
XUL istnieje obiekt PHP, a bardziej złożone widgety takie jak siatki,
drzewa czy okna z zakładkami mogą być stworzone właśnie za pomocą tych
obiektów

Ta klasa ma w PEAR status: %{status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{pearname}/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/XML/*.php
%{php_pear_dir}/XML/XUL
