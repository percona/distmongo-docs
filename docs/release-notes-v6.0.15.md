# Percona Distribution for MongoDB 6.0.15 (2024-04-30)

[Installation](installation.md){.md-button}


Percona Distribution for MongoDB is a freely available MongoDB database alternative, giving you a single solution that combines enterprise components from the open source community, designed and tested to work together. The aim of Percona Distribution for MongoDB is to enable you to run and operate your
MongoDB efficiently with the data being consistently backed up.


Percona Distribution for MongoDB includes the following components:

* *Percona Server for MongoDB* is a fully compatible source-available, drop-in replacement
for MongoDB.

* *Percona Backup for MongoDB* is a distributed, low-impact solution for achieving
consistent backups of MongoDB sharded clusters and replica sets.

This release of Percona Distribution for MongoDB is based on the production release of [Percona Server for MongoDB 6.0.15-12](https://docs.percona.com/percona-server-for-mongodb/6.0/release_notes/6.0.15-12.html) and [Percona Backup for MongoDB 2.4.1](https://docs.percona.com/percona-backup-mongodb/release-notes/2.4.1.html).


## Release Highlights

A number of issues with sharded multi-document transactions in sharded clusters of 2 or more shards have been identified that result in returning incorrect results and missing reads and writes. The issues occur when the transactions’ metadata is being concurrently modified by using the following operations: `moveChunk`, `moveRange`, `movePrimary`, `renameCollection`, `drop`, and `reshardCollection`. 

The data is affected when using the following functionalities:

* Sharded multi-document transactions
* Queryable encryption

The issues are fully fixed in MongoDB  4.4.29, 5.0.25, 6.0.14, 7.0.8, and are included in Percona Server for MongoDB 4.4.29-28, 5.0.26-22, 6.0.14-11 and 7.0.8-5. If you are using sharded multi-document transactions or queryable encryption, upgrade to Percona Server for MongoDB 6.0.14-11 or later versions as soon as possible. Please follow closely the upstream recommendations for mitigation and remediation outlined in [Sharded multi-document transactions may perform operations using inconsistent sharding metadata](https://www.mongodb.com/alerts/critical-alert-sharding-txn-issues-apr-2024) alert.

Improvements and bug fixes, provided by MongoDB and included in Percona Distribution for MongoDB are the following:

* Changed the requirement to use exclusive write lock to intent exclusive write lock that doesn’t prevent reading from a collection during the $out stage when running the rename collection command.
* Fixed the issue with the replication lag by changing the `internalInsertMaxBatchSize` default value to 64.
* Fixed the issue with the match expression optimization for the $or to an $in rewrite by avoiding creating directly nested $or.
* Explicitly stated that the missing w field from write concern object will be filled with default write concern value

Percona Backup for MongoDB 2.4.x enhancements include the following:

* Ability to [delete backup snapshots of a specific type](https://docs.percona.com/percona-backup-mongodb/usage/delete-backup.html#__tabbed_2_3). For example, you can delete only logical backups which you might have created and no longer need. You can also check what exactly will be deleted with the new `--dry-run flag`. This improvement helps you better meet the organization's backup policy and improves your experience with cleaning up outdated data.
* Point-in-time recovery oplog slicing is now running in parallel with backup snapshots. This ensures that you can make a [point-in-time recovery](https://docs.percona.com/percona-backup-mongodb/usage/pitr-tutorial.html) to any timestamp from very large backups that take hours to make.
* Fixed the issue with failing incremental backups. It was caused by the backup metadata document reaching the maximum size limit of 16MB. The issue is fixed by introducing the new approach of handling the metadatada document: it no longer contains the list of backup files which is now stored separately on the storage and is read by PBM on demand. The new metadata handling approach applies to physical, incremental and shapshot-based backups.
