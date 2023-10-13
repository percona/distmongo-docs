# Percona Distribution for MongoDB 4.4.25 (2023-10-16)


[Installation](installation.md){.md-button}

Percona Distribution for MongoDB is a freely available MongoDB database alternative, giving you a single solution that combines enterprise components from the open source community, designed and tested to work together. The aim of Percona Distribution for MongoDB is to enable you to run and operate your
MongoDB efficiently with the data being consistently backed up.

Percona Distribution for MongoDB includes the following components:

* *Percona Server for MongoDB* is a fully compatible source-available, drop-in replacement
for MongoDB.

* *Percona Backup for MongoDB* is a distributed, low-impact solution for achieving
consistent backups of MongoDB sharded clusters and replica sets.

This release of Percona Distribution for MongoDB is based on [Percona Server for MongoDB 4.4.25-24](https://docs.percona.com/percona-server-for-mongodb/4.4/release_notes/4.4.25-24.html) and [Percona Backup for MongoDB 2.3.0](https://docs.percona.com/percona-backup-mongodb/release-notes/2.3.0.html).


## Release Highlights

The bug fixes and improvements provided by MongoDB and included in Percona Server for MongoDB are the following:

* Improved the balancer behavior to stop iterating collections when there are no more available shards
* Improved performance of updating the routing table and prevented blocking client requests during refresh for clusters with 1 million of chunks
* Fixed commit point propagation for exhaust oplog cursors.
* Disallowed the increase of oldest ID during recovery and let all the history store records return to the rollback to stable irrespective of global visibility.
* Disallowed saving the update chain when there are no updates to be written to the history store.

Percona Backup for MongoDB 2.3.0 enhancements include the following:

* The support for MongoDB 4.2 is deprecated. Existing functionality in Percona Backup for MongoDB remains compatible with MongoDB 4.2 and Percona Server for MongoDB 4.2; however, further enhancements and bug fixes are no longer tested against this version.
* The ability to [view the backup contents](https://docs.percona.com/percona-backup-mongodb/usage/describe-backup.html) improves troubleshooting of backups in environments where databases are often created and / or dropped. 
* The ability to [make physical backups in mixed deployments](https://docs.percona.com/percona-backup-mongodb/features/physical.html#physical-backups-in-mixed-deployments) with MongoDB Community and Percona Server for MongoDB (PSMDB) nodes streamlines the backup flow for organizations that are still evaluating or migrating their data sets against PSMDB.
* Improved validation of a base backup snapshot for point-in-time recovery aligns the recovery flow for logical and physical backups.
