use 5.008003;
use ExtUtils::MakeMaker;
# See lib/ExtUtils/MakeMaker.pm for details of how to influence
# the contents of the Makefile that is written.
WriteMakefile(
    NAME              => 'Shell::EnvImporter',
    VERSION_FROM      => 'lib/Shell/EnvImporter.pm', # finds $VERSION
    PREREQ_PM         => {}, # e.g., Module::Name => 1.1
    ABSTRACT          => 'Perl extension for importing environment variable changes from external commands or shell scripts',
    ($] >= 5.005 ?     ## Add these new keywords supported since 5.005
      (AUTHOR         => 'David Faraldo <dfaraldo@cpan.org>') : ()
    ),
);
