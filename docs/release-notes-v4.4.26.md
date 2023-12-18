# Percona Distribution for MongoDB 4.4.26 (2023-12-18)


[Installation](installation.md){.md-button}

Percona Distribution for MongoDB is a freely available MongoDB database alternative, giving you a single solution that combines enterprise components from the open source community, designed and tested to work together. The aim of Percona Distribution for MongoDB is to enable you to run and operate your
MongoDB efficiently with the data being consistently backed up.

Percona Distribution for MongoDB includes the following components:

* *Percona Server for MongoDB* is a fully compatible source-available, drop-in replacement
for MongoDB.

* *Percona Backup for MongoDB* is a distributed, low-impact solution for achieving
consistent backups of MongoDB sharded clusters and replica sets.

This release of Percona Distribution for MongoDB is based on [Percona Server for MongoDB 4.4.26-25](https://docs.percona.com/percona-server-for-mongodb/4.4/release_notes/4.4.26-25.html) and [Percona Backup for MongoDB 2.3.1](https://docs.percona.com/percona-backup-mongodb/release-notes/2.3.1.html).


## Release Highlights

The bug fixes and improvements provided by MongoDB and included in Percona Server for MongoDB are the following:

* Added the ability to configure the retry behavior for Percona Server for MongoDB to connect to the KMIP server when using [data-at-rest encryption](https://docs.percona.com/percona-server-for-mongodb/4.4/kmip.html).
* [AWS IAM authentication](https://docs.percona.com/percona-server-for-mongodb/4.4/aws-iam.html) is now generally available, enabling you to use this functionality in production environments.

* Extended error message to provide more information why the index is invalid
* Fixed the conversion form string to doubleValue to not lose precision and be able to rountrip and retrieve the same value back.
* Improved the recipient shard behavior during the chunk migration to wait for changes to catalog cache to be persisted before the cloning phase.
* Fixed the issue that caused the modification of the original ChunkMap vector during the chunk migration and that could lead to data loss. The issue affects MongoDB versions 4.4.25, 5.0.21, 6.0.10 through 6.0.11 and 7.0.1 through 7.0.2. Requires stopping all chunk merge activities and restarting all the binaries in the cluster (both `mongod` and `mongos`). Please follow closely [the upstream recommendations](https://jira.mongodb.org/browse/SERVER-81966) how to remediate the issue.
* Improved the performance of the search_near WiredTiger cursor operation if many deleted items are present by reducing the cache size.


Percona Backup for MongoDB 2.3.1 enhancements include the following:

* Support for Percona Server for MongoDB 7.0.x
* The ability to define custom endpoints when using Microsoft Azure Blob Storage for backups
* Improved PBM Docker image to allow making physical backups with the shared mongodb data volume
* Updated Golang libraries that include fixes for the security vulnerability CVE-2023-39325.