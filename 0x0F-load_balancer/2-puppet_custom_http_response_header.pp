# Setup New Ubuntu server with nginx
# and add a custom HTTP header

# Update system packages
exec { 'update system':
    command => '/usr/bin/apt-get update',
}

# Install nginx package
package { 'nginx':
    ensure => 'installed',
    require => Exec['update system']
}

# Create a simple HTML file
file {'/var/www/html/index.html':
    content => 'Hello World!'
}

# Configure nginx to redirect requests and add a custom HTTP header
exec {'redirect_me':
    command => 'sed -i "24i\    rewrite ^/redirect_me https://th3-gr00t.tk/ permanent;" /etc/nginx/sites-available/default',
    provider => 'shell'
}

exec {'HTTP header':
    command => 'sed -i "25i\    add_header X-Served-By \$hostname;" /etc/nginx/sites-available/default',
    provider => 'shell'
}

# Ensure nginx service is running
service {'nginx':
    ensure => running,
    require => Package['nginx']
}
