#
# Conditional build:
%bcond_with	tests	# do perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	CGI
%define		pnam	Application-Dispatch
Summary:	CGI::Application::Dispatch - dispatch requests to CGI::Application based objects
Summary(pl.UTF-8):	CGI::Application::Dispatch - przesyłanie żądań do obiektów opartych na CGI::Application
Name:		perl-CGI-Application-Dispatch
Version:	3.05
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	3429676992e1b6a8e625738de883c687
URL:		http://search.cpan.org/dist/CGI-Application-Dispatch/
BuildRequires:	perl-CGI-Application
BuildRequires:	perl-Exception-Class
BuildRequires:	perl-Exception-Class-TryCatch
BuildRequires:	perl-Module-Build >= 0.20
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-build >= 4.3-0.20030515.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CGI::Application::Dispatch - dispatch requests to CGI::Application
based objects.

%description -l pl.UTF-8
CGI::Application::Dispatch służy do przesyłania żądań do obiektów
opartych na CGI::Application.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL Makefile.PL \
	installdirs=vendor \
	destdir=$RPM_BUILD_ROOT
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/CGI/Application/*.pm
%{perl_vendorlib}/CGI/Application/Dispatch
%{_mandir}/man3/*
