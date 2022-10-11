.. _DISTMONGO-5.0.13:

================================================================================
*Percona Distribution for MongoDB* 5.0.13 (2022-10-12)
================================================================================

:Date: October 12, 2022
:Installation: :ref:`install`

Percona Distribution for MongoDB is a freely available MongoDB database alternative, giving you a single solution that combines enterprise components from the open source community, designed and tested to work together. The aim of Percona Distribution for MongoDB is to enable you to run and operate your
|mongodb| efficiently with the data being consistently backed up.

|pdmdb| includes the following components:

* |PSMDB| is a fully compatible source-available, drop-in replacement
  for MongoDB.
* |pbm| is a distributed, low-impact solution for achieving
  consistent backups of |mongodb| sharded clusters and replica sets.

This release of |pdmdb| is based on `Percona Server for MongoDB 5.0.13-11 <https://www.percona.com/doc/percona-server-for-mongodb/5.0/release_notes/5.0.13-11.html>`_ and `Percona Backup for MongoDB 2.0.1 <https://www.percona.com/doc/percona-backup-mongodb/release-notes/2.0.1.html>`_.

Release Highlights
==================

This release of |pdmdb| includes bug fixes and improvements provided by MongoDB and included in Percona Server for MongoDB 5.0.13-11. Among them are the following:

* `Data at rest encryption using the KMIP protocol <https://docs.percona.com/percona-server-for-mongodb/5.0/kmip.html>`_ is now generally available, enabling you to use this functionality in production environments.
* |PSMDB| Docker container now includes the ``mongodb-tools`` utility set to align with the upstream container. This enables users to manage backup/restore operations of |PSMDB|.
* Updated exit code and status message during the master key rotation improves the user experience while using data-at-rest encryption with KMIP.
* Detected and resolved table logging inconsistencies for WiredTiger tables at startup
* Prevented the server from hanging in chunk migration when a step-down occurs.
* Fixed the issue with incorrect chunk size comparison during split by preventing the `AutoSplitVector` from using the `clientReadable`.
* Fixed the logger deadlock by adding a check against recursive logging 
* Fixed the global time window state before performing the rollback to stable operation by updating the pinned timestamp as part of the transaction setup.
* Fixed the issue that could lead to data inconsistency by introducing the additional validation of field types for shard key patterns. Users should not modify the type (hashed or range) for the existing shard key fields 
* Fixed the issue with failing resharding operation by introducing the start and end time metrics for resharding recipient
  
|PBM| 2.0.1 improvements include the following:

* The support of `server-side encryption with customer-provided keys managed on the customer side (SSE-C) <https://docs.percona.com/percona-backup-mongodb/details/storage-configuration.html#server-side-encryption>`_ enables you to use the S3-compatible storage of your choice thus preventing the vendor lock-in and saving your costs on AWS KMS (Key Management Service).
* The ability to `configure Percona Backup for MongoDB remotely <https://docs.percona.com/percona-backup-mongodb/manage/configure-remotely.html>`_ simplifies its management when |PBM| is deployed in Docker, Kubernetes or other cloud services. 
* The ability to configure the sidecar mode for Percona Backup for MongoDB improves its operation as part of `Kubernetes Operator for MongoDB <https://docs.percona.com/percona-operator-for-mongodb/index.html>`_.
* Troubleshooting enhancements:
  
    - The ability to `define a timezone for logs and to follow the logs dynamically <https://docs.percona.com/percona-backup-mongodb/reference/pbm-commands.html#pbm-logs>`_.
    - Indication of arbiter nodes as non-supported ones in ``pbm status`` output

.. include:: .res/replace.txt