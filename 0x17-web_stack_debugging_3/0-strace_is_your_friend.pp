# replacing 'phpp' typo with 'php' in the file /var/www/html/wp-settings

exec {
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
