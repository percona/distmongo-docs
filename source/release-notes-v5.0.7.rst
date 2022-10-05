.. _DISTMONGO-5.0.7:

================================================================================
*Percona Distribution for MongoDB* 5.0.7
================================================================================

:Date: April 20, 2022
:Installation: `Installing Percona Distribution for MongoDB <https://www.percona.com/doc/percona-distribution-for-mongodb/5.0/installation.html>`_

.. warning::

   We don't recommend this version for the production use due to the critical issue with sharding metadata inconsistency: `SERVER-68511 <https://jira.mongodb.org/browse/SERVER-68511>`_. The metadata inconsistency is observed when running the ``movePrimary`` command on the database that has the Feature Compatibility Version (FCV) set to 4.4 or earlier. Affects MongoDB versions 5.0.0 through 5.0.10 and MongoDB 6.0.0. Upgrade to the fixed version of MongoDB 5.0.11 / Percona Server for MongoDB 5.0.11-10 or |pdmdb| 5.0.11 as soon as possible.

   Please follow closely the upstream recommendations outlined in `SERVER-68511 <https://jira.mongodb.org/browse/SERVER-68511>`_ to work around this issue and for the remediation steps, if your cluster is affected.
   

Percona Distribution for MongoDB is a freely available MongoDB database alternative, giving you a single solution that combines enterprise components from the open source community, designed and tested to work together. The aim of Percona Distribution for MongoDB is to enable you to run and operate your
|mongodb| efficiently with the data being consistently backed up.

|pdmdb| includes the following components:

* |PSMDB| is a fully compatible source-available, drop-in replacement
  for MongoDB.
* |pbm| is a distributed, low-impact solution for achieving
  consistent backups of |mongodb| sharded clusters and replica sets.

This release of |pdmdb| is based on `Percona Server for MongoDB 5.0.7-6 <https://www.percona.com/doc/percona-server-for-mongodb/5.0/release_notes/5.0.7-6.html>`_ and `Percona Backup for MongoDB 1.7.0 <https://www.percona.com/doc/percona-backup-mongodb/release-notes/1.7.0.html>`_.

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

This release of Percona Distribution for MongoDB includes the support of Keys Management Interoperability Protocol (KMIP). Thus, users can store encryption keys in their favorite KMIP-compatible key manager to set up encryption at rest. This is a tech preview feature.

The most notable bug fixes, provided by MongoDB and included in Percona Server for MongoDB are the following:

* Fixed the issue where having a large number of split points causes the chunk splitter to not function correctly and huge chunks would not be split without manual intervention. This can be caused when having small shard key ranges and a very high number of documents and where more than 8192 split points would be needed.
* Recover the ``RecoverableCriticalSection`` service after the ``initialSync`` and ``startupRecovery`` stages have completed. This prevents a started up shard to miss an in-memory critical section of a resharded collection.
* Fixed an issue that occurred during the attempt to perform the collation-encoding of a document with a missing sort attribute. In this case an invariant is violated and ``mongod`` crashes. 
* Fixed an issue when the rename collection (sharding step) participants can get stuck.
* Fixed an issue with idle cursors remaining open when the client attempts to run an aggregation with ``$out`` or ``$merge`` in a transaction on a sharded cluster.  
* Check if the host has cgroups v2 enabled and read the memory limits according to that.
* Report an error when the WiredTiger version file is empty or missing during a startup.

 
 
|PBM| 1.7.0 improvements include the following:

* Support for `physical backups <https://docs.percona.com/percona-backup-mongodb/backup-types.html#backup-types>`_ in |PSMDB| starting from versions 4.2.15-16 and 4.4.6-8 and higher. Physical backups drastically speed up backup and restore performance for large databases (several terabytes). This is a technical preview feature. 
* `Oplog replay <https://docs.percona.com/percona-backup-mongodb/oplog-replay.html>`_ from the arbitrary start time. This reduces Recovery Point Objective (RPO) when database is recovered from physical or storage-level backups.
* Ability to configure compression method and level for point-in-time recovery chunks and compression level for backups.
* Ability to configure the number of S3 multipart upload chunks to comply with various S3-compatible storage provider requirements. 
* Ability to configure the number of upload retries. This facilitates data upload in case of unstable network connection.

.. include:: .res/replace.txt