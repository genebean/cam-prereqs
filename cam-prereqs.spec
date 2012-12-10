%define name	cam-prereqs
%define version	1.0
%define release	1

Name:		%{name}
Version:	%{version}
Release:	%{release}%{?dist}
Summary:	This package ensures the system has the dependacncies to install and run Sun / Oracle CAM

Group:		Development/Libraries
License:	BSD
URL:		https://github.com/genebean/cam-prereqs
Source0:	https://github.com/genebean/cam-prereqs/downloads/%{name}-%{version}-%{release}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


# i686 packages that must be installed even if on an x86_64 machine
Requires:	libXtst.i686 libselinux.i686 audit-libs.i686 cracklib.i686 db4.i686 pam.i686 libstdc++.i686 zlib.i686

# Dependancies that are needed which are not limited to the i686 version
Requires:	ksh


%description
This program is intended to simplify the installation of
Sun / Oracle Common Array Manager (CAM). In particular, it ensures that the
i686 version of some programs are installed as CAM will only work when they
are present, even on x86_64 systems.


%prep
%setup -q -n cam-prereqs


%build


%install
rm -rf $RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc README.md LICENSE


%changelog
* Mon Dec 10 2012 Gene Liverman <gliverman@gmail.com>
- Initial version of this SPEC file based on requirements listed in the CAM
  6.9.0 install documents.

