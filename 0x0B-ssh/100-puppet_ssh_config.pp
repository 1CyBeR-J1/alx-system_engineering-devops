#Making changes to Config File using Puppet

file_line { 'Turn off passwd auth':
  path  => '/etc/ssh/ssh_config',
  line  => '	PasswordAuthentication no',
  match => 'present',
}

file_line { 'Declare identity file':
  path  => '/etc/ssh/ssh_config',
  line  => '	IdentityFile ~/.ssh/school',
  match => 'present',
}
