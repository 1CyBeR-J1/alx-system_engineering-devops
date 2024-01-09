#puppet manifest

package { 'nginx':
# Install Nginx package
package { 'nginx':
	ensure => installed,
}

# Configure Nginx
file { '/etc/nginx/sites-available/default':
	ensure => file,
	content => "
    server {
	listen 80 default_server;
	listen [::]:80 default_server;
	root /var/www/html;
	index index.html index.htm index.nginx-debian.html;

	server_name _;
		
	add_header X-served-By $HOSTNAME;
		
	location /redirect_me {
		return 301 https://github.com/1CyBeR-J1;
	}
    }
  ",
  notify => Service['nginx'],
}

# Ensure Nginx service is running and enabled
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}
