# Percona Distribution for MongoDB 5.0.21 (2023-10-12)

[Installation](installation.md){.md-button}

Percona Distribution for MongoDB is a freely available MongoDB database alternative, giving you a single solution that combines enterprise components from the open source community, designed and tested to work together. The aim of Percona Distribution for MongoDB is to enable you to run and operate your
MongoDB efficiently with the data being consistently backed up.

Percona Distribution for MongoDB includes the following components:

* *Percona Server for MongoDB* is a fully compatible source-available, drop-in replacement
for MongoDB.

* *Percona Backup for MongoDB* is a distributed, low-impact solution for achieving
consistent backups of MongoDB sharded clusters and replica sets.

This release of Percona Distribution for MongoDB is based on [Percona Server for MongoDB 5.0.21-18](https://docs.percona.com/percona-server-for-mongodb/5.0/release_notes/5.0.21-18.html) and [Percona Backup for MongoDB 2.3.0](https://docs.percona.com/percona-backup-mongodb/release-notes/2.3.0.html).

## Release Highlights

The bug fixes and improvements provided by MongoDB and included in Percona Server for MongoDB are the following:

* Fixed the flow for converting a replica set into a sharded cluster by adding support for the drivers to communicate the signed `$clusterTimes` to shardsvr replica set before and after the `addShard` command is run
* Improved performance of updating the routing table and prevented blocking client requests during refresh for clusters with 1 million of chunks
* Fixed commit point propagation for exhaust oplog cursors during node sync
* Disallowed the retry to forcibly evict the page during reconciliation.

Percona Backup for MongoDB 2.3.0 enhancements include the following:

* The support for MongoDB 4.2 is deprecated. Existing functionality in Percona Backup for MongoDB remains compatible with MongoDB 4.2 and Percona Server for MongoDB 4.2; however, further enhancements and bug fixes are no longer tested against this version.
* The ability to [view the backup contents](https://docs.percona.com/percona-backup-mongodb/usage/describe-backup.html) improves troubleshooting of backups in environments where databases are often created and / or dropped. 
* The ability to [make physical backups in mixed deployments](https://docs.percona.com/percona-backup-mongodb/features/physical.html#physical-backups-in-mixed-deployments) with MongoDB Community and Percona Server for MongoDB (PSMDB) nodes streamlines the backup flow for organizations that are still evaluating or migrating their data sets against PSMDB.
* Improved validation of a base backup snapshot for point-in-time recovery aligns the recovery flow for logical and physical backups.

