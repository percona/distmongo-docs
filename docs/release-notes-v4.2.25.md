# Percona Distribution for MongoDB 4.2.25 (2024-02-08)

[Installation](installation.md)
 
Percona Distribution for MongoDB is a collection of solutions to run and operate your
MongoDB efficiently with the data being consistently backed up.

Percona Distribution for MongoDB includes the following components:

* *Percona Server for MongoDB* is a fully compatible source-available, drop-in replacement for MongoDB.

* *Percona Backup for MongoDB* is a distributed, low-impact solution for achieving
consistent backups of MongoDB sharded clusters and replica sets.

This release of Percona Distribution for MongoDB is based on [Percona Server for MongoDB 4.2.25-25](https://docs.percona.com/percona-server-for-mongodb/4.2/release_notes/4.2.25-25.html) and [Percona Backup for MongoDB 2.0.4](https://docs.percona.com/percona-backup-mongodb/release-notes/2.0.4.html).

## Release Highlights

* Optimized the construction of the balancer's collection distribution status histogram

* Fixed the query planner logic to distinguish parameterized queries in the presence of a partial index that contains logical expressions (`$and`, `$or`).

* Improved performance of updating the routing table and prevented blocking client requests during refresh for clusters with 1 million of chunks.

* Avoided traversing routing table in balancer split chunk policy

* Fixed the issue that caused the modification of the original ChunkMap vector during the chunk migration and that could lead to data loss. The issue affects MongoDB versions 4.4.25, 5.0.21, 6.0.10 through 6.0.11 and 7.0.1 through 7.0.2. Requires stopping all chunk merge activities and restarting all the binaries in the cluster (both `mongod` and `mongos`). 

Percona Backup for MongoDB 2.0.4 provides the ability to [specify the custom path to `mongod` binaries](https://docs.percona.com/percona-backup-mongodb/usage/restore#define-mongod-binary-location) to simplify the physical restore process.

## Packaging changes

Percona Distribution for MongoDB 4.2.25 is no longer available on Ubuntu 18.04 (Bionic Beaver). 


