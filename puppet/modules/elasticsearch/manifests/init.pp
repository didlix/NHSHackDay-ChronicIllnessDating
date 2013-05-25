class elasticsearch {
  $pkg  = "elasticsearch"
  $ver  = "0.90.0"
  $full = "${$pkg}-${$ver}"

  exec { "download-elasticsearch":
    command => "wget http://download.elasticsearch.org/$pkg/$pkg/$full.deb -O /tmp/$full.deb --no-check-certificate",
    unless => "test -f /tmp/$full.deb"
  }

  package { "default-jre": }

  package { "elasticsearch":
    provider => dpkg,
    ensure   => latest,
    source   => "/tmp/$full.deb",
    require  => [
      Package["default-jre"],
      Exec["download-elasticsearch"],
    ]
  }

  service { "elasticsearch":
    enable  => true,
    ensure  => running,
    require => Package["elasticsearch"]
  }
}
