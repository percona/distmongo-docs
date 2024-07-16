# Percona Distribution for MongoDB 7.0.12 (2024-07-18)

[Installation](installation.md){.md-button}

Percona Distribution for MongoDB is a freely available MongoDB database alternative, giving you a single solution that combines enterprise components from the open source community, designed and tested to work together. Its aim is to enable you to run and operate your
MongoDB efficiently with the data being consistently backed up.

Percona Distribution for MongoDB includes the following components:

* *Percona Server for MongoDB* is a fully compatible source-available, drop-in replacement
for MongoDB.

* *Percona Backup for MongoDB* is a distributed, low-impact solution for achieving
consistent backups of MongoDB sharded clusters and replica sets.

This release of Percona Distribution for MongoDB is based on the production release of [Percona Server for MongoDB 7.0.12-7](https://docs.percona.com/percona-server-for-mongodb/7.0/release_notes/7.0.12-7.html) and [Percona Backup for MongoDB 2.5.0](https://docs.percona.com/percona-backup-mongodb/release-notes/2.5.0.html).

## Release Highlights

* Upgraded the MozJS/SpiderMonkey engine that MongoDB uses to execute server-side JavaScript code within the database server to the latest ESR (Extended Support Release)
* Made sure an old heartbeat that is being processed when primary catchup starts does not cause the primary catchup to think it's already caught up
* Fixed the sorting of results produced by the `$unwind` aggregation with the array index field specified
* Marked the page clean in WiredTiger after re-instantiating the page with prepared updates to avoid reconciling the page every time

  
Percona Backup for MongoDB 2.5.0 improvements are the following:

* The ability to restore the desired subset of [custom databases with users and roles](https://docs.percona.com/percona-backup-mongodb/features/selective-backup.html#restore-a-database-with-users-and-roles) created in them. This is useful for deployments where each user has an individual database and authenticates against it.
* Previous versions of PBM required that `readConcern` and `writeConcern` are set to `majority` in MongoDB. In Percona Backup for MongoDB 2.5.0 you can now explicitly override this behavior, and thus, ensure backups in clusters configured to operate without the majority or lost it for some reason.
