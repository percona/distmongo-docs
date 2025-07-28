# Percona Distribution for MongoDB 7.0.22 ({{date.7_0_22}})

[Upgrade now](installation.md){.md-button}

Percona Distribution for MongoDB is a freely available MongoDB database alternative, giving you a single solution that combines enterprise components from the open source community, designed and tested to work together. Its aim is to enable you to run and operate your
MongoDB efficiently with the data being consistently backed up.

Percona Distribution for MongoDB includes the following components:

* *Percona Server for MongoDB* is a fully compatible source-available, drop-in replacement
for MongoDB.

* *Percona Backup for MongoDB* is a distributed, low-impact solution for achieving
consistent backups of MongoDB sharded clusters and replica sets.

This release of Percona Distribution for MongoDB is based on the production release of [Percona Server for MongoDB 7.0.22-12](https://docs.percona.com/percona-server-for-mongodb/7.0/release_notes/7.0.22-12.html) and [Percona Backup for MongoDB 2.10.0](https://docs.percona.com/percona-backup-mongodb/release-notes/2.10.0.html).

## Release Highlights

### Boost performance during cluster restore and scaling with file copy-based initial sync

You can now select how a newly added or a restored replica set member synchronizes the data from other members - via logical or file copy-based initial sync. File copy-based initial sync copies physical files from the source node. This sync method is faster than the logical one and it reduces your maintenance time on scaling your cluster.

This functionality is available in [Percona Server for MongoDB Pro](https://docs.percona.com/percona-server-for-mongodb/7.0/psmdb-pro.html) out of the box. Become a Percona Customer to enjoy all Pro features with little to no effort from your side.

### Packaging changes

Percona Distribution for MongoDB 7.0.22 is no longer supported on Ubuntu 20.04 (Focal Fossa) as this operating system has reached end of life. If you're not ready to upgrade to a newer Ubuntu OS but still want to update Percona Distribution for MongoDB, contact us! We're here to make your databases run better.
   
#### Upstream Improvements

* Fixed the issue with blocking Full Time Diagnostic Data Capture (FTDC) collection when checking the state of the `$backupCursor` by using atomic mode instead of a lock.
* Tracked nested paths through MatchExpression trees while encoding indexability for plan cache entries.
* Fixed the issue with missing documents when indexes on array fields contain subarrays by ensuring proper bounds when having nested arrays as predicates.
* Fixed an issue where change streams might incorrectly output a "drop" event during resharding or unsharding of a collection that is or was using zone sharding.
* Fixed the issue when a generation drain process in WiredTiger, which manages eviction of older data, encounters an issue and then resolves itself when the verbosity levels for eviction and checkpoint operations increase. The issue is fixed by restoring original verbosity levels for these operations.
* Prevented unauthorized access to data by improving the handling of the `$mergeCursors stage`. The issue affects MongoDB versions prior to 7.0.20 and is fixed upstream and included in Percona Server for MongoDB. We recommend users to upgrade to the latest version as soon as possible.
* Fixed the issue with incorrect handling of incomplete data that may prevent `mongos` from accepting new connections. The issue affects deployments configured to use a load balancer like HAProxy and affects Percona Server for MongoDB Server v6.0 prior to 6.0.23, Percona Server for MongoDB Server v7.0 prior to 7.0.20 and Percona Server for MongoDB Server v8.0 prior to 8.0.9. We recommend users to upgrade to the latest version as soon as possible.
* Fixed a race condition where a concurrent `upsert` operation could incorrectly fail with a `DuplicateKey` error instead of retrying as an update. With this fix, the upsert operation now correctly retries and applies the update when another operation inserts the document in parallel.
* Avoided retrying on duplicate key error for upserts in multidocument transactions.
* Fixed the issue with retrieving the wrong resolved namespace for a collection when there are multiple collections with the same name involved in a query.
* Fixed the issue with the shard processing the request bypassing the shard version protocol when a router is not aware of the collection being converted to timeseries.

### Percona Backup for MongoDB 2.10.0 improvements:

#### Fallback strategy for physical restores to ensure cluster operation

You can now configure PBM to use a fallback directory during a physical restores. At the restore start, PBM copies the `dbPath` contents to a special fallback directory. Then, the restore flows as usual. 

If the restore is successful, PBM deletes the fallback directory. If PBM detects that the cluster is in an error state, it triggers the fallback procedure and restores the cluster to its pre-restore state. This ensures your cluster remains operational, allowing you to retry the restore from another backup or perform other maintenance tasks.

Note that this functionality requires sufficient free disk space on each `mongod` instance to store the `dbPath` contents. At the restore start, PBM checks the available disk space and logs this information.

With this feature, your cluster can remain operational even if errors occur during a physical restore. For more details about the fallback flow and configuration, see the [documentation](https://docs.percona.com/percona-backup-mongodb/features/physical.html/#physical-restores-with-a-fallback-directory).

#### Improved security via the updated libraries

Percona Backup for MongoDB now uses the AWS SDK v2 for Go, which includes the latest features, security updates and improvements. This ensures the secure communication with AWS services.

#### Support of Google Cloud Client library

PBM now supports Google Cloud Client Library for interacting with Google Cloud Storage (GCS). PBM  communicates with Google Cloud Storage (GCS) via the JSON API and XML API. The preferred approach is to use the JSON API with a service account. HMAC keys are mainly used for compatibility with S3-style APIs. 

Note that PBM configuration for a backup storage now has a dedicated `gsc` subsection. If you're upgrading to PBM 2.10.0 or later, you must update your backup configuration accordingly:

1. Change the `storage.type` from `s3` to `gcs`.
2. Change the `storage.s3` section to `storage.gcs` and adjust the parameters accordingly.

Read more about available options in the [Google Cloud Storage (GCS)](https://docs.percona.com/percona-backup-mongodb/details/gcs.html) chapter.

This integration offers improved compatibility, more predictable API responses and better long-term support for GCS features.
