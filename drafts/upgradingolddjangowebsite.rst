Django Upgrade ⌨️
#################################################

:date: 2023-09-09 02:12
:modified: 2023-11-03 00:33
:tags: django, python
:category: Configuration
:slug: django-upgrade
:authors: Ishaan Arora
:summary: Mapping keys and a little bit about how keyboards work

Context
****************

You can assume that since the current project is working fine, the current dependecies don't have any issues
Use it as the min version, and look for changes in the Changelog

Sometimes Changelog is not enough

use git diff
usually projects also tag the release version in git

.. code:: sh

   $ git tag # shows a list of tags, good idea to pipe it to less
   $ git diff 4.6.0..4.12.2

Read the changelog

Learn about the usage of dependencies in your project.
I usually just do 

.. code:: sh

   $ grep -Rn bs4 --exclude-dir=pythonenv/


If changelog good, then fine, no need for code diff

Observations:
- lot of deps started using GH Actions
- a few of them started shipping tests in release tarballs

This part is just the homework, no guarantee that this will work. Now 

Setting up VMs
---------------
Used the libvirt stack

.. code:: sh

   $ virt-install --name rhel7.9 --memory 2048 --vcpus=2,maxvcpus=4 --location /home/pulsar17/Downloads/rhel-server-7.9-x86_64-dvd.iso --disk size=20,format=qcow2 --virt-type kvm --cpu host --graphics none --extra-args="console=tty0 console=ttyS0,115200"

.. tip:: 

   These virt-install cmds tend to be a little long
   Use Ctrl-X Ctrl-E if you're on bash, that will launch your editor, much like when you do ``git commit``. Gotta love the consistency.


https://access.redhat.com/solutions/253273

.. code:: sh

   Registering to: subscription.rhsm.redhat.com:443/subscription
   The system has been registered with ID: 962d93f1-c2b4-45af-97ea-37d24e9536ca
   The registered system name is: earth99
   Installed Product Current Status:
   Product Name: Red Hat Enterprise Linux Server
   Status:       Subscribed


https://yum.postgresql.org/repopackages/#pgredhatoldrepos

Installed postgres from custom repo, and nginx from SCL, python from RHEL repo
