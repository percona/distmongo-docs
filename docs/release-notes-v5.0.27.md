# Percona Distribution for MongoDB 5.0.27 (2024-06-19)

[Installation](installation.md){.md-button}

Percona Distribution for MongoDB is a freely available MongoDB database alternative, giving you a single solution that combines enterprise components from the open source community, designed and tested to work together. The aim of Percona Distribution for MongoDB is to enable you to run and operate your
MongoDB efficiently with the data being consistently backed up.

Percona Distribution for MongoDB includes the following components:

* *Percona Server for MongoDB* is a fully compatible source-available, drop-in replacement
for MongoDB.

* *Percona Backup for MongoDB* is a distributed, low-impact solution for achieving
consistent backups of MongoDB sharded clusters and replica sets.

This release of Percona Distribution for MongoDB is based on [Percona Server for MongoDB 5.0.27-23](https://docs.percona.com/percona-server-for-mongodb/5.0/release_notes/5.0.27-23.html) and [Percona Backup for MongoDB 2.5.0](https://docs.percona.com/percona-backup-mongodb/release-notes/2.5.0.html).


## Release Highlights

The bug fixes and improvements provided by MongoDB and included in Percona Server for MongoDB are the following:

* Changed the default value of `internalInsertMaxBatchSize` to 64 to avoid replication lag if the insert operations are slow
* Fixed the issue issue with the aggregation pipeline in MongoDB when using the `$lookup stage` with a time series foreign collection using a correlated predicate
* Explicitly stated that the missing `w` field from write concern object will be filled with default write concern value
* Fixed the bug with the replaying oplog updates during mongosync by preserving the zero-valued timestamps
* Fixed the issue with resumable index build sorter files not to be synced on shutdown

Percona Backup for MongoDB 2.5.0 improvements are the following:

* The ability to restore the desired subset of [custom databases with users and roles](https://docs.percona.com/percona-backup-mongodb/features/selective-backup.html#restore-a-database-with-users-and-roles) created in them. This is useful for deployments where each user has an individual database and authenticates against it.
* Previous versions of PBM required that `readConcern` and `writeConcern` are set to `majority` in MongoDB. In Percona Backup for MongoDB 2.5.0 you can now explicitly override this behavior, and thus, ensure backups in clusters configured to operate without the majority or lost it for some reason.