# Percona Distribution for MongoDB 6.0.6 (2023-05-18)

| Release date:     | May 18, 2023      |
|:------------------|:----------------------|
| **Installation**: | [Installing Percona Distribution for MongoDB](installation.md)


Percona Distribution for MongoDB is a freely available MongoDB database alternative, giving you a single solution that combines enterprise components from the open source community, designed and tested to work together. The aim of Percona Distribution for MongoDB is to enable you to run and operate your
MongoDB efficiently with the data being consistently backed up.


Percona Distribution for MongoDB includes the following components:

* *Percona Server for MongoDB* is a fully compatible source-available, drop-in replacement
for MongoDB.

* *Percona Backup for MongoDB* is a distributed, low-impact solution for achieving
consistent backups of MongoDB sharded clusters and replica sets.

This release of Percona Distribution for MongoDB is based on the production release of [Percona Server for MongoDB 6.0.6-5](https://docs.percona.com/percona-server-for-mongodb/6.0/release_notes/6.0.6-5.html) and [Percona Backup for MongoDB 2.1.0](https://docs.percona.com/percona-backup-mongodb/release-notes/2.1.0.html).


## Release Highlights

Bug fixes and improvements introduced in MongoDB and included in Percona Distribution for MongoDB are the following:

* Fixed the handling of the read preference tags to respect their order and ignore other tags when all eligible replica set members are found.
* Allowed usage of clustered index in queries.
* Prevented a node in quiesce mode to win election.
* Fixed the issue with the `$avg` operator to return the sum instead of the average within a `$group` stage
* Fixed deadlock between `stepdown` and `restoring` locks after yielding when all read tickets exhausted
  
Percona Backup for MongoDB 2.1.0 improvements include the following:

* The general availability of [incremental physical backups](https://docs.percona.com/percona-backup-mongodb/features/incremental-backup.html) are now generally available enabling you to use them in production environments. Note that due to the changes in metadata files required for the restore, backups made with previous PBM versions are incompatible for the restore with PBM 2.1.0. 
* [Selective backup and restore of sharded collections](https://docs.percona.com/percona-backup-mongodb/features/selective-backup.html#sharded-collections) improves the management of a desired subset of data in sharded clusters and saves you extra costs on data storage and transfer. This is the tech preview feature due to some [known limitations](https://docs.percona.com/percona-backup-mongodb/features/selective-backup.html#known-limitations).
* The support of [parallel download of data chunks from the S3 storage](https://docs.percona.com/percona-backup-mongodb/usage/restore.html#parallel-data-download) improves the physical restore performance up to 7.5 times. Read more about the benchmarking in the [Speeding up MongoDB restores in PBM](https://www.percona.com/blog/speeding-up-database-restores-in-pbm) blog post by *Andrew Pogrebnoi*.
* Improved deletion of old backups and point-in-time recovery oplog chunks simplifies the automation of backup storage cleanup.
* The improved handling of master keys for data-at-rest encryption in Percona Server for MongoDB and the retrieval of the key ID/secret path by PBM from a backup simplifies the environment preparation for the physical restore and improves the restore flow.
* The support of AWS tokens for the access to the S3 storage improves the security of your infrastructure and the integration with applications that interact with AWS resources via tokens.



