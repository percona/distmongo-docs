# Percona Distribution for MongoDB 7.0.7 (2024-04-04)

[Installation](installation.md){.md-button}

Percona Distribution for MongoDB is a freely available MongoDB database alternative, giving you a single solution that combines enterprise components from the open source community, designed and tested to work together. Its aim is to enable you to run and operate your
MongoDB efficiently with the data being consistently backed up.

Percona Distribution for MongoDB includes the following components:

* *Percona Server for MongoDB* is a fully compatible source-available, drop-in replacement
for MongoDB.

* *Percona Backup for MongoDB* is a distributed, low-impact solution for achieving
consistent backups of MongoDB sharded clusters and replica sets.

This release of Percona Distribution for MongoDB is based on the production release of [Percona Server for MongoDB 7.0.7-4](https://docs.percona.com/percona-server-for-mongodb/7.0/release_notes/7.0.7-4.html) and [Percona Backup for MongoDB 2.4.1](https://docs.percona.com/percona-backup-mongodb/release-notes/2.4.1.html).

!!! warning

    Due to [CVE-2024-1351](https://www.cve.org/CVERecord?id=CVE-2024-1351), in all MongoDB versions prior to 4.4.29, the `mongod` server allows incoming connections to skip peer certificate validation which results in untrusted connections to succeed. This issue occurs when the `mongod` is started with TLS enabled (`net.tls.mode` set to `allowTLS`, `preferTLS`, or `requireTLS`) and without a `net.tls.CAFile` configured. For details, see [SERVER-72839](https://jira.mongodb.org/browse/SERVER-72839).

    The issue is fixed upstream in versions 4.4.29, 5.0.25, 6.0.14 and 7.0.6 and in Percona Server for MongoDB 4.4.29-28, 5.0.25-22, 6.0.14-11 and 7.0.7-4. Now, configuring MongoDB to use TLS requires specifying the value for the `--tlsCAFile` flag, the `net.tls.CAFile `configuration option, or the `tlsUseSystemCA` parameter.

## Release Highlights

The bug fixes and improvements provided by MongoDB and included in Percona Distribution for MongoDB are the following:
  
Fixed the issue with missing peer certificate validation if neither CAFile nor clusterCAFile is provided.
Fixed the issue with multi-document transactions missing documents when the movePrimary operation runs concurrently by detecting placement conflicts in multi-document transactions.
* Changed the requirement to use exclusive write lock to intent exclusive write lock that doesn't prevent reading from a collection during the `$out` stage when running the rename collection command.
* Fixed the issue in SBE (Storage Based Encryption) engine with returning incorrect results when running queries/aggregations with a `$or` operator and the is enabled.
* Ensured sharding catalog is valid when acquiring collections in multi-document transactions.
* Fixed the issue with the `createIndex` command failing with the `StaleConfig` error if it is run from a stale mongos against a sharded non-empty collection.
* Improved the warning about persisted Read/Write Consern defaults on startup by showing it only for shard servers. 
* In mixed replica sets where nodes have different Feature Compatibilty Version value, the primary nodes reject the commands with parameters that cannot be recognized by other replica set members.
* Fixed the issue with exhaustive find command on config shard returning stale data by making shard registry use snapshot readConcern for reads from `config.shards` collection. 
  
Percona Backup for MongoDB 2.4.x improvements are the following:

* Ability to [delete backup snapshots of a specific type](https://docs.percona.com/percona-backup-mongodb/usage/delete-backup.html#__tabbed_2_3). For example, you can delete only logical backups which you might have created and no longer need. You can also check what exactly will be deleted with the new `--dry-run flag`. This improvement helps you better meet the organization's backup policy and improves your experience with cleaning up outdated data.
* Point-in-time recovery oplog slicing is now running in parallel with backup snapshots. This ensures that you can make a [point-in-time recovery](https://docs.percona.com/percona-backup-mongodb/usage/pitr-tutorial.html) to any timestamp from very large backups that take hours to make.
* Fixed the issue with failing incremental backups. It was caused by the backup metadata document reaching the maximum size limit of 16MB. The issue is fixed by introducing the new approach of handling the metadatada document: it no longer contains the list of backup files which is now stored separately on the storage and is read by PBM on demand. The new metadata handling approach applies to physical, incremental and shapshot-based backups.
