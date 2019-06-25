# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
    boxes = [
        {
            :name => "ubuntu-xenial",
            :box => "ubuntu/xenial64",
            :host_vars => {
                "ansible_python_interpreter" => "/usr/bin/python3"
            }
        }, {
            :name => "ubuntu-bionic",
            :box => "ubuntu/bionic64",
            :host_vars => {
                "ansible_python_interpreter" => "/usr/bin/python3"
            }
        }, {
            :name => "centos-7",
            :box => "centos/7",
            :host_vars => {}
        }
    ]
    host_vars = {}
    boxes.each do |opts|
        config.vm.define opts[:name] do |config|
            config.vm.box = opts[:box]
            config.vm.provider "virtualbox" do |vb|
                # Display the VirtualBox GUI when booting the machine
                vb.gui = true
                # Customize the amount of memory on the VM:
                vb.memory = "512"
            end
            host_vars[opts[:name]] = opts[:host_vars]
            if opts[:name] == boxes.last[:name]
                config.vm.provision "ansible" do |ansible|
                    ansible.playbook = "test.yml"
                    ansible.limit = "all"
                    ansible.host_vars = host_vars
                end
            end
        end
    end
end
