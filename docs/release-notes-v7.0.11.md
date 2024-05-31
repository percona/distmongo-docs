# Percona Distribution for MongoDB 7.0.11 (2024-06-03)

[Installation](installation.md){.md-button}

Percona Distribution for MongoDB is a freely available MongoDB database alternative, giving you a single solution that combines enterprise components from the open source community, designed and tested to work together. Its aim is to enable you to run and operate your
MongoDB efficiently with the data being consistently backed up.

Percona Distribution for MongoDB includes the following components:

* *Percona Server for MongoDB* is a fully compatible source-available, drop-in replacement
for MongoDB.

* *Percona Backup for MongoDB* is a distributed, low-impact solution for achieving
consistent backups of MongoDB sharded clusters and replica sets.

This release of Percona Distribution for MongoDB is based on the production release of [Percona Server for MongoDB 7.0.11-6](https://docs.percona.com/percona-server-for-mongodb/7.0/release_notes/7.0.11-6.html) and [Percona Backup for MongoDB 2.5.0](https://docs.percona.com/percona-backup-mongodb/release-notes/2.5.0.html).

## Release Highlights

* Fixed the issue issue with the aggregation pipeline in MongoDB when using the `$lookup stage` with a time series foreign collection using a correlated predicate
* Improved the behavior of `applyOps: dropIndexes` command on MongoDB 7.x when no UUID is specified by completing it without dropping indexes
* Ensured that the index entry inconsistencies validation produces complete results and respects memory limits
* Fixed the issue with performance regression by skipping in-memory deleted pages as part of the tree walk on each execution.
* Fixed the issue with excessive logging on arbiter nodes by preventing running of FTDC (Full-Time Diagnostic Data Capture) stats on these nodes
* Improved the `disableTestParameters` behavior to not be dependent on when the `setParameters` is set.
* Improved handling of directoryPerDb and wiredTigerDirectoryForIndexes to not insert directories as key when reporting namespaces and UUIDs during a backup   
* Improved checkpoint cleanup and page eviction logic to prevent their unnecessary slowdown by evicting the internal pages read by the checkpoint like a regular page.
  
Percona Backup for MongoDB 2.5.0 improvements are the following:

* The ability to restore the desired subset of [custom databases with users and roles](https://docs.percona.com/percona-backup-mongodb/features/selective-backup.html#restore-a-database-with-users-and-roles) created in them. This is useful for deployments where each user has an individual database and authenticates against it.
* Previous versions of PBM required that `readConcern` and `writeConcern` are set to `majority` in MongoDB. In Percona Backup for MongoDB 2.5.0 you can now explicitly override this behavior, and thus, ensure backups in clusters configured to operate without the majority or lost it for some reason.
