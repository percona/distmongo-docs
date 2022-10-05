.. _DISTMONGO-4.4.10:

================================================================================
*Percona Distribution for MongoDB* 4.4.10
================================================================================

:Date: November 10, 2021
:Installation: `Installing Percona Distribution for MongoDB <https://www.percona.com/doc/percona-distribution-for-mongodb/4.4/installation.html>`_

Percona Distribution for MongoDB is a freely available MongoDB database alternative, giving you a single solution that combines enterprise components from the open source community, designed and tested to work together. The aim of Percona Distribution for MongoDB is to enable you to run and operate your
|mongodb| efficiently with the data being consistently backed up.

|pdmdb| includes the following components:

* |PSMDB| is a fully compatible source-available, drop-in replacement
  for MongoDB.
* |pbm| is a distributed, low-impact solution for achieving
  consistent backups of |mongodb| sharded clusters and replica sets.

This release of |pdmdb| is based on `Percona Server for MongoDB 4.4.10-11 <https://www.percona.com/doc/percona-server-for-mongodb/4.4/release_notes/4.4.10-11.html>`_ and `Percona Backup for MongoDB 1.6.1 <https://www.percona.com/doc/percona-backup-mongodb/release-notes/1.6.1.html>`_.



Release Highlights
==================
This release of Percona Distribution for MongoDB includes bug fixes, provided by MongoDB and included in Percona Server for MongoDB. The most notable from  them are the following:

* Fixed delays in establishing egress connections on ``mongos`` due to delayed responses from ``libcrypto.so`` 
 
|PBM| 1.6.1 improvements include the following:

* Improved backup and point-in-time recovery routines alignment by using sequential ``delete-pitr``/``install-backup`` operations instead of in-memory backup intent. This fixes the inability of a backup to start.
* Added support for automated access to S3 buckets using an EC2 instance profile. When Percona Backup for MongoDB is deployed using an EC2 instance, EC2 environment variables and metadata are used for S3 authentication, saving you from explicitly specifying S3 credentials in the Percona Backup for MongoDB configuration file. This comes handy for architectures deployed using the services like Amazon EC2, kiam, kube2iam or irsa.
* Extended logging for ``pbm-agents``. This improves user experience with Percona Backup for MongoDB.


.. include:: .res/replace.txt
