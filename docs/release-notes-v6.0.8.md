# Percona Distribution for MongoDB 6.0.8 (2023-08-08)

| Release date:     | August 08, 2023      |
|:------------------|:----------------------|
| **Installation**: | [Installing Percona Distribution for MongoDB](installation.md)


Percona Distribution for MongoDB is a freely available MongoDB database alternative, giving you a single solution that combines enterprise components from the open source community, designed and tested to work together. The aim of Percona Distribution for MongoDB is to enable you to run and operate your
MongoDB efficiently with the data being consistently backed up.


Percona Distribution for MongoDB includes the following components:

* *Percona Server for MongoDB* is a fully compatible source-available, drop-in replacement
for MongoDB.

* *Percona Backup for MongoDB* is a distributed, low-impact solution for achieving
consistent backups of MongoDB sharded clusters and replica sets.

This release of Percona Distribution for MongoDB is based on the production release of [Percona Server for MongoDB 6.0.8-6](https://docs.percona.com/percona-server-for-mongodb/6.0/release_notes/6.0.8-6.html) and [Percona Backup for MongoDB 2.2.1](https://docs.percona.com/percona-backup-mongodb/release-notes/2.2.1.html).

!!! important

    **Changes to Chunk Management and Balancing**

    Several changes have been incrementally introduced within 6.0.x releases.

    * The name of a subset of data has changed from a `chunk` to a `range`. 
    * The data size has changed from 64 MB for a chunk to 128 MB for a range.

    * The balancer now distributes ranges based on the actual data size of collections. Formerly the balancer migrated and balanced data across shards based strictly on the number of chunks of data that exist for a collection across each shard. This, combined with the auto-splitter process could cause quite a heavy performance impact to heavy write environments. 

    * Ranges (formerly chunks) are no longer auto-split and will be split only when they move across shards for distribution purposes. The auto-splitter process is currently still available but it serves no purpose and does nothing active to the data. This also means that the Enable/Disable AutoSplit helpers should no longer be used. 

    The above changes are expected to lead to better performance overall going forward.

## Release Highlights

Bug fixes and improvements introduced in MongoDB and included in Percona Distribution for MongoDB are the following:

<<<<<<< HEAD

* The ability to [configure AWS STS endpoint](https://docs.percona.com/percona-server-for-mongodb/6.0/aws-iam-setup.html#configure-aws-sts-endpoint) improves authentication and connectivity with AWS services.
=======
* The ability to [configure AWS STS endpoint](https://docs.percona.com/percona-backup-mongodb/aws-iam-setup.html#configure-aws-sts-endpoint) improves authentication and connectivity with AWS services.
* The ability to configure AWS STS endpoint improves authentication and connectivity with AWS services.
>>>>>>> updated warning
* Enabled automatic of retry time series insert on `DuplicateKey` error.
* Added the CURL_OPT_SEEKFUNCTION to resend the data during multi-pass authentication.
* Prevented unnecessary logging of `WriteConflictExceptions` during the execution of a `findAndModify` command.
* Changed the index build behavior so that in-progress index builds are no longer accounted for `indexFreeStorageSize` when running dbStats.
* Prevented saving update chain when there were no updates to be written to the history store.
* Fixed the Rollback to Stable behavior to skip tables with no time window information in the checkpoint.
* Introduced the retry of multi-writes that hit StaleConfig due to critical section on the shard.
* Improved LDAP authentication by leaving authenticated users logged-in during LDAP server downtime.
* Fixed the issue with lost writes that occurred if recipient shard in chunk migration skips changes by having recipient shard to run the transferMods command on the donor shard primary until it learns there are no further changes.
* Fixed the issue with the server crash when restoring time series collection with authentication enabled by validating the `system.buckets.` namespace.

  
Percona Backup for MongoDB 2.2.x improvements include the following:

* Automated [Point-in-time recovery from physical backups](https://docs.percona.com/percona-backup-mongodb/usage/pitr-tutorial.html#from-physical-backups) offloads your DBAs on performing manual oplog replay on top of physical restore, ensures data consistency and unifies the user experience with PBM.  
* Owners of large data sets can now use PBM to [create external physical backups](https://docs.percona.com/percona-backup-mongodb/features/snapshots.html) as EBS snapshots or via a technology of their choice and restore from those backups with the data consistency guaranteed by PBM. Thereby they benefit from increased performance and reduced downtime, and are sure that their data remains consistent. This is the technical preview feature.
* The ability to [restore from physical and incremental backups to a new environment](https://docs.percona.com/percona-backup-mongodb/usage/restore.html#restoring-into-a-cluster-replica-set-with-a-different-name) with different replica set names extends the set of compatible environments for physical restore. 
* The ability to increase the wait time for physical backup to start eliminates the PBM failure when creating `$backupCursor` takes longer than usual.



