#
#   - Shell::EnvImporter -
#   This spec file was automatically generated by cpan2rpm [ver: 2.026]
#   The following arguments were used:
#       .
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define pkgname Shell-EnvImporter
%define filelist %{pkgname}-%{version}-filelist
%define NVR %{pkgname}-%{version}-%{release}
%define maketest 1

Name:      perl-Shell-EnvImporter
Summary:   Shell-EnvImporter - Perl extension for importing environment variable
Version:   1.01
Release:   1
Packager:  David Faraldo <dfaraldo@cpan.org>
License:   Artistic
Group:     Applications/CPAN
Url:       http://www.cpan.org
Buildroot: %{_tmppath}/%{name}-%{version}-%(id -u -n)
Buildarch: noarch
Prefix:    %(echo %{_prefix})
Source:    %{pkgname}-%{version}.tar.gz

%description
Shell::EnvImporter allows you to import environment variable changes
exported by an external script or command into the current environment.


%prep

# Unpack source tarball and make the files writable
%setup -q -c -n %{pkgname}-%{version} 
chmod -R u+w %{_builddir}/%{pkgname}-%{version}

%build
%{__perl} Makefile.PL DESTDIR=%{buildroot}
%{__make} 
%{__make} test

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%{makeinstall} DESTDIR=%{buildroot}

[ -x /usr/lib/rpm/brp-compress ] && /usr/lib/rpm/brp-compress

# remove special files
find %{buildroot} -name "perllocal.pod" \
    -o -name ".packlist"                \
    -o -name "*.bs"                     \
    |xargs -i rm -f {}

# no empty directories
find %{buildroot}%{_prefix}             \
    -type d -depth                      \
    -exec rmdir {} \; 2>/dev/null

%{__perl} -MFile::Find -le '
    find({ wanted => \&wanted, no_chdir => 1}, "%{buildroot}");
    print "%doc  Changes README";
    for my $x (sort @dirs, @files) {
        push @ret, $x unless indirs($x);
        }
    print join "\n", sort @ret;

    sub wanted {
        return if /auto$/;

        local $_ = $File::Find::name;
        my $f = $_; s|^\Q%{buildroot}\E||;
        return unless length;
        return $files[@files] = $_ if -f $f;

        $d = $_;
        /\Q$d\E/ && return for reverse sort @INC;
        $d =~ /\Q$_\E/ && return
            for qw|/etc %_prefix/man %_prefix/bin %_prefix/share|;

        $dirs[@dirs] = $_;
        }

    sub indirs {
        my $x = shift;
        $x =~ /^\Q$_\E\// && $x ne $_ && return 1 for @dirs;
        }
    ' > %filelist

[ -z %filelist ] && {
    echo "ERROR: empty %files listing"
    exit -1
    }

%clean

# Smoke the build root
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

# Smoke the build dir
/bin/rm -rf $RPM_BUILD_DIR/%{pkgname}-%{version}


%files -f %filelist
%defattr(-,root,root)

%changelog
* Tue Apr 5 2005 root@dhcp-101.localdomain
- Initial build.
