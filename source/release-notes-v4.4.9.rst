.. _DISTMONGO-4.4.9:

================================================================================
*Percona Distribution for MongoDB* 4.4.9
================================================================================

:Date: October 5, 2021
:Installation: `Installing Percona Distribution for MongoDB <https://www.percona.com/doc/percona-distribution-for-mongodb/4.4/installation.html>`_

.. warning::

   Beginning with MongoDB 4.4.2, several data impacting or corrupting bugs were introduced. Find the details in the following resources:

   * `WT-7984 <https://jira.mongodb.org/browse/WT-7984>`_ 
   * `WT-7995 <https://jira.mongodb.org/browse/WT-7995>`_
   * `Percona Server for MongoDB 4.4.9-10 <https://www.percona.com/doc/percona-server-for-mongodb/4.4/release_notes/4.4.9-10.html>`_

   These bugs are fixed in MongoDB 4.4.9. Percona Server for MongoDB 4.4.9-10, as part of Percona Distribution for MongoDB, includes the upstream fixes of these bugs.

   Please :ref:`upgrade <minor-upgrade>` your Percona Distribution for MongoDB to version 4.4.9 as soon as possible.

Percona Distribution for MongoDB is a freely available MongoDB database alternative, giving you a single solution that combines enterprise components from the open source community, designed and tested to work together. The aim of Percona Distribution for MongoDB is to enable you to run and operate your
|mongodb| efficiently with the data being consistently backed up.

|pdmdb| includes the following components:

* |PSMDB| is a fully compatible open source, drop-in replacement
  for MongoDB.
* |pbm| is a distributed, low-impact solution for achieving
  consistent backups of |mongodb| sharded clusters and replica sets.

This release of |pdmdb| is based on `Percona Server for MongoDB 4.4.9-10 <https://www.percona.com/doc/percona-server-for-mongodb/4.4/release_notes/4.4.9-10.html>`_ and `Percona Backup for MongoDB 1.6.0 <https://www.percona.com/doc/percona-backup-mongodb/release-notes/1.6.0.html>`_.



.. include:: .res/replace.txt
