# Percona Distribution for MongoDB 6.0.25 ({{date.6_0_25}})

[Upgrade now](minor-upgrade.md){.md-button}


Percona Distribution for MongoDB is a freely available MongoDB database alternative, giving you a single solution that combines enterprise components from the open source community, designed and tested to work together. The aim of Percona Distribution for MongoDB is to enable you to run and operate your
MongoDB efficiently with the data being consistently backed up.


Percona Distribution for MongoDB includes the following components:

* *Percona Server for MongoDB* is a fully compatible source-available, drop-in replacement
for MongoDB.

* *Percona Backup for MongoDB* is a distributed, low-impact solution for achieving
consistent backups of MongoDB sharded clusters and replica sets.

This release of Percona Distribution for MongoDB is based on the production release of [Percona Server for MongoDB 6.0.25-20](https://docs.percona.com/percona-server-for-mongodb/6.0/release_notes/6.0.25-20.html) and [Percona Backup for MongoDB 2.10.0](https://docs.percona.com/percona-backup-mongodb/release-notes/2.10.0.html).

## Release Highlights

This is the last release of Percona Distribution for MongoDB 6.0.x series.

### Upstream Improvements

Improvements and bug fixes, provided by MongoDB and included in Percona Distribution for MongoDB are the following:

The bug fixes, provided by MongoDB Community Edition and included in Percona Server for MongoDB, are the following:

* Added TTL properties to the output of listIndexes
* Added missing authorziation checks to document-source aggregation stages
* Fixed a race condition where a concurrent `upsert` operation could incorrectly fail with a `DuplicateKey` error instead of retrying as an update. With this fix, the upsert operation now correctly retries and applies the update when another operation inserts the document in parallel.
* Avoided retrying on duplicate key error for upserts in multidocument transactions
* Fixed the issue with missing documents when indexes on array fields contain subarrays by ensuring proper bounds when having nested arrays as predicates

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