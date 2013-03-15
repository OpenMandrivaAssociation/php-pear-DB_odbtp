%define		_class		DB
%define		_subclass	odbtp
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	1.0.4
Release:	8
Summary:	DB interface for ODBTP
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/DB_odbtp/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
DB_odbtp is a PEAR DB driver that uses the ODBTP extension to connect
to a database. It can be used to remotely access any Win32-ODBC
accessible database from any platform.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/docs/* %{upstream_name}-%{version}/examples
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.4-6mdv2012.0
+ Revision: 741849
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.4-5
+ Revision: 679293
- mass rebuild

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.4-4mdv2011.0
+ Revision: 613634
- the mass rebuild of 2010.1 packages

* Wed Dec 16 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.4-3mdv2010.1
+ Revision: 479293
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Thu Oct 01 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.4-2mdv2010.0
+ Revision: 452032
- fix %%postun

* Sat Sep 26 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.4-1mdv2010.0
+ Revision: 449526
- new version
- use pear installer
- use fedora %%post/%%postun

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 1.0.3-8mdv2010.0
+ Revision: 440998
- rebuild

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 1.0.3-7mdv2009.1
+ Revision: 321964
- rebuild

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0.3-6mdv2009.0
+ Revision: 236830
- rebuild

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 1.0.3-5mdv2008.1
+ Revision: 136404
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 1.0.3-5mdv2007.0
+ Revision: 81564
- Import php-pear-DB_odbtp

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 1.0.3-5mdk
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.3-4mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.3-3mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.3-2mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.3-1mdk
- 1.0.3

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-1mdk
- initial Mandriva package (PLD import)

