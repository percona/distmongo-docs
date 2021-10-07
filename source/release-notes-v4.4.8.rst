.. _DISTMONGO-4.4.8:

================================================================================
*Percona Distribution for MongoDB* 4.4.8
================================================================================

:Date: August 16, 2021
:Installation: `Installing Percona Distribution for MongoDB <https://www.percona.com/doc/percona-distribution-for-mongodb/4.4/installation.html>`_

.. warning::

   This version is not recommended for production use due to the following critical issues found in MongoDB Community: `WT-7984 <https://jira.mongodb.org/browse/WT-7984>`_ and `WT-7995 <https://jira.mongodb.org/browse/WT-7995>`_. They are fixed in `MongoDB 4.4.9 Community Edition  <https://docs.mongodb.com/manual/release-notes/4.4/#4.4.9---sep-21--2021>`_ and `Percona Server for MongoDB 4.4.9-10 <https://www.percona.com/doc/percona-server-for-mongodb/4.4/release_notes/4.4.9-10.html>`_. |pdmdb| 4.4.9 includes these fixes too.

   We recommend you to :ref:`upgrade <minor-upgrade>` to |pdmdb| 4.4.9-10 as soon as possible and run the `validate <https://docs.mongodb.com/manual/reference/command/validate/>`_ command on every collection on every replica set node.

Percona Distribution for MongoDB is a freely available MongoDB database alternative, giving you a single solution that combines enterprise components from the open source community, designed and tested to work together. The aim of Percona Distribution for MongoDB is to enable you to run and operate your
|mongodb| efficiently with the data being consistently backed up.

|pdmdb| includes the following components:

* |PSMDB| is a fully compatible open source, drop-in replacement
  for MongoDB.
* |pbm| is a distributed, low-impact solution for achieving
  consistent backups of |mongodb| sharded clusters and replica sets.

This release of |pdmdb| is based on `Percona Server for MongoDB 4.4.8-9 <https://www.percona.com/doc/percona-server-for-mongodb/4.4/release_notes/4.4.8-9.html>`_ and `Percona Backup for MongoDB 1.6.0 <https://www.percona.com/doc/percona-backup-mongodb/release-notes/1.6.0.html>`_.



.. include:: .res/replace.txt
