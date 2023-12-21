# Percona Distribution for MongoDB 5.0.23 (2023-12-21)

[Installation](installation.md){.md-button}

Percona Distribution for MongoDB is a freely available MongoDB database alternative, giving you a single solution that combines enterprise components from the open source community, designed and tested to work together. The aim of Percona Distribution for MongoDB is to enable you to run and operate your
MongoDB efficiently with the data being consistently backed up.

Percona Distribution for MongoDB includes the following components:

* *Percona Server for MongoDB* is a fully compatible source-available, drop-in replacement
for MongoDB.

* *Percona Backup for MongoDB* is a distributed, low-impact solution for achieving
consistent backups of MongoDB sharded clusters and replica sets.

This release of Percona Distribution for MongoDB is based on [Percona Server for MongoDB 5.0.23-20](https://docs.percona.com/percona-server-for-mongodb/5.0/release_notes/5.0.23-20.html) and [Percona Backup for MongoDB 2.3.1](https://docs.percona.com/percona-backup-mongodb/release-notes/2.3.1.html).

## Release Highlights

The bug fixes and improvements provided by MongoDB and included in Percona Server for MongoDB are the following:

* [AWS IAM authentication](https://docs.percona.com/percona-server-for-mongodb/5.0/aws-iam.html) is now generally available, enabling you to use this functionality in production environments.
* Improved the Primary Only Service interface to expose the primary state upon lookup
* Ensured that shard primaries commit a majority write before using new routing information from the config server.
* Fixed the rollback-to-stable behavior to read the newest transaction value only when it exists in the checkpoint.
* Hid expected eviction failures from the application and don't rollback in case of errors

Percona Backup for MongoDB 2.3.1 enhancements include the following:

* Support for Percona Server for MongoDB 7.0.x
* The ability to define custom endpoints when using Microsoft Azure Blob Storage for backups
* Improved PBM Docker image to allow making physical backups with the shared mongodb data volume
* Updated Golang libraries that include fixes for the security vulnerability CVE-2023-39325.
