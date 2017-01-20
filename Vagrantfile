# -*- mode: ruby -*-
# vi: set ft=ruby :

$script = <<SCRIPT
#!/bin/bash
apt-get update -y && apt-get upgrade -y
# install python3-venv
# install python 
SCRIPT

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/xenial64"
  config.vm.provision :shell, inline: $script
  config.vm.network "forwarded_port", guest:8080, host:18080
end
