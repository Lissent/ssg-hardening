Name: ssg-hardening		
Version: 1.0.0
Release: 1.el5
Summary: A script used to preform hardening of the Layer7 Technology Secure Span Gateway

Group: Applications/System
License: ASL 2.0
URL: https://github.com/Layer7tech/ssg-hardening
Source0: v1.0.0
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch

#BuildRequires:	
Requires: python >= 2.4

%description
This script will implement hardening for the Layer7 Technology Secure Spam Gateway


%prep
# Will have the change the argument of -n for every new source as it is appended with the sha1sum of the commit
%setup -q -n Layer7tech-ssg-hardening-12ecdd1


%build


%install
rm -rf %{buildroot}
install ssg-hardening -D %{buildroot}/usr/bin/ssg-hardening
install etc/audit/audit.rules  -D %{buildroot}/etc/ssg-hardening/audit/audit.rules
install etc/pam.d/system-auth-ac  -D %{buildroot}/etc/ssg-hardening/pam.d/system-auth-ac


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%attr(550,-,-) %{_bindir}/ssg-hardening
%config %attr(550,-,-) %{_sysconfdir}/ssg-hardening
%config %attr(750,-,-) %{_sysconfdir}/ssg-hardening/audit
%config %attr(755,-,-) %{_sysconfdir}/ssg-hardening/pam.d
%config %attr(640,-,-) %{_sysconfdir}/ssg-hardening/audit/audit.rules
%config %attr(644,-,-) %{_sysconfdir}/ssg-hardening/pam.d/system-auth-ac

%changelog
* Mon Feb 06 2012 Frederic Masi <fmasi@layer7tech.com> 1.0.0-0
First release version.
For more info on how we got to this point please see https://github.com/Layer7tech/ssg-hardening/commits/master
