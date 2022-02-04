.. _DISTMONGO-5.0.6:

================================================================================
*Percona Distribution for MongoDB* 5.0.6
================================================================================

:Date: February 10, 2022
:Installation: `Installing Percona Distribution for MongoDB <https://www.percona.com/doc/percona-distribution-for-mongodb/5.0/installation.html>`_

Percona Distribution for MongoDB is a freely available MongoDB database alternative, giving you a single solution that combines enterprise components from the open source community, designed and tested to work together. The aim of Percona Distribution for MongoDB is to enable you to run and operate your
|mongodb| efficiently with the data being consistently backed up.

|pdmdb| includes the following components:

* |PSMDB| is a fully compatible open source, drop-in replacement
  for MongoDB.
* |pbm| is a distributed, low-impact solution for achieving
  consistent backups of |mongodb| sharded clusters and replica sets.

This release of |pdmdb| is based on `Percona Server for MongoDB 5.0.6-5 <https://www.percona.com/doc/percona-server-for-mongodb/5.0/release_notes/5.0.6-5.html>`_ and `Percona Backup for MongoDB 1.6.1 <https://www.percona.com/doc/percona-backup-mongodb/release-notes/1.6.1.html>`_.

.. warning::

   Inconsistent data is observed after the upgrade from MongoDB 4.4.3 and 4.4.4 to versions 4.4.8+ and 5.0.2+.
   This issue is fixed upstream in versions 4.4.11 and 5.0.6. |PSMDB| also includes the fix in versions 4.4.12-12 and 5.0.6-5

   See the upgrade recommendations below:

   - Clusters on versions 4.4.0 and 4.4.1 are safe to upgrade to 4.4.8+ or 5.0.2+ but should upgrade to recommended versions 4.4.11+ or 5.0.5+
   - Clusters on versions 4.4.2, 4.4.3, or 4.4.4 should **downgrade** to 4.4.1 and then upgrade to versions  4.4.11+ or 5.0.5+. 
   - Clusters running versions 4.4.5 - 4.4.7 can and should upgrade to versions 4.4.11+ or 5.0.5+. 

   Note that clusters running versions 4.4.2 - 4.4.8 are affected by the bug `WT-7995 <https://jira.mongodb.org/browse/WT-7995>`_. See `WT-7995 <https://jira.mongodb.org/browse/WT-7995>`_ for specific explanation and instructions on running the `validate <https://docs.mongodb.com/manual/reference/command/validate/>`_ command to check for data inconsistencies. These data inconsistencies can lead to data loss if not identified and repaired at this point between versions 4.4.8 and 4.4.9.

   If the `validate <https://docs.mongodb.com/manual/reference/command/validate/>`_  command output reports any failures, resync the impacted node from an unaffected node.   **The validate command must be run against all collections in the database. This process can be resource intensive and can negatively impact performance.**

Release Highlights
==================
This release of Percona Distribution for MongoDB includes bug fixes, provided by MongoDB and included in Percona Server for MongoDB. The most notable from them are the following:

* Fixed an issue with inconsistent data observed during the direct upgrade from from 4.4.3 and 4.4.4 to 4.4.8+ and 5.0.2+. Data inconsistency was caused by the incorrect checkpoint metadata to sometimes be recorded by MongoDB versions 4.4.3 and 4.4.4. WiredTiger used this metadata during node startup that could lead to data corruption and could cause the DuplicateKey error. The fix requires the upgrade to versions 4.4.11+ or 5.0.5+. For details, refer to `WT-8395 <https://jira.mongodb.org/browse/WT-8395>`_.
* Fixed an issue unavailability of a shard in sharded clusters. Affects MongoDB versions 5.0.0 - 5.0.5. Requires the following steps:

   - Restarting the shards as replica sets 
   - Checking that range deletion tasks are consistent with migration coordinators 
   - Majority-deleting all migration coordinators with a definitive decision
   - Restarting the nodes as shards.

  For details, refer to `SERVER-62245 <https://jira.mongodb.org/browse/SERVER-62245>`_.
* Fixed time-series bucket OID collisions by adding the difference between the actual timestamp and the rounded timestamp to the instance portion of the OID.


.. include:: .res/replace.txt