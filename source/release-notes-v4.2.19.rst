.. _DISTMONGO-4.2.19:

================================================================================
*Percona Distribution for MongoDB* 4.2.19
================================================================================

:Date: March 29, 2022
:Installation: :ref:`install`

|pdmdb| is a collection of solutions to run and operate your
|mongodb| efficiently with the data being consistently backed up.  

|pdmdb| includes the following components:

* |PSMDB| is a fully compatible source-available, drop-in replacement
  for MongoDB.
* |pbm| is a distributed, low-impact solution for achieving
  consistent backups of |mongodb| sharded clusters and replica sets.

This release of |pdmdb| is based on `Percona Server for MongoDB 4.2.19-19 <https://www.percona.com/doc/percona-server-for-mongodb/4.2/release_notes/4.2.19-19.html>`_ and `Percona Backup for MongoDB 1.6.1 <https://www.percona.com/doc/percona-backup-mongodb/release-notes/1.6.1.html>`_. 	

Release Highlights
===================

The bug fixes, provided by MongoDB and included in Percona Server for MongoDB 4.2.19-19 and |pdmdb| 4.2.19 are the following:

* Support of :ref:`Keys Management Interoperability Protocol (KMIP) <kmip>`. Thus, users can store encryption keys in their favorite KMIP-compatible key manager to set up encryption at rest. This is a tech preview feature. 
* Added the ``repairShardedCollectionChunksHistory`` command to restore history fields for some chunks. This aims to fix broken snapshot reads and distributed transactions.
* Fixed an issue with transaction coordinator crashing if the transaction is aborted when attempting to commit a transaction.
* Fixed the issue with the distributed transactions being in the prolonged prepared state that was caused by the  blocking of acquiring the WiredTiger write tickets by the transaction coordinator.
* Fixed an issue with an empty array for the ``$nin`` statement.



.. include:: .res/replace.txt
