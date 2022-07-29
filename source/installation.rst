.. _install:

=============================================     
Install |pdmdb|
=============================================

We recommend to install |pdmdb| from Percona repositories using the package manager of your operating system. Find the list of supported Linux distributions on the `Percona Software and Platform Lifecycle <https://www.percona.com/services/policies/percona-software-platform-lifecycle#mongodb>`_ page.

Alternatively, you can download |pdmdb| from Percona website and install it manually from binary tarballs. 

Choose how you wish to install |pdmdb|:

.. tabs:: 
 
   .. tab:: On Debian / Ubuntu

      |tip.run-all.root|

      1. Install |percona-release|
         
         Install the |percona-release| repository management tool to subscribe to Percona repositories:

         * Install ``curl``:
           
           .. code-block:: bash

              $ sudo apt update
              $ sudo apt install curl 

         * Download the |percona-release| package
           
           .. code-block:: bash

              $ curl -O https://repo.percona.com/apt/percona-release_latest.generic_all.deb
         
         * Install the package and dependancies
           
           .. code-block:: bash 

              $ sudo apt install gnupg2 lsb-release ./percona-release_latest.generic_all.deb

         * Refresh the local cache

           .. code-block:: bash

              $ supo apt update

      #. Enable the repository
         
         Percona provides :ref:`two repositories <repo-overview>` for |pdmdb|. To enable a repo, we recommend using the ``setup`` command:

         .. code-block:: bash

            $ sudo percona-release setup pdmdb-4.4

      #. Install |pdmdb| packages:
         
         .. code-block:: bash

            $ sudo apt install percona-server-mongodb percona-backup-mongodb

   .. tab:: On RHEL / derivatives

      |tip.run-all.root|

      1. Install |percona-release|
         
         Install the |percona-release| repository management tool to subscribe to Percona repositories:
         
         .. code-block:: bash

            $ sudo yum install -y https://repo.percona.com/yum/percona-release-latest.noarch.rpm
         
      #. Enable the repository 
         
         Percona provides :ref:`two repositories <repo-overview>` for |pdmdb|. To enable a repo, we recommend using the ``setup`` command:

         .. code-block:: bash

            $ sudo percona-release setup pdmdb-4.4

      #. Install |pdmdb| packages
         
         .. code-block:: bash

            $ sudo yum install percona-server-mongodb percona-backup-mongodb

   .. tab:: From tarballs

      You can find binary tarbals on the `Percona software downloads page <https://www.percona.com/downloads/percona-distribution-mongodb-4.4/LATEST/>`_

      1. Select *Generic Linux* from the dropdown.
      2. Download binary tarballs.  Replace the ``<version>`` variable with the desired version:
         
         .. code-block:: bash 

            $ wget https://downloads.percona.com/downloads/percona-distribution-mongodb-4.4/percona-distribution-mongodb-<version>/binary/tarball/percona-backup-mongodb-<version>-x86_64.tar.gz 
            $ wget https://downloads.percona.com/downloads/percona-distribution-mongodb-4.4/percona-distribution-mongodb-<version>/binary/tarball/percona-server-mongodb-<version>-x86_64.glibc2.17.tar.gz

      #. Extract the tarballs
         
         .. code-block:: bash

            $ tar -xf percona-backup-mongodb-<version>-x86_64.tar.gz 
            $ tar -xf percona-server-mongodb-<version>-x86_64.glibc2.17.tar.gz

      #. Export the location of the binaries to the PATH variable

         For example, if you’ve extracted the tarballs to your home directory, the commands would be the following:

         .. code-block:: bash

            $ export PATH=~/percona-backup-mongodb-<version>/:~/percona-server-mongodb-<version>/:$PATH

      #. Create the default data directory for |PSMDB|:
         
         .. code-block:: bash

            $ sudo mkdir -p /data/db

      #. Check that you have read and write permissions for the data directory and run ``mongod``.
         
   .. tab:: On Kubernetes

      Deploy and run |pdmdb| on Kubernetes with `Percona Operator for MongoDB <https://www.percona.com/software/percona-kubernetes-operators>`_. See `Quickstart guides <https://www.percona.com/doc/kubernetes-operator-for-psmongodb/index.html#quickstart-guides>`_ for the installation instructions on your favorite Kubernetes flavor.

To set up monitoring of your |pdmdb| in PMM, see `Set up PMM to monitor MongoDB <https://docs.percona.com/percona-monitoring-and-management/setting-up/client/mongodb.html>`_ 

Uninstall |pdmdb|
==============================================

To uninstall |pdmdb|, remove the packages using the package manager of your
operation system. Optionally, disable |Percona| repository.

.. seealso::

   Uninstalling |PSMDB|:       
      * `on Debian or Ubuntu <https://www.percona.com/doc/percona-server-for-mongodb/4.4/install/uninstall.html#apt-uninstall>`_
      * `on RHEL or CentOS <https://www.percona.com/doc/percona-server-for-mongodb/4.4/install/uninstall.html#yum-uninstall>`_

   `Uninstalling Percona Backup for MongoDB <https://www.percona.com/doc/percona-backup-mongodb/uninstalling.html>`_
	 

.. include:: .res/replace.txt
