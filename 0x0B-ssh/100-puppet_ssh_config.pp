# Puppet manifest to set up client SSH configuration
file {'~/.ssh/config':
  ensure  => present,
  replace => 'yes',
  path    => '~/.ssh/config',
  content => 'Host *
     HostName 34.74.115.197
     User ubuntu
     IdentityFile ~/.ssh/holberton',
  mode    => '7000',
}
