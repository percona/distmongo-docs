# Percona Distribution for MongoDB 4.2.24 (2023-03-09)

| **Release date** | March 9, 2023   |
| ---------------- | ------------------ |
| **Installation** | [Install Percona Distribution for MongoDB](installation.md)|
 
Percona Distribution for MongoDB is a collection of solutions to run and operate your
MongoDB efficiently with the data being consistently backed up.

Percona Distribution for MongoDB includes the following components:

* *Percona Server for MongoDB* is a fully compatible source-available, drop-in replacement for MongoDB.

* *Percona Backup for MongoDB* is a distributed, low-impact solution for achieving
consistent backups of MongoDB sharded clusters and replica sets.

This release of Percona Distribution for MongoDB is based on [Percona Server for MongoDB 4.2.24-24](https://docs.percona.com/percona-server-for-mongodb/4.2/release_notes/4.2.24-24.html) and [Percona Backup for MongoDB 2.0.4](https://docs.percona.com/percona-backup-mongodb/release-notes/2.0.4.html).

## Release Highlights

* Changed the yielding policy of `dataSize` command to `YIELD_AUTO` for both when the command is called with `estimate:true` or `false`

* Prevented dropping empty path component from elemMatch path during index selection

* Disallowed creating the 'admin', 'local', and 'config' databases with alternative cases in names on sharded clusters

* Made migration properly handle cases when shard key value modification also results to changes in chunk membership

Percona Backup for MongoDB 2.0.4 provides the ability to [specify the custom path to `mongod` binaries](https://docs.percona.com/percona-backup-mongodb/usage/restore#define-mongod-binary-location) to simplify the physical restore process.



