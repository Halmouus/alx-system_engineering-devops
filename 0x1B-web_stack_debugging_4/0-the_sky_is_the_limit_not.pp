# Fix the stack to reduce failed requests to 0

# Fix the stack limit
exec { 'fix_stack_limit':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}

# restart Nginx
exec { 'nginx_restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}