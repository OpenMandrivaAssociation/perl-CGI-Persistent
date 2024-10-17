%define upstream_name    CGI-Persistent
%define upstream_version 1.11

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	CGI-Persistent module for perl 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/CGI/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(CGI)
BuildRequires:	perl-Object-Persistence
BuildArch:	noarch

%description
This module provides transparent state persistence for CGI applications.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
chmod 0755 html/roach.cgi

%build
perl Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
%makeinstall_std

%files
%doc html/*
%{perl_vendorlib}/CGI/Persistent.pm
%{_mandir}/*/*


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 1.110.0-2mdv2011.0
+ Revision: 680694
- mass rebuild

* Wed Jul 29 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.110.0-1mdv2011.0
+ Revision: 403003
- rebuild using %%perl_convert_version

* Sun Jul 06 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.11-1mdv2009.0
+ Revision: 232106
- update to new version 1.11

* Sat Dec 22 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.00-3mdv2008.1
+ Revision: 136916
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Oct 28 2006 Nicolas LÃ©cureuil <neoclust@mandriva.org> 1.00-2mdv2007.0
+ Revision: 73393
- import perl-CGI-Persistent-1.00-2mdk

* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.00-2mdk
- Fix SPEC Using perl Policies
	- BuildRequires
	- Source URL
- use mkrel

* Fri Jul 15 2005 Andreas Hasenack <andreas@mandriva.com> 1.00-1mdk
- initial Mandriva package

