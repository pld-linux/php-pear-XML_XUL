%include	/usr/lib/rpm/macros.php
%define		_class		XML
%define		_subclass	XUL
%define		_status		alpha
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - class to build Mozilla XUL applications
Summary(pl):	%{_pearname} - klasa to budowania aplikacji Mozilli w XUL
Name:		php-pear-%{_pearname}
Version:	0.6.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	68b39bdfde0bc4f10917c036da7d7f07
URL:		http://pear.php.net/package/XML_XUL/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The XML User Interface Language (XUL) is a markup language for
describing user interfaces. With XUL you can create rich, sophisticated
cross-platform web applications easily. XML_XUL provides a API similar
to DOM to create XUL applications. There's a PHP object for each XUL
element, and the more complex widgets like grids, trees and tabboxes can
easily be created with these objects.

This class has in PEAR status: %{_status}.

%description -l pl
Jêzyk Interfejsu U¿ytkownika w XML (XML User Interface Language lub XUL)
jest korzystaj±cym ze znaczników jêzykiem do opisu interfejsu
u¿ytkownika. Z pomoc± XUL mo¿liwe jest ³atwe stworzenie rozbudowanych
miêdzyplatformowych aplikacji internetowych. XML_XUL dostarcza API
zbli¿onego do DOM w celu tworzeniu aplikacji XUL. Dla ka¿dego elementu
XUL istnieje obiekt PHP, a bardziej z³o¿one widgety takie jak siatki,
drzewa czy okna z zak³adkami mog± byæ stworzone w³a¶nie za pomoc± tych
obiektów

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Element

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}
install %{_pearname}-%{version}/%{_subclass}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}
install %{_pearname}-%{version}/%{_subclass}/Element/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Element

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/examples
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}
