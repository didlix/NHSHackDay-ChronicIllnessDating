stage { 'req-install': before => Stage['rvm-install'] }

class requirements {
  group { "puppet": ensure => "present", }
  exec { "apt-update":
    command => "/usr/bin/apt-get -y update"
  }

  package {
    ["python", "language-pack-en", "postgresql", "sqllite" "postgresql-client", "libpq-dev", "git-core", "libgdbm-dev", "libncurses5-dev", "libtool", "pkg-config", "libffi-dev"]:
      ensure => installed, require => Exec['apt-update']
  }
}

class createdb {

  include postgresql::server
  postgresql::db{ 'nhshd':
    user          => 'nhshd',
    password      => 'nhshd',
    grant         => 'all',
  }
}

class startapp {

  exec { 'mkvirtualenv NHSHD':
    command => 'mkvirtualenv NHSHD',
    cwd => '/mnt/NHSHD',
    logoutput => true;
  }

  exec { 'workon NHSHD':
    command => 'workon NHSHD',
    cwd => '/mnt/NHSHD',
    logoutput => true;
  }

  exec { 'python manage.py runserver':
    command => 'python manage.py runserver',
    cwd => '/mnt/NHSHD',
    logoutput => true;
  }
}

class doinstall {
  include requirements
  include createdb
  include installapp
  include bundleinstall
  include startapp

  Class['requirements'] -> Class['createdb'] -> Class['startapp']
}

include doinstall
