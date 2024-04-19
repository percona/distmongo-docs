# Percona Distribution for MongoDB 7.0.8 (2024-04-24)

[Installation](installation.md){.md-button}

Percona Distribution for MongoDB is a freely available MongoDB database alternative, giving you a single solution that combines enterprise components from the open source community, designed and tested to work together. Its aim is to enable you to run and operate your
MongoDB efficiently with the data being consistently backed up.

Percona Distribution for MongoDB includes the following components:

* *Percona Server for MongoDB* is a fully compatible source-available, drop-in replacement
for MongoDB.

* *Percona Backup for MongoDB* is a distributed, low-impact solution for achieving
consistent backups of MongoDB sharded clusters and replica sets.

This release of Percona Distribution for MongoDB is based on the production release of [Percona Server for MongoDB 7.0.8-5](https://docs.percona.com/percona-server-for-mongodb/7.0/release_notes/7.0.8-5.html) and [Percona Backup for MongoDB 2.4.1](https://docs.percona.com/percona-backup-mongodb/release-notes/2.4.1.html).

## Release Highlights

!!! warning

    A number of issues with sharded multi-document transactions in sharded clusters of 2 or more shards have been identified that result in returning incorrect results and missing reads and writes. The issues occur when the transactions’ metadata is being concurrently modified by using the following operations: `moveChunk`, `moveRange`, `movePrimary`, `renameCollection`, `drop`, and `reshardCollection`. 
    The data is affected when using the following functionalities:

    * Sharded multi-document transactions
    * Queryable encryption

    The issues are fully fixed in MongoDB  4.4.29, 5.0.25, 6.0.14, 7.0.8, and are included in Percona Server for MongoDB 4.4.29-28, 5.0.26-22,6.0.14-11 and 7.0.8-5. If you are using sharded multi-document transactions or queryable encryption, upgrade to Percona Server for MongoDB 7.0.8-5 as soon as possible. Please follow closely the upstream recommendations for mitigation and remediation outlined in [Sharded multi-document transactions may perform operations using inconsistent sharding metadata](https://www.mongodb.com/alerts/critical-alert-sharding-txn-issues-apr-2024) alert.

The bug fixes and improvements provided by MongoDB and included in Percona Distribution for MongoDB are the following:
  
* Fixed the issue with reads returning incomplete results and mismatched sharding metadata when performed on sharded collections with the `readConcern: snapshot` and an `atClusterTime` values. The issue occurs if the following conditions apply to collections:

    * a collection is sharded at either the time of the read or at the atClusterTime.
    * a collection is dropped after the time atClusterTime
    * a collection is recreated as non-sharded after being dropped.

     The issue affects MongoDB versions 7.0.0 through 7.0.7. It is fixed upstream in 7.0.8 and is included in Percona Server for MongoDB 7.0.8-5. Follow the upstream recommendations for workaround and remediation.

* Fixed the issue with the replication lag by changing the `internalInsertMaxBatchSize` default value to 64
* Fixed NUMA (Non-Uniform Memory Access) nodes counting
* Ensured that query shape for `$documents` stage in an aggregation pipeline is unique on each execution.
  
Percona Backup for MongoDB 2.4.x improvements are the following:

* Ability to [delete backup snapshots of a specific type](https://docs.percona.com/percona-backup-mongodb/usage/delete-backup.html#__tabbed_2_3). For example, you can delete only logical backups which you might have created and no longer need. You can also check what exactly will be deleted with the new `--dry-run flag`. This improvement helps you better meet the organization's backup policy and improves your experience with cleaning up outdated data.
* Point-in-time recovery oplog slicing is now running in parallel with backup snapshots. This ensures that you can make a [point-in-time recovery](https://docs.percona.com/percona-backup-mongodb/usage/pitr-tutorial.html) to any timestamp from very large backups that take hours to make.
* Fixed the issue with failing incremental backups. It was caused by the backup metadata document reaching the maximum size limit of 16MB. The issue is fixed by introducing the new approach of handling the metadatada document: it no longer contains the list of backup files which is now stored separately on the storage and is read by PBM on demand. The new metadata handling approach applies to physical, incremental and shapshot-based backups.
