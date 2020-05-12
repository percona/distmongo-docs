.. _install:


=============================================     
Installing |pdmdb|
=============================================

.. contents::
   :local:

Percona provides installation packages for the |pdmdb|
in |deb| and |rpm| formats for the most 64-bit Linux distributions.

.. list-table:: 
   :widths: 100 
   :header-rows: 1

   * - Supported Distributions
   * - * Debian 9 (stretch)
       * Debian 10 (buster)
       * Ubuntu 16.04 (Xenial Xerus)
       * Ubuntu 18.04 LTS (Bionic Beaver)
       * Ubuntu 20.04 (Focal Fossa)
   * - * Red Hat Enterprise Linux / CentOS 6
       * Red Hat Enterprise Linux / CentOS 7
       * Red Hat Enterprise Linux / CentOS 8

|pdmdb| is installed using the |percona-release| utility.
This is the most straightforward way since |percona-release|
enables the required repositories for you.

The installation of |pdmdb| includes the following steps:

#. Install the |percona-release| utility.
#. Set up the |Percona| repository for the required version of
   |pdmdb|.
#. Install the packages.

.. note::

   Make sure to run all commands as root or via |sudo| during the installation.

Install |percona-release|
==============================================

See the `percona-release documentation
<https://www.percona.com/doc/percona-repo-config/percona-release.html#installation>`_
for installation instructions relevant to your operating system.

If you have previously installed |percona-release|, make sure to update it to the
latest version. Refer to the `percona-release documentation
<https://www.percona.com/doc/percona-repo-config/percona-release.html#updating-percona-release-to-the-latest-version>`_
for details.

Set up |Percona| repository
==============================================

As soon as |percona-release| is up-to-date, set up |Percona| repository for the
required version of |pdmdb| (``pdmdb<version>``). For example, to set up |pdmdb|
4.2.6, use the following command:

.. code-block:: bash

   $ percona-release setup pdmdb4.2.6

   
Install packages
==============================================

Install |pdmdb| components using the package manager of your operating system.

Install on *Debian / Ubuntu*
----------------------------------------------

Use the following commands to install |PSMDB| and /or
|PBM|:

.. code-block:: bash

   # Update the local cache
   $ apt-get update
   # Install the Percona Server for MongoDB package
   $ apt install percona-server-mongodb
   # Install the Percona Backup for MongoDB package
   $ apt install percona-backup-mongodb
   
   
.. seealso::

      * Installing |PSMDB|
	   https://www.percona.com/doc/percona-server-for-mongodb/4.2/install/apt.html
      * Installing |PBM|
	   https://www.percona.com/doc/percona-backup-mongodb/installation.html#installing-pbm-using-apt
    
Install on  *Red Hat Enterprise Linux / CentOS*
-------------------------------------------------

Use the following commands to install |PSMDB| and /or
|PBM|:

.. code-block:: bash

   # Install the Percona Server for MongoDB package
   $ yum install percona-server-mongodb
   # Install the Percona Backup for MongoDB package
   $ yum install percona-backup-mongodb

.. seealso::

      * Installing |PSMDB|
	   https://www.percona.com/doc/percona-server-for-mongodb/4.2/install/yum.html#uninstalling-percona-server-for-mongodb
      * Installing |PBM|
	   https://www.percona.com/doc/percona-backup-mongodb/installation.html#installing-pbm-using-yum  

Uninstalling |pdmdb|
==============================================

To uninstall |pdmdb|, remove the packages using the package manager of your
operation system. Optionally, disable |Percona| repository.

.. seealso::

   Uninstalling |PSMDB|:
       
   * `on Debian or Ubuntu
     <https://www.percona.com/doc/percona-server-for-mongodb/4.2/install/apt.html#uninstalling-percona-server-for-mongodb>`_
   * `on RHEL or CentOS
     <https://www.percona.com/doc/percona-server-for-mongodb/4.2/install/yum.html#uninstalling-percona-server-for-mongodb>`_

   Uninstalling |PBM|
      https://www.percona.com/doc/percona-backup-mongodb/uninstalling.html
	 
.. include:: .res/replace.txt
