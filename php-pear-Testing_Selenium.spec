%define		_class		Testing
%define		_subclass	Selenium
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - PHP Client for the Selenium Remote Control test tool
Summary(pl.UTF-8):	%{_pearname} - Klient PHP dla narzędzia Selenium Remote Control
Name:		php-pear-%{_pearname}
Version:	0.4.4
Release:	1
License:	Apache v2.0
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	40b079eb2e388c5fbb98cc901ce93135
Patch0:		%{_pearname}-PHPUnit2.patch
URL:		http://pear.php.net/package/Testing_Selenium/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Obsoletes:	php-pear-Testing_Selenium-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Selenium Remote Control (SRC) is a test tool that allows you to write
automated web application UI tests in any programming language against
any HTTP website using any mainstream JavaScript-enabled browser. SRC
provides a Selenium Server, which can automatically start/stop/control
any supported browser. It works by using Selenium Core, a pure-HTML+JS
library that performs automated tasks in JavaScript; the Selenium
Server communicates directly with the browser using AJAX.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Selenium Remote Control (SRC) to narzędzie umożliwiające pisanie
automatycznych testów aplikacji internetowych na poziomie interfejsu
użytkownika. Umożliwia testowanie za pomocą większości przeglądarek
obsługujących JavaScript. SRC udostępnia Selenium Server,
automatycznie uruchamiający/wstrzymujący/sterujący dowolną obsługiwaną
przeglądarką. Działa za pomocą Selenium Core - biblioteki w czystym
HTML-u i JavaScripcie wykonującej zautomatyzowane zadania w
JavaScripcie; Selenium Server komunikuje się bezpośrednio z
przeglądarką poprzez AJAX.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup
%patch -P0 -p1

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/data/Testing_Selenium
%{php_pear_dir}/Testing/Selenium.php
%{php_pear_dir}/Testing/Selenium
