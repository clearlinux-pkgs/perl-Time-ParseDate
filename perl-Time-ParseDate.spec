#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Time-ParseDate
Version  : 2015.103
Release  : 15
URL      : https://cpan.metacpan.org/authors/id/M/MU/MUIR/modules/Time-ParseDate-2015.103.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/MU/MUIR/modules/Time-ParseDate-2015.103.tar.gz
Summary  : 'Parse and format time values'
Group    : Development/Tools
License  : GPL-2.0
Requires: perl-Time-ParseDate-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
This package contains the following perl5 modules:
Time::CTime.pm
ctime, strftime, and asctime
Time::JulianDay.pm
Julian Day conversions
Time::ParseDate.pm
Reverses strftime and also understands relative times
Time::Timezone.pm
Time::DaysInMonth.pm

%package dev
Summary: dev components for the perl-Time-ParseDate package.
Group: Development
Provides: perl-Time-ParseDate-devel = %{version}-%{release}
Requires: perl-Time-ParseDate = %{version}-%{release}

%description dev
dev components for the perl-Time-ParseDate package.


%package perl
Summary: perl components for the perl-Time-ParseDate package.
Group: Default
Requires: perl-Time-ParseDate = %{version}-%{release}

%description perl
perl components for the perl-Time-ParseDate package.


%prep
%setup -q -n Time-ParseDate-2015.103
cd %{_builddir}/Time-ParseDate-2015.103

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Time::CTime.3
/usr/share/man/man3/Time::DaysInMonth.3
/usr/share/man/man3/Time::JulianDay.3
/usr/share/man/man3/Time::ParseDate.3
/usr/share/man/man3/Time::Timezone.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/Time/CTime.pm
/usr/lib/perl5/vendor_perl/5.34.0/Time/DaysInMonth.pm
/usr/lib/perl5/vendor_perl/5.34.0/Time/JulianDay.pm
/usr/lib/perl5/vendor_perl/5.34.0/Time/ParseDate.pm
/usr/lib/perl5/vendor_perl/5.34.0/Time/Timezone.pm
