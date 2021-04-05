# Puppet manifest to set up client SSH configuration
file_line {'no authorized password':
  ensure  => 'present',
  path    => '~/.ssh/config',
  line    => 'PasswordAuthentication no',
}
file_line {'file_identity':
  ensure  => 'present',
  path    => '~/.ssh/config',
  line    => 'IdentityFile ~/.ssh/holberton',
}
