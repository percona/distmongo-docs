.. _DISTMONGO-5.0.9:

================================================================================
*Percona Distribution for MongoDB* 5.0.9 (2022-06-20)
================================================================================

:Date: |date|
:Installation: :ref:`install`

.. warning::

   We don't recommend this version for the production use due to the critical issue with sharding metadata inconsistency: `SERVER-68511 <https://jira.mongodb.org/browse/SERVER-68511>`_. The metadata inconsistency is observed when running the ``movePrimary`` command on the database that has the Feature Compatibility Version (FCV) set to 4.4 or earlier. Affects MongoDB versions 5.0.0 through 5.0.10 and MongoDB 6.0.0. Upgrade to the fixed version of MongoDB 5.0.11 / Percona Server for MongoDB 5.0.11-10 or |pdmdb| 5.0.11 as soon as possible.

   Please follow closely the upstream recommendations outlined in `SERVER-68511 <https://jira.mongodb.org/browse/SERVER-68511>`_ to work around this issue and for the remediation steps, if your cluster is affected.

Percona Distribution for MongoDB is a freely available MongoDB database alternative, giving you a single solution that combines enterprise components from the open source community, designed and tested to work together. The aim of Percona Distribution for MongoDB is to enable you to run and operate your
|mongodb| efficiently with the data being consistently backed up.

|pdmdb| includes the following components:

* |PSMDB| is a fully compatible open source, drop-in replacement
  for MongoDB.
* |pbm| is a distributed, low-impact solution for achieving
  consistent backups of |mongodb| sharded clusters and replica sets.

This release of |pdmdb| is based on `Percona Server for MongoDB 5.0.9-8 <https://www.percona.com/doc/percona-server-for-mongodb/5.0/release_notes/5.0.9-8.html>`_ and `Percona Backup for MongoDB 1.8.0 <https://www.percona.com/doc/percona-backup-mongodb/release-notes/1.8.0.html>`_.

Release Highlights
==================

* This release of Percona Distribution for MongoDB provides the following improvements to the data-at-rest encryption using the Keys Management Interoperability Protocol (KMIP) (tech preview feature):

  * the `support of multiple KMIP servers <https://docs.percona.com/percona-server-for-mongodb/5.0/kmip.html#kmip>`_ as the failover to your setup
  * the ability to set KMIP client certificate passwords through a flag to simplify the migration from MongoDB Enterprise to |PSMDB|

* Added support for Ubuntu 22.04 for |PSMDB| and |PBM|.
* Added improvements to initial syncs from a secondary sync source.
  
The bug fixes, provided by MongoDB and included in Percona Server for MongoDB and |pdmdb| are the following:

* Detect namespace changes when refreshing Collection after yielding to maintain data consistency and avoid stale catalogs.
* Fixed the issue with releasing the critical state too early when sharding an empty collection. This could result in unwanted writes to that collection.
* Fixed the wrong key/value returning during search near when the key doesn't exist
  
|PBM| 1.8.0 improvements include the following:

* Ability to `restore data to a replica set with a different name and configuration <https://docs.percona.com/percona-backup-mongodb/running.html#pbm-restore-new-env>`_. This extends the list of environments compatible for the restore.
* When you use EBS-snapshots or other tools for physical backups, you `no longer have to create a mandatory base backup snapshot in Percona Backup for MongoDB as the starting point for Point-in-Time Recovery oplog slicing <https://docs.percona.com/percona-backup-mongodb/configuration-options.html#pitr-oplog-only>`_. This reduces time and effort on managing excessive backups and makes Point-in-time recovery from physical or storage-level backups more straightforward.
* The ability to wait for the backup operation to finish before doing further actions through the session lock. This simplifies the automation of operations with |PBM|.
* Ability to define backup compression level and method in |PBM| configuration.  
* To simplify the |PBM| configuration, the example configuration file is now included in the |PBM| package. 

.. |date| replace:: June 20, 2022
.. include:: .res/replace.txt