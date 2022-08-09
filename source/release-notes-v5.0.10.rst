.. _DISTMONGO-5.0.10:

================================================================================
*Percona Distribution for MongoDB* 5.0.10 (2022-08-09)
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

This release of |pdmdb| is based on `Percona Server for MongoDB 5.0.10-9 <https://www.percona.com/doc/percona-server-for-mongodb/5.0/release_notes/5.0.10-9.html>`_ and `Percona Backup for MongoDB 1.8.1 <https://www.percona.com/doc/percona-backup-mongodb/release-notes/1.8.1.html>`_.

Release Highlights
==================

This release of |pdmdb| includes bug fixes and improvements provided by MongoDB and included in Percona Server for MongoDB. It specifically includes multiple fixes related to sharding and the resharding operation. 

* Fixed the issue with bad projection created during dependency analysis due to string order assumption. It resulted in the ``PathCollision`` error. The issue is fixed by improving dependency analysis for projections by folding dependencies into ancestor dependencies where possible.
* Fixed the deadlock situation in cross shard transactions that could occur when the FCV (Feature Compatibility Version) was set after the "prepared" state of the transactions. That ended up with both the the `setFCV <https://www.mongodb.com/docs/manual/reference/command/setFeatureCompatibilityVersion/>`_ thread and the ``TransactionCoordinator`` hung.
* This is a v6.0 backport fix to v5.0 that disables opportunistic read targeting (except for specified hedged reads) in order to prevent possible performance problems associated with uneven read distribution across the secondaries.
* Backported the check for user errors in case deadline on the migration destination manager is hit while waiting for a range to be cleared up. This prevents the balancer from getting blocked.
* Fixed the situation where the shards may skip certain steps in the resharding process but respond to the resharding coordinator as if they had. This can cause the resharding coordinator to continue to wait for updated states in the ``config.reshardingOperations`` document on the primary config server and stall indefinitely.
* Fixed the potential for the range deleter to wait unnecessarily during concurrent migrations between batches.
* Fixed the issue where 2 very different measurements (one in the past and one in future) could be incorrectly included in the same buckettime-series bucket.
* Resolved potential problem when adding or removing shards and incorrectly gossiping a new topology time without it being majorly committed.
  
|PBM| 1.8.1 improvements include the following:

* Fixed the restore failure on a different cluster. Now the UUID of users and system collections are not preserved when replaying the oplog. 
* The Point-in-Time recovery chunks display is now consistent in both ``pbm status`` and ``pbm list`` outputs

Packaging Notes
===============

Debian 9 (“Stretch”) is no longer supported. 

.. seealso::

   Percona Blog: `OS Platform End of Life (EOL) Announcement for Debian Linux 9 <https://www.percona.com/blog/os-platform-end-of-life-eol-announcement-for-debian-linux-9/>`_  

.. |date| replace:: August 9, 2022
.. include:: .res/replace.txt