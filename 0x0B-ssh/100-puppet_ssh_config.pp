# Puppet manifest to set up client SSH configuration
file {'~/.ssh/config':
  ensure  => present,
  replace => 'yes',
  path    => '~/.ssh/config',
  content => 'Host *
     HostName 34.75.232.120
     User ubuntu
     IdentityFile ~/.ssh/holberton',
  mode    => '7000',
}
