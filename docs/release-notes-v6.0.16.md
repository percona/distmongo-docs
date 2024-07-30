# Percona Distribution for MongoDB 6.0.16 ({{date.6_0_16}})

[Upgrade now](minor-upgrade.md){.md-button}


Percona Distribution for MongoDB is a freely available MongoDB database alternative, giving you a single solution that combines enterprise components from the open source community, designed and tested to work together. The aim of Percona Distribution for MongoDB is to enable you to run and operate your
MongoDB efficiently with the data being consistently backed up.


Percona Distribution for MongoDB includes the following components:

* *Percona Server for MongoDB* is a fully compatible source-available, drop-in replacement
for MongoDB.

* *Percona Backup for MongoDB* is a distributed, low-impact solution for achieving
consistent backups of MongoDB sharded clusters and replica sets.

This release of Percona Distribution for MongoDB is based on the production release of [Percona Server for MongoDB 6.0.16-13](https://docs.percona.com/percona-server-for-mongodb/6.0/release_notes/6.0.16-13.html) and [Percona Backup for MongoDB 2.5.0](https://docs.percona.com/percona-backup-mongodb/release-notes/2.5.0.html).


## Release Highlights

Improvements and bug fixes, provided by MongoDB and included in Percona Distribution for MongoDB are the following:

* Fixed the issue with the aggregation pipeline in MongoDB when using the `$lookup stage` with a time series foreign collection using a correlated predicate
* Fixed the bug with the replaying oplog updates during mongosync by preserving the zero-valued timestamps.
* Improved handling of directoryPerDb and wiredTigerDirectoryForIndexes to not insert directories as key when reporting namespaces and UUIDs during a backup   
* Fixed the issue with performance regression by skipping in-memory deleted pages as part of the tree walk on each execution.
* Improved checkpoint cleanup and page eviction logic to prevent their unnecessary slowdown by evicting the internal pages read by the checkpoint like a regular page. 

Percona Backup for MongoDB 2.5.0 enhancements include the following:

* The ability to restore the desired subset of [custom databases with users and roles](https://docs.percona.com/percona-backup-mongodb/features/selective-backup.html#restore-a-database-with-users-and-roles) created in them. This is useful for deployments where each user has an individual database and authenticates against it.
* Previous versions of PBM required that `readConcern` and `writeConcern` are set to `majority` in MongoDB. In Percona Backup for MongoDB 2.5.0 you can now explicitly override this behavior, and thus, ensure backups in clusters configured to operate without the majority or lost it for some reason.

## Packaging notes

* Percona Distribution for MongoDB 6.0.16 is available on Ubuntu 24.04 (Noble Numbat)
