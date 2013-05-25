class requirements {
  group { "puppet": ensure => "present", }
  exec { "apt-update":
    command => "/usr/bin/apt-get -y update"
  }

  package {
    ["python", "build-essential", "python-dev", "virtualenvwrapper", "language-pack-en", "postgresql", "sqlite", "postgresql-client", "libpq-dev", "git-core", "libgdbm-dev", "libncurses5-dev", "libtool", "pkg-config", "libffi-dev"]:
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

  exec { 'virtualenv NHSHD':
    command => '/usr/bin/virtualenv NHSHD',
    cwd => '/home/vagrant',
    logoutput => true;
  }

  exec { '/usr/bin/pip':
    command => '/usr/bin/pip install -r /mnt/nhsdating/requirements.txt',
    cwd => '/mnt/nhsdating',
    logoutput => true;
  }

  exec { 'python manage.py runserver':
    command => '/usr/bin/python manage.py runserver 192.168.33.10:80 &',
    cwd => '/mnt/nhsdating',
    logoutput => true;
  }
}

class doinstall {
  include requirements
  include createdb
  include startapp

  Class['requirements'] -> Class['createdb'] -> Class['startapp']
}

include doinstall
