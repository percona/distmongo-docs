# Percona Distribution for MongoDB 6.0.9 (2023-09-14)

[Installation](installation.md){.md-button}


Percona Distribution for MongoDB is a freely available MongoDB database alternative, giving you a single solution that combines enterprise components from the open source community, designed and tested to work together. The aim of Percona Distribution for MongoDB is to enable you to run and operate your
MongoDB efficiently with the data being consistently backed up.


Percona Distribution for MongoDB includes the following components:

* *Percona Server for MongoDB* is a fully compatible source-available, drop-in replacement
for MongoDB.

* *Percona Backup for MongoDB* is a distributed, low-impact solution for achieving
consistent backups of MongoDB sharded clusters and replica sets.

This release of Percona Distribution for MongoDB is based on the production release of [Percona Server for MongoDB 6.0.9-7](https://docs.percona.com/percona-server-for-mongodb/6.0/release_notes/6.0.9-7.html) and [Percona Backup for MongoDB 2.2.1](https://docs.percona.com/percona-backup-mongodb/release-notes/2.2.1.html).

## Release Highlights

Bug fixes and improvements introduced in MongoDB and included in Percona Distribution for MongoDB are the following:

* Fixed the flow for converting a replica set into a sharded cluster b adding support for the drivers to communicate the signed $clusterTimes to shardsvr replica set before and after the `addShard` command is run 
* Fixed the issue with the incorrect output for the query where the $or operator rewrites the $elemMatch extra condition.
* Blocked the $group min/max rewrite in timestamp if there is a non-meta filter.
* Disallowed the retry to forcibly evict the page during reconciliation.

  
Percona Backup for MongoDB 2.2.1 provides the ability to increase the wait time for physical backup to start. This eliminates the PBM failure when creating `$backupCursor` takes longer than usual.



