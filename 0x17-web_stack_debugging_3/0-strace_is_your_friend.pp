# Puppet manifest to fix the WordPress site by correcting a filename extension

exec { 'fix wordpress site':
  command  => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path     => '/usr/local/bin/:/bin/',
  provider => shell,
}
