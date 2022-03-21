.. _DISTMONGO-4.4.13:

================================================================================
*Percona Distribution for MongoDB* 4.4.13
================================================================================

:Date: March 23, 2022
:Installation: `Installing Percona Distribution for MongoDB <https://www.percona.com/doc/percona-distribution-for-mongodb/4.4/installation.html>`_

Percona Distribution for MongoDB is a freely available MongoDB database alternative, giving you a single solution that combines enterprise components from the open source community, designed and tested to work together. The aim of Percona Distribution for MongoDB is to enable you to run and operate your
|mongodb| efficiently with the data being consistently backed up.

|pdmdb| includes the following components:

* |PSMDB| is a fully compatible open source, drop-in replacement
  for MongoDB.
* |pbm| is a distributed, low-impact solution for achieving
  consistent backups of |mongodb| sharded clusters and replica sets.

This release of |pdmdb| is based on `Percona Server for MongoDB 4.4.13-13 <https://www.percona.com/doc/percona-server-for-mongodb/4.4/release_notes/4.4.13-13.html>`_ and `Percona Backup for MongoDB 1.6.1 <https://www.percona.com/doc/percona-backup-mongodb/release-notes/1.6.1.html>`_.

.. warning::

   Inconsistent data is observed after the upgrade from MongoDB 4.4.3 and 4.4.4 to versions 4.4.8+ and 5.0.2+.
   This issue is fixed upstream in versions 4.4.11+ and 5.0.6+.

   Percona Server for MongoDB 4.4.12 and higher, as part of Percona Distribution for MongoDB 4.4.12 and higher, includes the upstream fixes of these bugs.

   Please :ref:`upgrade <minor-upgrade>` your Percona Distribution for MongoDB to version 4.4.12+ as soon as possible.

Release Highlights
==================

This release of Percona Distribution for MongoDB includes improvements and bug fixes, provided by MongoDB and included in Percona Server for MongoDB. The most notable from  them are the following:

* Added support for `Keys Management Interoperability Protocol (KMIP) <https://www.percona.com/doc/percona-server-for-mongodb/4.4/kmip.html>`_ so that users can store encryption keys in their favorite KMIP-compatible key manager to set up encryption at rest. This is a tech preview feature. 
* Fixed the issue where having a large number of split points causes the chunk splitter to not function correctly and huge chunks would not be split without manual intervention. This can be caused when having small shard key ranges and a very high number of documents and where more than 8192 split points would be needed.
* Added the ``repairShardedCollectionChunksHistory`` command to restore history fields for some chunks. This aims to fix broken snapshot reads and distributed transactions.
* Fixed incorrect logging of queryHash/planCacheKey for operations that share the same ``$lookup`` shape.
* Added a new startup parameter that skips verifying the table logging settings on restarting as a replica set node from the standalone mode during the restore. This speeds up the restore process.



.. include:: .res/replace.txt
