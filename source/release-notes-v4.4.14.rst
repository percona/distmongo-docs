.. _DISTMONGO-4.4.14:

================================================================================
*Percona Distribution for MongoDB* 4.4.14 (2022-05-25)
================================================================================

:Date: May 25, 2022
:Installation: :ref:`install`

Percona Distribution for MongoDB is a freely available MongoDB database alternative, giving you a single solution that combines enterprise components from the open source community, designed and tested to work together. The aim of Percona Distribution for MongoDB is to enable you to run and operate your
|mongodb| efficiently with the data being consistently backed up.

|pdmdb| includes the following components:

* |PSMDB| is a fully compatible source-available, drop-in replacement
  for MongoDB.
* |pbm| is a distributed, low-impact solution for achieving
  consistent backups of |mongodb| sharded clusters and replica sets.

This release of |pdmdb| is based on `Percona Server for MongoDB 4.4.14-14 <https://www.percona.com/doc/percona-server-for-mongodb/4.4/release_notes/4.4.14-14.html>`_ and `Percona Backup for MongoDB 1.7.0 <https://www.percona.com/doc/percona-backup-mongodb/release-notes/1.7.0.html>`_.

.. important:: 

   To make :ref:`physical backups <backup-types>` and restores, the ``pbm-agent`` must have the read / write access to the ``dataDir``. If you use the filesystem-based backup storage, the ``pbm-agent`` must also have the read / write access to the backup directory. Therefore, starting from version 1.7.0, the user running the ``pbm-agent`` is changed from ``pbm`` to ``mongod`` in |PBM| packages.

   To upgrade |PBM| to version 1.7.0, do the following:

   1. Stop the ``pbm-agent`` process
   2. :ref:`Upgrade <pbm.upgrade>` new version packages
   3. Reload the ``systemd`` process to update the unit file with the following command: 
      
      .. code-block:: bash

         $ sudo  systemctl daemon-reload

   5. If you have a filesystem-based backup storage, grant read / write permissions to the backup directory to the ``mongod`` user.
   6. Restart the ``pbm-agent`` process.

   If MongoDB runs under a *different user than mongod* (the default configuration for |PSMDB|), use the same user to run the ``pbm-agent``. For filesystem-based storage, grant the read / write permissions to the backup directory for this user.

Release Highlights
==================

This release of Percona Distribution for MongoDB includes improvements and bug fixes, provided by MongoDB and included in Percona Server for MongoDB. The most notable from  them are the following:

* Support of the master key rotation for data encrypted using the  :ref:`Keys Management Interoperability Protocol (KMIP) <https://docs.percona.com/percona-server-for-mongodb/4.4/kmip.html>` protocol (tech preview feature). This improvement allows users to comply with regulatory standards for data security.
* Fixed the issue where having a large number of split points causes the chunk splitter to not function correctly and huge chunks would not be split without manual intervention. This can be caused when having small shard key ranges and a very high number of documents and where more than 8192 split points would be needed.
* Added the ``repairShardedCollectionChunksHistory`` command to restore history fields for some chunks. This aims to fix broken snapshot reads and distributed transactions.
* Fixed incorrect logging of queryHash/planCacheKey for operations that share the same ``$lookup`` shape
* Added a new startup parameter that skips verifying the table logging settings on restarting as a replica set node from the standalone mode during the restore. This speeds up the restore process.
  
|PBM| 1.7.0 improvements include the following:

* Support for `physical backups <https://docs.percona.com/percona-backup-mongodb/backup-types.html#backup-types>`_ in |PSMDB| starting from versions 4.2.15-16 and 4.4.6-8 and higher. Physical backups drastically speed up backup and restore performance for large databases (several terabytes). This is a technical preview feature. 
* `Oplog replay <https://docs.percona.com/percona-backup-mongodb/oplog-replay.html>`_ from the arbitrary start time. This reduces Recovery Point Objective (RPO) when database is recovered from physical or storage-level backups.
* Ability to configure compression method and level for point-in-time recovery chunks and compression level for backups.
* Ability to configure the number of S3 multipart upload chunks to comply with various S3-compatible storage provider requirements. 
* Ability to configure the number of upload retries. This facilitates data upload in case of unstable network connection.


.. include:: .res/replace.txt
