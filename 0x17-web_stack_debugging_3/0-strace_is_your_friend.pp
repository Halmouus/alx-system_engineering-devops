# Puppet manifest to fix the WordPress site by correcting a filename extension

exec { 'Fix wordpress site':
  command  => 'sed -i "s/.phpp/.php/" /var/www/html/wp-settings.php',
  path     => '/usr/local/bin/:/bin/'
  provider => shell,
}
