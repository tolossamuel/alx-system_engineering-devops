# The amount of traffic will increase as the Nginx server can handle.

# The ULIMIT of the default file will increase
exec { 'fix--for-nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
} ->

# Nginx Restart 
exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
