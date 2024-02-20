# Percona Distribution for MongoDB 6.0.13 (2024-02-20)

[Installation](installation.md){.md-button}


Percona Distribution for MongoDB is a freely available MongoDB database alternative, giving you a single solution that combines enterprise components from the open source community, designed and tested to work together. The aim of Percona Distribution for MongoDB is to enable you to run and operate your
MongoDB efficiently with the data being consistently backed up.


Percona Distribution for MongoDB includes the following components:

* *Percona Server for MongoDB* is a fully compatible source-available, drop-in replacement
for MongoDB.

* *Percona Backup for MongoDB* is a distributed, low-impact solution for achieving
consistent backups of MongoDB sharded clusters and replica sets.

This release of Percona Distribution for MongoDB is based on the production release of [Percona Server for MongoDB 6.0.13-10](https://docs.percona.com/percona-server-for-mongodb/6.0/release_notes/6.0.13-10.html) and [Percona Backup for MongoDB 2.3.1](https://docs.percona.com/percona-backup-mongodb/release-notes/2.3.1.html).

## Release Highlights

Bug fixes and improvements provided by MongoDB and included in Percona Distribution for MongoDB are the following:

* Percona Distribution for MongoDB packages are available for ARM64 architectures, enabling users to install it on premises. The ARM64 packages are available for the following operating systems:

    * Ubuntu 20.04 (Focal Fossa)
    * Ubuntu 22.04 (Jammy Jellyfish)
    * Red Hat Enterprise Linux 8 and compatible derivatives
    * Red Hat Enterprise Linux 9 and compatible derivatives


* Removed size storer entries upon collection drop
* Improved shard key index error messages by adding detailed information about an invalid index.
* Improved slow query logging by adding the duration between a write operation getting a commit timestamp and actually committing. This helps identify issues where operations are committing slowly and are slowing down replication.
* Fixed the issue with data and ShardVersion mismatch on sharded multi-document transactions by exposing the maxValidAfter timestamp alongside the shardVersion
* Fixed the issue with infinite loop during plan enumeration triggered by the `$or` queries



Percona Backup for MongoDB 2.3.1 enhancements include the following:

* Support for Percona Server for MongoDB 7.0.x
* The ability to define custom endpoints when using Microsoft Azure Blob Storage for backups
* Improved PBM Docker image to allow making physical backups with the shared mongodb data volume
* Updated Golang libraries that include fixes for the security vulnerability CVE-2023-39325.
