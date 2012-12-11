%define name	cam-prereqs
%define version	1.0
%define release	3

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
Requires:	libXtst(x86-32) libselinux(x86-32) audit-libs(x86-32) 
Requires:	cracklib(x86-32) db4(x86-32) pam(x86-32) 
Requires:	libstdc++(x86-32) zlib(x86-32)

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
# rpmlint shows an error by not doing "rm -rf $RPM_BUILD_ROOT" here...
# putting it in breaks the build.

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc README.md LICENSE


%changelog
* Tue Dec 11 2012 Gene Liverman <gliverman@gmail.com - 1.0-3
- Corrected Requires, replacing .i686 with (x86-32).
- Changed the 32-bit dependancies to be on more than one line.

* Mon Dec 10 2012 Gene Liverman <gliverman@gmail.com> - 1.0-2
- Modified install section to fix build error.

* Mon Dec 10 2012 Gene Liverman <gliverman@gmail.com> - 1.0-1
- Initial version of this SPEC file based on requirements listed in the CAM
  6.9.0 install documents.

