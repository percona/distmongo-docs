.. _DISTMONGO-4.4.18:

================================================================================
*Percona Distribution for MongoDB* 4.4.18 (2022-12-19)
================================================================================

:Date: December 19, 2022
:Installation: :ref:`install`


Percona Distribution for MongoDB is a freely available MongoDB database alternative, giving you a single solution that combines enterprise components from the open source community, designed and tested to work together. The aim of Percona Distribution for MongoDB is to enable you to run and operate your
|mongodb| efficiently with the data being consistently backed up.

|pdmdb| includes the following components:

* |PSMDB| is a fully compatible source-available, drop-in replacement
  for MongoDB.
* |pbm| is a distributed, low-impact solution for achieving
  consistent backups of |mongodb| sharded clusters and replica sets.

This release of |pdmdb| is based on `Percona Server for MongoDB 4.4.18-18 <https://www.percona.com/doc/percona-server-for-mongodb/4.4/release_notes/4.4.18-18.html>`_ and `Percona Backup for MongoDB 2.0.2 <https://www.percona.com/doc/percona-backup-mongodb/release-notes/2.0.2.html>`_.


Release Highlights
==================

This release of Percona Distribution for MongoDB includes improvements and bug fixes, provided by MongoDB and included in Percona Server for MongoDB. The most notable from them are the following:

* Fixed the issue with how the server handles batches of writes when running $out with secondary read preference by updating write size estimation logic in ``DocumentSourceWriter``
* Improved the performance of inserts into unique indexes
* Prevented dropping empty path component from elemMatch path during index selection
* Avoided sending the "keyValue" field to drivers on duplicate key error
* Disallowed the use of the ``allowSpeculativeMajorityReads`` flag for the ``find`` command in transactions
  

|PBM| 2.0.2 fixes the usability issues for applications operating with Percona Backup for MongoDB by providing the error messages for the status output in the JSON format.  


.. include:: .res/replace.txt
