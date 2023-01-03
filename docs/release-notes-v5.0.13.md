# Percona Distribution for MongoDB 5.0.13 (2022-10-12)

| Release date:     | October 12, 2022      |
|:------------------|:----------------------|
| **Installation**: | [Installing Percona Distribution for MongoDB](installation.md) |


Percona Distribution for MongoDB is a freely available MongoDB database alternative, giving you a single solution that combines enterprise components from the open source community, designed and tested to work together. The aim of Percona Distribution for MongoDB is to enable you to run and operate your
MongoDB efficiently with the data being consistently backed up.

Percona Distribution for MongoDB includes the following components:

* *Percona Server for MongoDB* is a fully compatible source-available, drop-in replacement
for MongoDB.

* *Percona Backup for MongoDB* is a distributed, low-impact solution for achieving
consistent backups of MongoDB sharded clusters and replica sets.

This release of Percona Distribution for MongoDB is based on [Percona Server for MongoDB 5.0.13-11](https://docs.percona.com/percona-server-for-mongodb/5.0/release_notes/5.0.13-11.html) and [Percona Backup for MongoDB 2.0.1](https://docs.percona.com/percona-backup-mongodb/release-notes/2.0.1.html).

## Release Highlights

This release of Percona Distribution for MongoDB includes bug fixes and improvements provided by MongoDB and included in Percona Server for MongoDB 5.0.13-11. Among them are the following:

* [Data at rest encryption using the KMIP protocol](https://docs.percona.com/percona-server-for-mongodb/5.0/kmip.html) is now generally available, enabling you to use this functionality in production environments.

* *Percona Server for MongoDB* Docker container now includes the `mongodb-tools` utility set to align with the upstream container. This enables users to manage backup/restore operations of *Percona Server for MongoDB*.

* Fixed security vulnerability [CVE-2022-3602](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3602) for Percona Distribution for MongoDB 5.0.8 and higher installed from tarballs on Ubuntu 22.04.

* Updated exit code and status message during the master key rotation improves the user experience while using data-at-rest encryption with KMIP.

* Detected and resolved table logging inconsistencies for WiredTiger tables at startup

* Prevented the server from hanging in chunk migration when a step-down occurs.

* Fixed the issue with incorrect chunk size comparison during split by preventing the AutoSplitVector from using the clientReadable.

* Fixed the logger deadlock by adding a check against recursive logging

* Fixed the global time window state before performing the rollback to stable operation by updating the pinned timestamp as part of the transaction setup.

* Fixed the issue that could lead to data inconsistency by introducing the additional validation of field types for shard key patterns. Users should not modify the type (hashed or range) for the existing shard key fields

* Fixed the issue with failing resharding operation by introducing the start and end time metrics for resharding recipient

*Percona Backup for MongoDB* 2.0.1 improvements include the following:

* The support of [server-side encryption with customer-provided keys managed on the customer side (SSE-C)](https://docs.percona.com/percona-backup-mongodb/details/storage-configuration.html#server-side-encryption) enables you to use the S3-compatible storage of your choice thus preventing the vendor lock-in and saving your costs on AWS KMS (Key Management Service).

* The ability to [configure Percona Backup for MongoDB remotely](https://docs.percona.com/percona-backup-mongodb/manage/configure-remotely.html) simplifies its management when *Percona Backup for MongoDB* is deployed in Docker, Kubernetes or other cloud services.

* The ability to configure the sidecar mode for Percona Backup for MongoDB improves its operation as part of [Kubernetes Operator for MongoDB](https://docs.percona.com/percona-operator-for-mongodb/index.html).

* Troubleshooting enhancements:

>     * The ability to [define a timezone for logs and to follow the logs dynamically](https://docs.percona.com/percona-backup-mongodb/reference/pbm-commands.html#pbm-logs).

>     * Indication of arbiter nodes as non-supported ones in `pbm status` output
