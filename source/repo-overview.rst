.. _repo-overview:

Repository overview
===============================

|percona| provides two repositories for |pdmdb|:

.. list-table:: 
   :widths: auto
   :header-rows: 1

   * - Major release repository
     - Minor release repository
   * - **Major Release repository** (e.g. ``pdmdb-5.0``) includes the latest version packages. Whenever a package is updated, the package manager of your operating system detects that and prompts you to update. As long as you update all Distribution packages at the same time, you can ensure that the packages you're using have been tested and verified by |percona|.

       We recommend to install |pdmdb| from the *Major Release repository*
     - **Minor Release repository** includes a particular minor release of the database and all of the packages that were tested and verified to work with that minor release (e.g. ``pdmdb-5.0.9``). You may choose to install |pdmdb| from the Minor Release repository if you have decided to standardize on a particular release which has passed rigorous testing procedures and which has been verified to work with your applications. This allows you to deploy to a new host and ensure that you'll be using the same version of all the Distribution packages, even if newer releases exist in other repositories.


       The disadvantage of using a Minor Release repository is that you are locked in this particular release. When potentially critical fixes are released in a later minor version of the database, you will not be prompted for an upgrade by the package manager of your operating system. You would need to change the configured repository in order to install the upgrade.  


.. include:: .res/replace.txt
