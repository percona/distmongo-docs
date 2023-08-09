# Percona Distribution for MongoDB 4.4.23 (2023-08-14)


| **Release date** | August 14, 2023 |
|----------------- | ---------------- | 
| **Installation** | [Install Percona Distribution for MongoDB](installation.md) |

Percona Distribution for MongoDB is a freely available MongoDB database alternative, giving you a single solution that combines enterprise components from the open source community, designed and tested to work together. The aim of Percona Distribution for MongoDB is to enable you to run and operate your
MongoDB efficiently with the data being consistently backed up.

Percona Distribution for MongoDB includes the following components:

* *Percona Server for MongoDB* is a fully compatible source-available, drop-in replacement
for MongoDB.

* *Percona Backup for MongoDB* is a distributed, low-impact solution for achieving
consistent backups of MongoDB sharded clusters and replica sets.

This release of Percona Distribution for MongoDB is based on [Percona Server for MongoDB 4.4.23-22](https://docs.percona.com/percona-server-for-mongodb/4.4/release_notes/4.4.23-22.html) and [Percona Backup for MongoDB 2.2.1](https://docs.percona.com/percona-backup-mongodb/release-notes/2.2.1.html).


## Release Highlights

The bug fixes and improvements provided by MongoDB and included in Percona Server for MongoDB are the following:

* The ability to [configure AWS STS endpoint](https://docs.percona.com/percona-backup-mongodb/4.4/aws-iam-setup.html#configure-aws-sts-endpoint) improves authentication and connectivity with AWS services.


* Improved the behavior of systems without swap memory space by pinning program code segments in memory on `mongod` startup.
* Fixed the issue with the index uniqueness violations after upgrade from version 4.0 to versions 4.2 and later by falling back to old format partial index entry removal if an entry in the new format is not found in the index.
* Fixed performance issues of the aggregation framework by improving the `Value::hash_combine()` function operation on big-endian platforms 

Percona Backup for MongoDB 2.2.x improvements include the following:

* Automated [Point-in-time recovery from physical backups](https://docs.percona.com/percona-backup-mongodb/usage/pitr-tutorial.html#from-physical-backups) offloads your DBAs on performing manual oplog replay on top of physical restore, ensures data consistency and unifies the user experience with PBM.  
* Owners of large data sets can now use PBM to [create external physical backups](https://docs.percona.com/percona-backup-mongodb/features/snapshots.html) as EBS snapshots or via a technology of their choice and restore from those backups with the data consistency guaranteed by PBM. Thereby they benefit from increased performance and reduced downtime, and are sure that their data remains consistent. This is the technical preview feature.
* The ability to [restore from physical and incremental backups to a new environment](https://docs.percona.com/percona-backup-mongodb/usage/restore.html#restoring-into-a-cluster-replica-set-with-a-different-name) with different replica set names extends the set of compatible environments for physical restore. 
* The ability to increase the wait time for physical backup to start eliminates the PBM failure when creating `$backupCursor` takes longer than usual.