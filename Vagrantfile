# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/focal64"

  config.vm.box_check_update = false

  config.vm.provider "virtualbox" do |v|
    v.memory = 4096
    v.cpus = 1
  end

  config.vm.define "kube1" do |kube1|
    kube1.vm.hostname = 'kube1'
    kube1.vm.network "private_network", ip: "192.168.20.10"
    kube1.vm.network "forwarded_port", guest: 80, host: 80
  end

  config.vm.define "kube2" do |kube2|
    kube2.vm.hostname = 'kube2'
    kube2.vm.network "private_network", ip: "192.168.20.20"
    kube2.vm.network "forwarded_port", guest: 80, host: 8080
  end

  config.vm.define "kube3" do |kube3|
    kube3.vm.hostname = 'kube3'
    kube3.vm.network "private_network", ip: "192.168.20.30"
    kube3.vm.network "forwarded_port", guest: 80, host: 8090
  end

  config.vm.define "test" do |test|
    test.vm.hostname = 'test'
    test.vm.network "private_network", ip: "192.168.20.40"
    test.vm.network "forwarded_port", guest: 80, host: 8095
  end
  
end
