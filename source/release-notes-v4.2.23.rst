.. _DISTMONGO-4.2.23:

================================================================================
*Percona Distribution for MongoDB* 4.2.23 (2022-11-08)
================================================================================

:Date: November 8, 2022
:Installation: :ref:`install`

|pdmdb| is a collection of solutions to run and operate your
|mongodb| efficiently with the data being consistently backed up.  

|pdmdb| includes the following components:

* |PSMDB| is a fully compatible source-available, drop-in replacement
  for MongoDB.
* |pbm| is a distributed, low-impact solution for achieving
  consistent backups of |mongodb| sharded clusters and replica sets.

This release of |pdmdb| is based on `Percona Server for MongoDB 4.2.23-23 <https://www.percona.com/doc/percona-server-for-mongodb/4.2/release_notes/4.2.23-23.html>`_ and `Percona Backup for MongoDB 2.0.2 <https://www.percona.com/doc/percona-backup-mongodb/release-notes/2.0.2.html>`_. 	


Release Highlights
===================

* :ref:`Data-at-rest encryption using the Key Management Interoperability Protocol (KMIP) <kmip>` is generally available enabling you to use it in your production environment
* :ref:`backup-cursor` functionality is generally available, enabling your application developers to use it for building custom backup solutions. 
  
  .. note::

     Percona provides `Percona Backup for MongoDB <https://docs.percona.com/percona-backup-mongodb/index.html>`_ - the open source tool for consistent backups and restores in MongoDB sharded clusters.

* Fixed security vulnerability `CVE-2022-3602 <https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3602>`_ for |pdmdb| 4.2.21 and higher installed from tarballs on Ubuntu 22.04.
* Detected and resolved table logging inconsistencies for WiredTiger tables at startup
* Fixed retryable writes on update and delete commands to not execute more than once if chunk is migrated and shard key pattern uses nested fields
* Changed the `ExpressionSetUnion::isCommutative()` function to return false when a non-simple collation is in place for the `$setUnion` aggregation expression
* Prevented TTLMonitor from processing index if `expireAfterSeconds` value is NaN (Not a Number)

|PBM| 2.0.x improvements are the following:

* Physical backups and restores are now generally available. This enables you to use them in production environments.
* `Data-at-rest encryption <https://docs.percona.com/percona-backup-mongodb/usage/restore.html#physical-restores-with-data-at-rest-encryption>`_ is supported for physical backups and restores. This enables you to comply to data security regulations and save time on operating with large data sets.
* By `tracking physical restore progress <https://docs.percona.com/percona-backup-mongodb/usage/restore-progress.html>`_, you have a clear picture of your restore operations and can timely react to any changes or issues.
* `Logical backups and restores can now be done selectively <https://docs.percona.com/percona-backup-mongodb/usage/selective-backup.html>`_. This is a tech preview feature [1]_ yet it enables you to work only with the desired subset of data and thereby save time on database maintenance and costs on storage.
  
|PBM| 2.0.2 fixes the usability issues for applications operating with Percona Backup for MongoDB by providing the error messages for the status output in the JSON format.  
 
 

.. include:: .res/replace.txt
