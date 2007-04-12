%define real_name CGI-Persistent

Summary:	CGI-Persistent module for perl 
Name:		perl-%{real_name}
Version:	1.00
Release: %mkrel 2
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/CGI/%{real_name}-%{version}.tar.gz
BuildRequires:	perl-devel
BuildRequires:  perl(CGI)
BuildRequires:  perl-Object-Persistence
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This module provides transparent state persistence for CGI applications.

%prep
%setup -q -n %{real_name}-%{version} 
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




