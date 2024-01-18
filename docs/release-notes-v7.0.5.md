# Percona Distribution for MongoDB 7.0.5 (2024-01-23)

[Installation](installation.md){.md-button}

Percona Distribution for MongoDB is a freely available MongoDB database alternative, giving you a single solution that combines enterprise components from the open source community, designed and tested to work together. Its aim is to enable you to run and operate your
MongoDB efficiently with the data being consistently backed up.

Percona Distribution for MongoDB includes the following components:

* *Percona Server for MongoDB* is a fully compatible source-available, drop-in replacement
for MongoDB.

* *Percona Backup for MongoDB* is a distributed, low-impact solution for achieving
consistent backups of MongoDB sharded clusters and replica sets.

This release of Percona Distribution for MongoDB is based on the production release of [Percona Server for MongoDB 7.0.5-3](https://docs.percona.com/percona-server-for-mongodb/7.0/release_notes/7.0.5-3.html) and [Percona Backup for MongoDB 2.3.1](https://docs.percona.com/percona-backup-mongodb/release-notes/2.3.1.html).


## Release Highlights
  
* Removed size storer entries upon collection drop
* Explicitly stated that the missing `w` field from write concern object will be filled with default write concern value
* Fixed infinite loop in lockstep $or plan enumeration
* Investigated a solution to avoid a Full Time Diagnostic Data Capture (FTDC) mechanism to stall during checkpoint
  
Percona Backup for MongoDB 2.3.1 improvements are the following:

* Support for Percona Server for MongoDB 7.0.x
* The ability to define custom endpoints when using Microsoft Azure Blob Storage for backups
* Improved PBM Docker image to allow making physical backups with the shared mongodb data volume
* Updated Golang libraries that include fixes for the security vulnerability CVE-2023-39325.

