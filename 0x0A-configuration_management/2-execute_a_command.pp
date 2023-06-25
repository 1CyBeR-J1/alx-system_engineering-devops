# create a manifest that kills a process named killmenow using puppet
exec {'killmenow':
  command => 'pkill -f killmenow',
  path    => '/usr/bin:/bin:/usr/sbin:/sbin',
}
