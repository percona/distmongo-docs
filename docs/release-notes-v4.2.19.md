# Percona Distribution for MongoDB 4.2.19 (2022-03-29)

| **Release date** | March 29, 2022   |
| ---------------- | ------------------ |
| **Installation** | [Install Percona Distribution for MongoDB](installation.md)| 

Percona Distribution for MongoDB is a collection of solutions to run and operate your
MongoDB efficiently with the data being consistently backed up.

Percona Distribution for MongoDB includes the following components:

* *Percona Server for MongoDB* is a fully compatible source-available, drop-in replacement
for MongoDB.

* *Percona Backup for MongoDB* is a distributed, low-impact solution for achieving
consistent backups of MongoDB sharded clusters and replica sets.

This release of Percona Distribution for MongoDB is based on [Percona Server for MongoDB 4.2.19-19](https://docs.percona.com/percona-server-for-mongodb/4.2/release_notes/4.2.19-19.html) and [Percona Backup for MongoDB 1.6.1](https://docs.percona.com/percona-backup-mongodb/release-notes/1.6.1.html).

## Release Highlights

The bug fixes, provided by MongoDB and included in Percona Server for MongoDB 4.2.19-19 and Percona Distribution for MongoDB 4.2.19 are the following:

* Support of Keys Management Interoperability Protocol (KMIP). Thus, users can store encryption keys in their favorite KMIP-compatible key manager to set up encryption at rest. This is a tech preview feature [^1].

* Added the `repairShardedCollectionChunksHistory` command to restore history fields for some chunks. This aims to fix broken snapshot reads and distributed transactions.

* Fixed an issue with transaction coordinator crashing if the transaction is aborted when attempting to commit a transaction.

* Fixed the issue with the distributed transactions being in the prolonged prepared state that was caused by the  blocking of acquiring the WiredTiger write tickets by the transaction coordinator.

* Fixed an issue with an empty array for the `$nin` statement.

[^1]: Tech Preview Features are not yet ready for enterprise use and are not included in support via SLA. They are included in this release so that users can provide feedback prior to the full release of the feature in a future GA release (or removal of the feature if it is deemed not useful). This functionality can change (APIs, CLIs, etc.) from tech preview to GA.