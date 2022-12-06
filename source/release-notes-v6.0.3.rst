.. _DISTMONGO-6.0.3:

================================================================================
*Percona Distribution for MongoDB* 6.0.3 (2022-12-07)
================================================================================

:Date: December 7, 2022
:Installation: :ref:`install`

Percona Distribution for MongoDB is a freely available MongoDB database alternative, giving you a single solution that combines enterprise components from the open source community, designed and tested to work together. The aim of Percona Distribution for MongoDB is to enable you to run and operate your
|mongodb| efficiently with the data being consistently backed up.

|pdmdb| includes the following components:

* |PSMDB| is a fully compatible source-available, drop-in replacement
  for MongoDB.
* |pbm| is a distributed, low-impact solution for achieving
  consistent backups of |mongodb| sharded clusters and replica sets.

This release of |pdmdb| is based on the production release of `Percona Server for MongoDB 6.0.3-2 <https://docs.percona.com/percona-server-for-mongodb/6.0/release_notes/6.0.3-2.html>`_ and `Percona Backup for MongoDB 2.0.2 <https://www.percona.com/doc/percona-backup-mongodb/release-notes/2.0.2.html>`_.


Release Highlights
==================
  
* Fixed the issue with how the server handles batches of writes when running $out with secondary read preference by updating write size estimation logic in ``DocumentSourceWriter``
* Allowed search queries to pass through query analysis when Client-Side Field Level Encryption is enabled for the MongoClient
* Prevented dropping empty path component from `elemMatch` path during index selection
* Prevented yielding strong locks upon startup recovery when ``_id`` index is missing

  
|PBM| 2.0.2 fixes the usability issues for applications operating with Percona Backup for MongoDB by providing the error messages for the status output in the JSON format.  
  

.. include:: .res/replace.txt
