.. _DISTMONGO-4.2.18:

================================================================================
*Percona Distribution for MongoDB* 4.2.18
================================================================================

:Date: January 19, 2022
:Installation: `Installing Percona Distribution for MongoDB <https://www.percona.com/doc/percona-server-for-mongodb/4.2/install/index.html>`_

|pdmdb| is a collection of solutions to run and operate your
|mongodb| efficiently with the data being consistently backed up.  

|pdmdb| includes the following components:

* |PSMDB| is a fully compatible open source, drop-in replacement
  for MongoDB.
* |pbm| is a distributed, low-impact solution for achieving
  consistent backups of |mongodb| sharded clusters and replica sets.

This release of |pdmdb| is based on `Percona Server for MongoDB 4.2.18-18 <https://www.percona.com/doc/percona-server-for-mongodb/4.2/release_notes/4.2.18-18.html>`_ and `Percona Backup for MongoDB 1.6.1 <https://www.percona.com/doc/percona-backup-mongodb/release-notes/1.6.1.html>`_. 	

Release Highlights
===================

The bug fixes, provided by MongoDB and included in Percona Server for MongoDB 4.2.18-18 and |pdmdb| 4.2.18 are the following:

* Added the `SetAllowMigrationsCommand` command that prevents the balancer to migrate chunks on shards.
* Added a flag for the config server that prevents new migrations to start and ongoing migrations to commit.
* Improved the duplicate key handler behavior if the exact key already exists in the table. This fixes availability loss during the index build that was caused by checking many false duplicates.
* Added periodic clean up of logical sessions cache on arbiters 


|PBM| 1.6.1 improvements include the following:

* Improved backup and point-in-time recovery routines alignment by using sequential ``delete-pitr``/``install-backup`` operations instead of in-memory backup intent. This fixes the inability of a backup to start.
* Added support for automated access to S3 buckets using an EC2 instance profile. When Percona Backup for MongoDB is deployed using an EC2 instance, EC2 environment variables and metadata are used for S3 authentication, saving you from explicitly specifying S3 credentials in the Percona Backup for MongoDB configuration file. This comes handy for architectures deployed using the services like Amazon EC2, kiam, kube2iam or irsa.
* Extended logging for ``pbm-agents``. This improves user experience with Percona Backup for MongoDB.




.. include:: .res/replace.txt
