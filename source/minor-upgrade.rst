.. _minor-upgrade:

================================================================================
Minor upgrade of |pdmdb|
================================================================================

To receive bug fixes and feature enhancements that come with minor releases, keep your |pdmdb| upgraded to the latest version.

Before the upgrade, we recommend to back up your data in order to be on the safe side if anything goes wrong.

Similar to installing, |pdmdb| is upgraded from |percona| repositories using the |percona-release| utility. Update |percona-release| to the latest version using `these instructions <https://www.percona.com/doc/percona-repo-config/percona-release.html#updating-percona-release-to-the-latest-version>`_. This is required to install new version packages of |pdmdb|. 

|tip.run-all.root| 

The upgrade procedure includes the following steps:

Enable |percona| repository
==========================================================================

If you installed |pdmdb| from the Major release repository, this step is optional. This repository automatically includes new version packages and you receive a prompt for an upgrade from the package manager of your operating system.

If you installed |pdmdb| from the Minor release repository, you must enable the new version repository (e.g. ``pdmdb-5.0.1``) to upgrade. We recommend to use the ``setup`` subcommand:

.. code-block:: bash
 
   $ sudo percona-release setup pdmdb-5.0.1

.. seealso::

   :ref:`install`

Stop the service
===========================================================================

Stop |PSMDB|:

.. code-block:: bash

   $ systemctl mongod stop

Stop |pbm-agent|:

.. code-block:: bash

  $ systmectl pbm-agent stop

Install new version packages
===========================================================================

Install |PSMDB| and |PBM| using the package manager of your operating system. Please refer to the :ref:`pdmdb-install` section for the corresponding installation instructions.

Restart the service
===========================================================================

Start |PSMDB|:

.. code-block:: bash

   $ systemctl mongod start

Start |pbm-agent|:

.. code-block:: bash

  $ systmectl pbm-agent start


.. include:: .res/replace.txt