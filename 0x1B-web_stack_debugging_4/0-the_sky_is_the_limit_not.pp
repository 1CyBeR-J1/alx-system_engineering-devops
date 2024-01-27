#puppet script to debug server with failed requests

exec { 'fix server':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}

# Restart Nginx
-> exec { 'nginx restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
