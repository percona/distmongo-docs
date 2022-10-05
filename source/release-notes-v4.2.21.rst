.. _DISTMONGO-4.2.21:

================================================================================
*Percona Distribution for MongoDB* 4.2.21 (2022-06-29)
================================================================================

:Date: June 29, 2022
:Installation: :ref:`install`

|pdmdb| is a collection of solutions to run and operate your
|mongodb| efficiently with the data being consistently backed up.  

|pdmdb| includes the following components:

* |PSMDB| is a fully compatible source-available, drop-in replacement
  for MongoDB.
* |pbm| is a distributed, low-impact solution for achieving
  consistent backups of |mongodb| sharded clusters and replica sets.

This release of |pdmdb| is based on `Percona Server for MongoDB 4.2.21-21 <https://www.percona.com/doc/percona-server-for-mongodb/4.2/release_notes/4.2.21-21.html>`_ and `Percona Backup for MongoDB 1.8.0 <https://www.percona.com/doc/percona-backup-mongodb/release-notes/1.8.0.html>`_. 	


Release Highlights
===================

* This release of Percona Distribution for MongoDB provides the following improvements to the data-at-rest encryption using the Key Management Interoperability Protocol (KMIP) (tech preview feature):

  * the `support of multiple KMIP servers <https://docs.percona.com/percona-server-for-mongodb/5.0/kmip.html#kmip>`_ as the failover to your setup
  * the ability to set KMIP client certificate passwords through a flag to simplify the migration from MongoDB Enterprise to |PSMDB|

* Added support for Ubuntu 22.04 for |PSMDB| and |PBM|.
  
The bug fixes, provided by MongoDB and included in Percona Server for MongoDB 4.2.20-20 and |pdmdb| 4.2.20 are the following:

* Extended the ``getParameter`` command output with the information about a parameter to be enabled on runtime or only on startup
* Ensured that applying schema validation rules to a non-empty collection prevents chunk migration for the data that existed before these rules were applied.
* Improved the ``CollectionCatalog`` workflow by making hashing before taking a lock and adding an API for restoring after yield.
* Fixed the issue with cache eviction causing deadlocks by allowing a transaction to time itself out 
   

|PBM| 1.8.0 improvements include the following:

* Ability to `restore data to a replica set with a different name and configuration <https://docs.percona.com/percona-backup-mongodb/running.html#pbm-restore-new-env>`_. This extends the list of environments compatible for the restore.
* When you use EBS-snapshots or other tools for physical backups, you `no longer have to create a mandatory base backup snapshot in Percona Backup for MongoDB as the starting point for Point-in-Time Recovery oplog slicing <https://docs.percona.com/percona-backup-mongodb/configuration-options.html#pitr-oplog-only>`_. This reduces time and effort on managing excessive backups and makes Point-in-time recovery from physical or storage-level backups more straightforward.
* The ability to wait for the backup operation to finish before doing further actions through the session lock. This simplifies the automation of operations with |PBM|.
* Ability to define backup compression level and method in |PBM| configuration.  
* To simplify the |PBM| configuration, the example configuration file is now included in the |PBM| package. 

.. include:: .res/replace.txt
