# Percona Distribution for MongoDB 4.4.28 (2024-02-07)


[Installation](installation.md){.md-button}

Percona Distribution for MongoDB is a freely available MongoDB database alternative, giving you a single solution that combines enterprise components from the open source community, designed and tested to work together. The aim of Percona Distribution for MongoDB is to enable you to run and operate your
MongoDB efficiently with the data being consistently backed up.

Percona Distribution for MongoDB includes the following components:

* *Percona Server for MongoDB* is a fully compatible source-available, drop-in replacement
for MongoDB.

* *Percona Backup for MongoDB* is a distributed, low-impact solution for achieving
consistent backups of MongoDB sharded clusters and replica sets.

This release of Percona Distribution for MongoDB is based on [Percona Server for MongoDB 4.4.28-27](https://docs.percona.com/percona-server-for-mongodb/4.4/release_notes/4.4.28-27.html) and [Percona Backup for MongoDB 2.3.1](https://docs.percona.com/percona-backup-mongodb/release-notes/2.3.1.html).


## Release Highlights

The bug fixes and improvements provided by MongoDB and included in Percona Server for MongoDB are the following:

* Fixed the issue with the data and the ShardVersion mismatch for sharded multi-document transactions by adding the check that no chunk has moved for the collection being referenced since transaction started
* Improved cluster balancer performance by optimizing the construction of the balancer's collection distribution status histogram
* Fixed the issue with blocking acquiring read/write tickets by TransactionCoordinator by validating that it can be recovered on step-up and can commit the transaction when there are no storage tickets available
* Investigated a solution to avoid a Full Time Diagnostic Data Capture (FTDC) mechanism to stall during checkpoint


Percona Backup for MongoDB 2.3.1 enhancements include the following:

* Support for Percona Server for MongoDB 7.0.x
* The ability to define custom endpoints when using Microsoft Azure Blob Storage for backups
* Improved PBM Docker image to allow making physical backups with the shared mongodb data volume
* Updated Golang libraries that include fixes for the security vulnerability CVE-2023-39325.

## Packaging changes

Percona Distribution for MongoDB 4.4.28 is no longer available on Ubuntu 18.04 (Bionic Beaver). 
