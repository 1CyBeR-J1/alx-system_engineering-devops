# install flask from pip3 with certain requirement
package {'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
