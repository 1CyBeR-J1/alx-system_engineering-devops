#fix a 500 error on Apache automated by using puppet
#
exec { 'fix-apache':
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path    => ['/bin','/usr/bin', '/usr/sbin']
}
