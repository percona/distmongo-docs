.. _DISTMONGO-4.2.17:

================================================================================
*Percona Distribution for MongoDB* 4.2.17
================================================================================

:Date: October 11, 2021
:Installation: `Installing Percona Distribution for MongoDB <https://www.percona.com/doc/percona-server-for-mongodb/4.2/install/index.html>`_

|pdmdb| is a collection of solutions to run and operate your
|mongodb| efficiently with the data being consistently backed up.  

|pdmdb| includes the following components:

* |PSMDB| is a fully compatible source-available, drop-in replacement
  for MongoDB.
* |pbm| is a distributed, low-impact solution for achieving
  consistent backups of |mongodb| sharded clusters and replica sets.

This release of |pdmdb| is based on `Percona Server for MongoDB 4.2.17-17 <https://www.percona.com/doc/percona-server-for-mongodb/4.2/release_notes/4.2.17-17.html>`_ and `Percona Backup for MongoDB 1.6.0 <https://www.percona.com/doc/percona-backup-mongodb/release-notes/1.6.0.html>`_. 	

Release Highlights
===================

The bug fixes, provided by MongoDB and included in Percona Server for MongoDB 4.2.17-17 and |pdmdb| 4.2.17 are the following:

* The ``libsasl2`` dependencies are added for DEB-based operating systems to enable GSSAPI and Kerberos authentication to work out-of-the box after installing MongoDB (`SERVER-54729 <https://jira.mongodb.org/browse/SERVER-54729>`_)
* The number of modify updates in WiredTiger is now limited to prevent performance issues (`WT-7776 <https://jira.mongodb.org/browse/WT-7776>`_)
* Errors related to proxy connections receive new error codes so that they don't change the behavior of clients' drivers (`SERVER-50549 <https://jira.mongodb.org/browse/SERVER-50549>`_)
* Pre-warming of connection pools in `mongos` tier (`SERVER-44152 <https://jira.mongodb.org/browse/SERVER-44152>`_)
* Improvements to Secondary slowdowns or hangs (`SERVER-34938 <https://jira.mongodb.org/browse/SERVER-34938>`_)


|PBM| 1.6.0 improvements include the following:

* Support for Percona Server for MongoDB and MongoDB Community 5.0
* Point-in-time recovery enhancements: ability to restore from any previous snapshot and configurable span of oplog events
* JSON output for `PBM commands <https://www.percona.com/doc/percona-backup-mongodb/pbm-commands.html>`_ to simplify interfacing PBM with applications




.. include:: .res/replace.txt
