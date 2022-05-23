.. _DISTMONGO-4.2.20:

================================================================================
*Percona Distribution for MongoDB* 4.2.20 (2022-05-23)
================================================================================

:Date: May 23, 2022
:Installation: :ref:`install`

|pdmdb| is a collection of solutions to run and operate your
|mongodb| efficiently with the data being consistently backed up.  

|pdmdb| includes the following components:

* |PSMDB| is a fully compatible open source, drop-in replacement
  for MongoDB.
* |pbm| is a distributed, low-impact solution for achieving
  consistent backups of |mongodb| sharded clusters and replica sets.

This release of |pdmdb| is based on `Percona Server for MongoDB 4.2.20-20 <https://www.percona.com/doc/percona-server-for-mongodb/4.2/release_notes/4.2.20-20.html>`_ and `Percona Backup for MongoDB 1.7.0 <https://www.percona.com/doc/percona-backup-mongodb/release-notes/1.7.0.html>`_. 	

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
===================

The bug fixes, provided by MongoDB and included in Percona Server for MongoDB 4.2.20-20 and |pdmdb| 4.2.20 are the following:

* Support of the master key rotation for data encrypted using the  :ref:`Keys Management Interoperability Protocol (KMIP) <https://docs.percona.com/percona-server-for-mongodb/4.2/kmip.html>` protocol (tech preview feature). This improvement allows users to comply with regulatory standards for data security. 
* Abort the WiredTiger transaction after releasing Client lock to avoid deadlocks.
* Check if the host has ``cgroups`` v2 enabled and read the memory limits according to that.
* Return the shutdown error as the top level error when batch writing command fails due to mongos shutdown.
* Fixed the double free state for the ``DocumentSource::optimizeAt()`` pipeline by making sure all pointers are in place before disposing the pipeline prefix.     

|PBM| 1.7.0 improvements include the following:

* Support for `physical backups <https://docs.percona.com/percona-backup-mongodb/backup-types.html#backup-types>`_ in |PSMDB| starting from versions 4.2.15-16 and 4.4.6-8 and higher. Physical backups drastically speed up backup and restore performance for large databases (several terabytes). This is a technical preview feature. 
* `Oplog replay <https://docs.percona.com/percona-backup-mongodb/oplog-replay.html>`_ from the arbitrary start time. This reduces Recovery Point Objective (RPO) when database is recovered from physical or storage-level backups.
* Ability to configure compression method and level for point-in-time recovery chunks and compression level for backups.
* Ability to configure the number of S3 multipart upload chunks to comply with various S3-compatible storage provider requirements. 
* Ability to configure the number of upload retries. This facilitates data upload in case of unstable network connection.

.. include:: .res/replace.txt
