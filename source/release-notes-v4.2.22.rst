.. _DISTMONGO-4.2.22:

================================================================================
*Percona Distribution for MongoDB* 4.2.22 (2022-09-06)
================================================================================

:Date: September 6, 2022
:Installation: :ref:`install`

|pdmdb| is a collection of solutions to run and operate your
|mongodb| efficiently with the data being consistently backed up.  

|pdmdb| includes the following components:

* |PSMDB| is a fully compatible source-available, drop-in replacement
  for MongoDB.
* |pbm| is a distributed, low-impact solution for achieving
  consistent backups of |mongodb| sharded clusters and replica sets.

This release of |pdmdb| is based on `Percona Server for MongoDB 4.2.22-22 <https://www.percona.com/doc/percona-server-for-mongodb/4.2/release_notes/4.2.22-22.html>`_ and `Percona Backup for MongoDB 1.8.1 <https://www.percona.com/doc/percona-backup-mongodb/release-notes/1.8.1.html>`_. 	


Release Highlights
===================

.. important::

   With this release, the ``kmipKeyIdentifier`` option for data-at-rest encryption using the KMIP protocol (tech preview feature) is optional. This change serves to improve the user experience with |PSMDB| as the option names and behavior are similar to those of MongoDB Enterprise. However, if data-at-rest encryption using KMIP is configured, it is the breaking change because the standard upgrade procedure does not work. We do recommend to use the data-at-rest encryption using the KMIP protocol only for testing purposes until it is in the general availability stage.

   If you have configured data at rest encryption and it is absolutely necessary to upgrade your MongoDB instance, see the `upgrade instructions <https://docs.percona.com/percona-server-for-mongodb/4.2/kmip.html#minor-upgrade-of-psmdb-to-version-4-2-22-22-and-higher>`_.

This release of |pdmdb| includes bug fixes and improvements provided by MongoDB and included in Percona Server for MongoDB and |pdmdb|. Among them are the following:

* Fixed an issue that occurred during the attempt to perform the collation-encoding of a document with a missing sort attribute. In this case an invariant is violated and ``mongod`` crashes.
* Fixed the TTLMonitor behavior to skip processing TTL indexes if the expireAfterSeconds option value is NaN (Not a Number).
* Changed the behavior of the ShardingTaskExecutorPoolSize parameter to control the connection pool size for config server replica set and shard nodes separately.
* Fixed the issue with bad projection created during dependency analysis due to string order assumption. It resulted in the ``PathCollision`` error. The issue is fixed by improving dependency analysis for projections by folding dependencies into ancestor dependencies where possible.

|PBM| 1.8.1 improvements include the following:

* Fixed the restore failure on a different cluster. Now the UUID of users and system collections are not preserved when replaying the oplog. 
* The Point-in-Time recovery chunks display is now consistent in both ``pbm status`` and ``pbm list`` outputs

Packaging Notes
===============

Debian 9 (“Stretch”) is no longer supported. 
   
 

.. include:: .res/replace.txt
