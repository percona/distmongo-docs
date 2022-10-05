.. _DISTMONGO-5.0.5:

================================================================================
*Percona Distribution for MongoDB* 5.0.5
================================================================================

:Date: December 28, 2021
:Installation: `Installing Percona Distribution for MongoDB <https://www.percona.com/doc/percona-distribution-for-mongodb/5.0/installation.html>`_

.. warning::

   We don't recommend this version for the production use due to the critical issue with sharding metadata inconsistency: `SERVER-68511 <https://jira.mongodb.org/browse/SERVER-68511>`_. The metadata inconsistency is observed when running the ``movePrimary`` command on the database that has the Feature Compatibility Version (FCV) set to 4.4 or earlier. Affects MongoDB versions 5.0.0 through 5.0.10 and MongoDB 6.0.0. Upgrade to the fixed version of MongoDB 5.0.11 / Percona Server for MongoDB 5.0.11-10 as soon as possible.

   Please follow closely the upstream recommendations outlined in `SERVER-68511 <https://jira.mongodb.org/browse/SERVER-68511>`_ to work around this issue and for the remediation steps, if your cluster is affected.

We are pleased to announce the release of the Percona Distribution for MongoDB  for the recent major version 5.0.x.

Percona Distribution for MongoDB is a freely available MongoDB database alternative, giving you a single solution that combines enterprise components from the open source community, designed and tested to work together. The aim of Percona Distribution for MongoDB is to enable you to run and operate your
|mongodb| efficiently with the data being consistently backed up.

|pdmdb| includes the following components:

* |PSMDB| is a fully compatible source-available, drop-in replacement
  for MongoDB.
* |pbm| is a distributed, low-impact solution for achieving
  consistent backups of |mongodb| sharded clusters and replica sets.

This release of |pdmdb| is based on the production release of `Percona Server for MongoDB 5.0.5-4 <https://www.percona.com/doc/percona-server-for-mongodb/5.0/release_notes/5.0.5-4.html>`_ and `Percona Backup for MongoDB 1.6.1 <https://www.percona.com/doc/percona-backup-mongodb/release-notes/1.6.1.html>`_.



Release Highlights
==================
This release of Percona Distribution for MongoDB includes bug fixes, provided by MongoDB and included in Percona Server for MongoDB. The most notable from them are the following:

* Added histograms to track latency for tasks scheduled on the reactor thread.
* Fixed an issue when resharding a collection that could cause data inconsistency (lost writes) due to incorrect actions by the ReshardingCoordinator and attempts to commit anyway. Also could cause fassert() to config server primary.
* Fixed an issue with stalls on the config server. Updates to config server during resharding may wait too long for oplog slot thus stalling replication on config server indefinitely.
* Fixed a resharding issue relating to RecipientStateMachine that caused the server to crash 
 
|PBM| 1.6.1 improvements include the following:

* Improved backup and point-in-time recovery routines alignment by using sequential ``delete-pitr``/``install-backup`` operations instead of in-memory backup intent. This fixes the inability of a backup to start.
* Added support for automated access to S3 buckets using an EC2 instance profile. When Percona Backup for MongoDB is deployed using an EC2 instance, EC2 environment variables and metadata are used for S3 authentication, saving you from explicitly specifying S3 credentials in the Percona Backup for MongoDB configuration file. This comes handy for architectures deployed using the services like Amazon EC2, kiam, kube2iam or irsa.
* Extended logging for ``pbm-agents``. This improves user experience with Percona Backup for MongoDB.


.. include:: .res/replace.txt