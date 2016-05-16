# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.provision :shell, :path => "bootstrap.sh"

  config.vm.provider "virtualbox" do |v|
    # lxml needs more than 512MB of memory during compilation :-(
    v.memory = 1024
  end

  if Vagrant.has_plugin?("vagrant-multi-putty")
    # For Windows users with putty, this allows you to specify a putty profile (with 
    # keybindings, port forwarding, terminal config etc) and apply it to any putty
    # connections to this VM. By convention, the profile should be called vagrant-default
    puts "Putty plugin detected - setting default profile"
    config.putty.session = "vagrant-default"
  end
end
