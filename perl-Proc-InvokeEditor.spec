%define upstream_name    Proc-InvokeEditor
%define upstream_version 1.03

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Perl extension for starting a text editor
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Proc/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Carp::Assert)
BuildRequires: perl(File::Spec)
BuildRequires: perl(File::Temp)
BuildRequires: perl(Test::More)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This module provides the ability to supply some text to an external text
editor, have it edited by the user, and retrieve the results.

The File::Temp module is used to provide secure, safe temporary files, and
File::Temp is set to its highest available level of security. This may
cause problems on some systems where no secure temporary directory is
available.

When the editor is started, no subshell is used. Your path will be scanned
to find the binary to use for each editor if the string given does not
exist as a file, and if a named editor contains whitespace, eg) if you try
to use the editor 'xemacs -nw', then the string will be split on whitespace
and anything after the editor name will be passed as arguments to your
editor. A shell is not used but this should cover most simple cases.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc META.yml Changes LICENSE README
%{_mandir}/man3/*
%perl_vendorlib/Proc/


