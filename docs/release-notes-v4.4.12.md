# Percona Distribution for MongoDB 4.4.12 (2022-02-07)

* **Date**

    February 7, 2022

* **Installation**

    [Installing Percona Distribution for MongoDB](https://www.percona.com/doc/percona-distribution-for-mongodb/4.4/installation.html)

Percona Distribution for MongoDB is a freely available MongoDB database alternative, giving you a single solution that combines enterprise components from the open source community, designed and tested to work together. The aim of Percona Distribution for MongoDB is to enable you to run and operate your
MongoDB efficiently with the data being consistently backed up.

Percona Distribution for MongoDB includes the following components:

* *Percona Server for MongoDB* is a fully compatible source-available, drop-in replacement
for MongoDB.

* *Percona Backup for MongoDB* is a distributed, low-impact solution for achieving
consistent backups of MongoDB sharded clusters and replica sets.

This release of Percona Distribution for MongoDB is based on [Percona Server for MongoDB 4.4.12-12](https://www.percona.com/doc/percona-server-for-mongodb/4.4/release_notes/4.4.12-12.html) and [Percona Backup for MongoDB 1.6.1](https://www.percona.com/doc/percona-backup-mongodb/release-notes/1.6.1.html).

## Release Highlights

This release of Percona Distribution for MongoDB includes improvements and bug fixes, provided by MongoDB and included in Percona Server for MongoDB. The most notable from  them are the following:

* Defined a timeout for a health check process and throw an error when the process fails to complete within a timeout. This prevents health check to hang.

* Added the ability to transition through the valid states of the fault manager, and the interface to observer and log its state transitions.

* Fixed broken OP_QUERY exhaust cursor implementation

* Added the `repairShardedCollectionChunksHistory` command to restore `history` fields for some chunks. This aims to fix broken snapshot reads and distributed transactions.
