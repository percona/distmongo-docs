.. _DISTMONGO-5.0.11:

================================================================================
*Percona Distribution for MongoDB* 5.0.11 (2022-09-01)
================================================================================

:Date: |date|
:Installation: :ref:`install`

Percona Distribution for MongoDB is a freely available MongoDB database alternative, giving you a single solution that combines enterprise components from the open source community, designed and tested to work together. The aim of Percona Distribution for MongoDB is to enable you to run and operate your
|mongodb| efficiently with the data being consistently backed up.

|pdmdb| includes the following components:

* |PSMDB| is a fully compatible open source, drop-in replacement
  for MongoDB.
* |pbm| is a distributed, low-impact solution for achieving
  consistent backups of |mongodb| sharded clusters and replica sets.

This release of |pdmdb| is based on `Percona Server for MongoDB 5.0.11-10 <https://www.percona.com/doc/percona-server-for-mongodb/5.0/release_notes/5.0.11-10.html>`_ and `Percona Backup for MongoDB 1.8.1 <https://www.percona.com/doc/percona-backup-mongodb/release-notes/1.8.1.html>`_.

Release Highlights
==================

.. important::

   With this release, the ``kmipKeyIdentifier`` option for data-at-rest encryption using the KMIP protocol (tech preview feature) is optional. This change serves to improve the user experience with |PSMDB| as the option names and behavior are similar to those of MongoDB Enterprise. However, if data-at-rest encryption using KMIP is configured, it is the breaking change because the standard upgrade procedure does not work. We do recommend to use the data-at-rest encryption using the KMIP protocol only for testing purposes until it is in the general availability stage.

   If you have configured data at rest encryption and it is absolutely necessary to upgrade your MongoDB instance, see the :ref:`upgrade instructions <upgrade-kmip>`.


This release of |pdmdb| includes bug fixes and improvements provided by MongoDB and included in Percona Server for MongoDB and |pdmdb|. Among them are the following:

* Fixed the issue that caused inconsistency in sharding metadata when running the ``movePrimary`` command on the database that has the Feature Compatibility Version (FCV) set to 4.4 or earlier. Affects MongoDB versions 5.0.0 through 5.0.10 and MongoDB 6.0.0. Upgrade to the the fixed version of MongoDB 5.0.11 / Percona Server for MongoDB 5.0.11-10 as soon as possible.
* Improved handling of large/NaN (Not a Number) values for text index and geo index version.
* Prevented potential server crash or lost writes when a resharding retry happens after the primary node failover. This is fixed by refreshing the routing information on the primary node during resharding.
* Prevented rollback to stable operation to generate wrong updates/tombstones by always reading the cell time window information to decide the history store update visibility.
* Fixed memory leak in update restore eviction.
* Failed chunk migrations can lead to recipient shard having different config.transactions records between primaries and secondaries - inconsistent data.
* Fixed the issue when resharding a collection with a very large number of zones configured may have stalled on config server primary indefinitely.
* Fixed the issue when retrying a failed resharding operation after a primary failover could lead to server crash or lost writes.
* Prevented sharding DDL coordinator to lock itself out in distlock retry loop.
  
|PBM| 1.8.1 improvements include the following:

* Fixed the restore failure on a different cluster. Now the UUID of users and system collections are not preserved when replaying the oplog. 
* The Point-in-Time recovery chunks display is now consistent in both ``pbm status`` and ``pbm list`` outputs

Packaging Notes
===============

Debian 9 (“Stretch”) is no longer supported. 

.. seealso::

   Percona Blog: `OS Platform End of Life (EOL) Announcement for Debian Linux 9 <https://www.percona.com/blog/os-platform-end-of-life-eol-announcement-for-debian-linux-9/>`_  

.. |date| replace:: September 1, 2022
.. include:: .res/replace.txt