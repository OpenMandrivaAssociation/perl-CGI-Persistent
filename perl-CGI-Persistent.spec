%define upstream_name    CGI-Persistent
%define upstream_version 1.11

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:	CGI-Persistent module for perl 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/CGI/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:  perl(CGI)
BuildRequires:  perl-Object-Persistence
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This module provides transparent state persistence for CGI applications.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
chmod 0755 html/roach.cgi

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc html/*
%{perl_vendorlib}/CGI/Persistent.pm
%{_mandir}/*/*
