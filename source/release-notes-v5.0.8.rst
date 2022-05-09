.. _DISTMONGO-5.0.8:

================================================================================
*Percona Distribution for MongoDB* 5.0.8
================================================================================

:Date: May 10, 2022
:Installation: `Installing Percona Distribution for MongoDB <https://www.percona.com/doc/percona-distribution-for-mongodb/5.0/installation.html>`_

Percona Distribution for MongoDB is a freely available MongoDB database alternative, giving you a single solution that combines enterprise components from the open source community, designed and tested to work together. The aim of Percona Distribution for MongoDB is to enable you to run and operate your
|mongodb| efficiently with the data being consistently backed up.

|pdmdb| includes the following components:

* |PSMDB| is a fully compatible open source, drop-in replacement
  for MongoDB.
* |pbm| is a distributed, low-impact solution for achieving
  consistent backups of |mongodb| sharded clusters and replica sets.

This release of |pdmdb| is based on `Percona Server for MongoDB 5.0.8-7 <https://www.percona.com/doc/percona-server-for-mongodb/5.0/release_notes/5.0.8-7.html>`_ and `Percona Backup for MongoDB 1.7.0 <https://www.percona.com/doc/percona-backup-mongodb/release-notes/1.7.0.html>`_.

Release Highlights
==================

This release of Percona Distribution for MongoDB includes the support of master key rotation for data encrypted using the Keys Management Interoperability Protocol (KMIP) (tech preview feature). Thus, users can comply with regulatory standards for data security. 

The most notable bug fixes, provided by MongoDB and included in Percona Server for MongoDB are the following:

* Fixed a bug that causes replication to stall on secondary replica set members in a sharded cluster handling cross-shard transactions. It is caused by WiredTger to erroneously return a write conflict when deciding if an update to a record is allowed. If MongoDB decides to retry the operation that caused the conflict in WiredTiger, it will enter an indefinite retry loop, and oplog application will stall on secondary nodes.

  If this bug is hit, the secondary nodes will experience indefinite growth in replication lag. Restart the secondary nodes to resume replication.

  This bug affects MongoDB 4.4.10 through 4.4.13 and 5.0.4 to 5.0.7.
  
  Update to the latest version to avoid the secondary replication stall and lag issues.

* Fixed the issue with a commitQuorum incorrectly allowing non-voting buildIndexes:false nodes to be included in the commitQuorum count. It also fixed an error message relating to data-bearing nodes and quorum regarding to non-voting nodes.
* Fixed the order of backup blocks returned to the user to match the order retrieved from WiredTiger.
* Fixed the issue reporting an incorrect number of documents deleted from a capped collection when utilizing a collection scan to perform the delete action.


.. include:: .res/replace.txt