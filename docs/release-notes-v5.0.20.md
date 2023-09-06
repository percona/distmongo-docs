# Percona Distribution for MongoDB 5.0.20 (2023-09-07)

[Installation](installation.md){.md-button}

Percona Distribution for MongoDB is a freely available MongoDB database alternative, giving you a single solution that combines enterprise components from the open source community, designed and tested to work together. The aim of Percona Distribution for MongoDB is to enable you to run and operate your
MongoDB efficiently with the data being consistently backed up.

Percona Distribution for MongoDB includes the following components:

* *Percona Server for MongoDB* is a fully compatible source-available, drop-in replacement
for MongoDB.

* *Percona Backup for MongoDB* is a distributed, low-impact solution for achieving
consistent backups of MongoDB sharded clusters and replica sets.

This release of Percona Distribution for MongoDB is based on [Percona Server for MongoDB 5.0.20-17](https://docs.percona.com/percona-server-for-mongodb/5.0/release_notes/5.0.20-17.html) and [Percona Backup for MongoDB 2.2.1](https://docs.percona.com/percona-backup-mongodb/release-notes/2.2.1.html).

## Release Highlights

The bug fixes and improvements provided by MongoDB and included in Percona Server for MongoDB are the following:

* Fixed the issue with the incorrect output for the query where the `$or` operator rewrites the `$elemMatch` extra condition.
* Fixed commit point propagation for exhaust oplog cursors.
* Blocked the `$group` min/max rewrite in timestamp if there is a non-meta filter. 
* Improved the reconciliation time and slow eviction for pages with lots of updates by avoiding saving the update chain when there are no updates to be written to the history store
* Fixed the Rollback to Stable behavior to skip tables with no time window information in the checkpoint.

Percona Backup for MongoDB 2.2.1 provides the ability to increase the wait time for physical backup to start. This eliminates the PBM failure when creating `$backupCursor` takes longer than usual.

