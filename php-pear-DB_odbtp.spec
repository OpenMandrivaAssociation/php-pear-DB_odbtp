%define		_class		DB
%define		_subclass	odbtp
%define		upstream_name	%{_class}_%{_subclass}

Summary:	DB interface for ODBTP
Name:		php-pear-%{upstream_name}
Version:	1.0.4
Release:	%mkrel 1
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/DB_odbtp/
Source0:	http://pear.php.net/get/%{upstream_name}-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
DB_odbtp is a PEAR DB driver that uses the ODBTP extension to connect
to a database. It can be used to remotely access any Win32-ODBC
accessible database from any platform.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install
rm -rf %{buildroot}

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%post
pear install --nodeps --soft --force --register-only \
    %{_datadir}/pear/packages/%{upstream_name}.xml >/dev/null || :

%preun
if [ "$1" -eq "0" ]; then
    pear uninstall --nodeps --ignore-errors --register-only \
        %{pear_name} >/dev/null || :
fi

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/docs/* %{upstream_name}-%{version}/examples
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml
