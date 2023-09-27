# Install Nginx using puppet

package { 'nginx':
  ensure => 'installed',
}

service { 'nginx':
  ensure => 'running',
  enable => true,
  require => Package['nginx'],
}

file { '/etc/nginx/sites-available/default':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  line   => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
  after  => 'listen 80 default_server;',
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
}

exec { 'append_redirect_me':
  command => "/usr/bin/sed -i '/^}$/i \\\n\tlocation \\/redirect_me {return 301 https:\\/\\/www.youtube.com\\/watch?v=QH2-TGUlwu4;}' /etc/nginx/sites-available/default",
}
