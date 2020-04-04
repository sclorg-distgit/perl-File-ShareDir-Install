%{?scl:%scl_package perl-File-ShareDir-Install}

Name:           %{?scl_prefix}perl-File-ShareDir-Install
Version:        0.13
Release:        8%{?dist}
Summary:        Install shared files
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/File-ShareDir-Install
Source0:        https://cpan.metacpan.org/modules/by-module/File/File-ShareDir-Install-%{version}.tar.gz
BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  %{?scl_prefix}perl-generators
BuildRequires:  %{?scl_prefix}perl-interpreter
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
# Module Runtime
BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(Exporter)
BuildRequires:  %{?scl_prefix}perl(File::Spec)
BuildRequires:  %{?scl_prefix}perl(IO::Dir)
BuildRequires:  %{?scl_prefix}perl(strict)
BuildRequires:  %{?scl_prefix}perl(warnings)
# Test Suite
BuildRequires:  %{?scl_prefix}perl(Config)
BuildRequires:  %{?scl_prefix}perl(CPAN::Meta::YAML)
BuildRequires:  %{?scl_prefix}perl(File::Path)
BuildRequires:  %{?scl_prefix}perl(Test::More)
# Runtime
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%(%{?scl:scl enable %{scl} '}eval "$(perl -V:version)";echo $version%{?scl:'}))

%description
File::ShareDir::Install allows you to install read-only data files from a
distribution. It is a companion module to File::ShareDir, which allows you
to locate these files after installation.

%prep
%setup -q -n File-ShareDir-Install-%{version}

%build
%{?scl:scl enable %{scl} '}perl Makefile.PL INSTALLDIRS=vendor && make %{?_smp_mflags}%{?scl:'}

%install
%{?scl:scl enable %{scl} '}make pure_install DESTDIR=%{buildroot}%{?scl:'}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
%{?scl:scl enable %{scl} '}make test%{?scl:'}

%files
%doc LICENSE
%doc Changes CONTRIBUTING README
%{perl_vendorlib}/File/
%{_mandir}/man3/File::ShareDir::Install.3*

%changelog
* Fri Jan 03 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.13-8
- SCL

* Thu Sep  5 2019 Paul Howarth <paul@city-fan.org> - 0.13-7
- Use author-independent source URL

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.13-5
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.13-2
- Perl 5.28 rebuild

* Mon May 14 2018 Paul Howarth <paul@city-fan.org> - 0.13-1
- Update to 0.13
  - Add rules files for 'prove' and Test::Harness to specify that tests need to
    be run serially for now
  - Support spaces (and other special characters too) in share files (GH#2)
- BR: perl(CPAN::Meta::YAML) so we can process testrules.yml

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.11-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Aug  8 2016 Paul Howarth <paul@city-fan.org> - 0.11-1
- Update to 0.11
  - Release with new tooling
- This release by ETHER → update source URL
- BR: perl-generators
- Simpify find command using -delete

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.10-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.10-2
- Perl 5.22 rebuild

* Thu Dec 11 2014 Paul Howarth <paul@city-fan.org> - 0.10-1
- Update to 0.10
  - Recurse with $def in _scan_share_dir (CPAN RT#95749)

* Thu Nov 13 2014 Paul Howarth <paul@city-fan.org> - 0.09-1
- Update to 0.09
  - Get rid of DB::single
  - Don't do POD tests by default
- Specify all dependencies

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.08-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Feb  3 2014 Paul Howarth <paul@city-fan.org> - 0.08-1
- Update to 0.08
  - Tweak documentation and fix typos
  - Added $INCLUDE_DOTFILES and $INCLUDE_DOTDIRS
  - Added delete_share
  - Tests may now be run in parallel
- Don't need to remove empty directories from the buildroot

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 20 2013 Petr Pisar <ppisar@redhat.com> - 0.04-6
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 12 2012 Petr Pisar <ppisar@redhat.com> - 0.04-3
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Aug 28 2011 Iain Arnell <iarnell@gmail.com> 0.04-1
- update to latest upstream
- clean up spec for modern rpmbuild

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.03-6
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.03-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.03-4
- Rebuild to fix problems with vendorarch/lib (#661697)

* Sat May 01 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.03-3
- Mass rebuild with perl-5.12.0

* Sun Apr 04 2010 Iain Arnell <iarnell@gmail.com> 0.03-2
- use perl_default_filter and DESTDIR

* Fri Apr 02 2010 Iain Arnell 0.03-1
- Specfile autogenerated by cpanspec 1.78.
