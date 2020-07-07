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

|percona| provides two repositories for |pdmdb|. We recommend to install |pdmdb|  from the *Major Release repository* (e.g. ``pdmdb-4.2``) as it includes the latest version packages. Whenever a package is updated, the package manager of your operating system detects that and prompts you to update. As long as you update all Distribution packages at the same time, you can ensure that the packages you're using have been tested and verified by |percona|. 

The *Minor Release repository* includes a particular minor release of the database and all of the packages that were tested and verified to work with that minor release (e.g. ``pdmdb-4.2.8``). You may choose to install |pdmdb| from the Minor Release repository if you have decided to standardize on a particular release which has passed rigorous testing procedures and which has been verified to work with your applications. This allows you to deploy to a new host and ensure that you'll be using the same version of all the Distribution packages, even if newer releases exist in other repositories.

The disadvantage of using a Minor Release repository is that you are locked in this particular release. When potentially critical fixes are released in a later minor version of the database, you will not be prompted for an upgrade by the package manager of your operating system. You would need to change the configured repository in order to install the upgrade.

----------

The installation of |pdmdb| includes the following steps:

#. Install the |percona-release| utility.
#. Set up the |Percona| repository for the required version of
   |pdmdb|.
#. Install the packages.

.. note::

   Run all commands as root or via |sudo| during the installation.

Install |percona-release|
==============================================

See the `Percona Software Repositories Documentation <https://www.percona.com/doc/percona-repo-config/percona-release.html#installation>`_
for installation instructions relevant to your operating system.

If you have previously installed |percona-release|, make sure it is `updated to the
latest version <https://www.percona.com/doc/percona-repo-config/percona-release.html#updating-percona-release-to-the-latest-version>`_.

Set up |Percona| repository
==============================================

As soon as |percona-release| is up-to-date, use the ``setup`` command to enable |Percona| repository for |pdmdb| (``pdmdb-4.2``). 

.. code-block:: bash

   $ sudo percona-release setup pdmdb-4.2

.. hint::

   To enable a minor version repository (e.g. pdmdb-4.2.8), use the following command:

   .. code-block:: bash
   
      $ sudo percona-release setup pdmdb-4.2.8
   
Install packages
==============================================

Install |pdmdb| components using the package manager of your operating system.

Install on *Debian / Ubuntu*
----------------------------------------------

Use the following commands to install |PSMDB| and / or
|PBM|:

.. code-block:: bash

   # Install the Percona Server for MongoDB package
   $ apt-get install percona-server-mongodb
   # Install the Percona Backup for MongoDB package
   $ apt-get install percona-backup-mongodb
   
   
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
	 
.. |version| replace:: 4.2.8

.. include:: .res/replace.txt
