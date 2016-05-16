# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "ubuntu/wily64"

  config.vm.provision "ansible_local" do |ansible|
    ansible.verbose = "v"
    ansible.install = true
    ansible.galaxy_role_file = "requirements.yml"
    ansible.playbook = "playbook.yml"
  end

  config.vm.provider "virtualbox" do |v|
    # lxml needs more than 512MB of memory during compilation
    v.memory = 1024
  end

#  config.vm.box = "ubuntu/trusty64"
#  config.vm.provision :shell, :path => "bootstrap.sh"
  config.vm.network "private_network", ip: "192.168.61.101"

  if Vagrant.has_plugin?("vagrant-multi-putty")
    # For Windows users with putty, this allows you to specify a putty profile (with 
    # keybindings, port forwarding, terminal config etc) and apply it to any putty
    # connections to this VM. By convention, the profile should be called vagrant-default
    puts "Putty plugin detected - setting default profile"
    config.putty.session = "vagrant-default"
  end
end
