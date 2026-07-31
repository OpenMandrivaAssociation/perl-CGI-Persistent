%define upstream_name    CGI-Persistent
%define upstream_version 1.11
Name:		perl-%{upstream_name}
Version:	1.11
Release:	12

Summary:	CGI-Persistent module for perl 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/CGI-Persistent
Source0:	https://cpan.metacpan.org/authors/id/V/VI/VIPUL/CGI-Persistent-1.11.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(CGI)
BuildRequires:	perl-Object-Persistence
BuildArch:	noarch

%description
This module provides transparent state persistence for CGI applications.

%prep
%setup -q -n CGI-Persistent-1.11
chmod 0755 html/roach.cgi

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build
make test || :

%check
make test || :

%install
%makeinstall_std

%files
%doc html/*
%{perl_vendorlib}/CGI/Persistent.pm
%{_mandir}/*/*


