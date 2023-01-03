# Percona Distribution for MongoDB 4.2.18 (2022-01-19)

| **Release date** | January 19, 2022   |
| ---------------- | ------------------ |
| **Installation** | [Install Percona Distribution for MongoDB](installation.md)|

Percona Distribution for MongoDB is a collection of solutions to run and operate your
MongoDB efficiently with the data being consistently backed up.

Percona Distribution for MongoDB includes the following components:

* *Percona Server for MongoDB* is a fully compatible source-available, drop-in replacement
for MongoDB.

* *Percona Backup for MongoDB* is a distributed, low-impact solution for achieving
consistent backups of MongoDB sharded clusters and replica sets.

This release of Percona Distribution for MongoDB is based on [Percona Server for MongoDB 4.2.18-18](https://docs.percona.com/percona-server-for-mongodb/4.2/release_notes/4.2.18-18.html) and [Percona Backup for MongoDB 1.6.1](https://docs.percona.com/percona-backup-mongodb/release-notes/1.6.1.html).

## Release Highlights

The bug fixes, provided by MongoDB and included in Percona Server for MongoDB 4.2.18-18 and Percona Distribution for MongoDB 4.2.18 are the following:

* Added the SetAllowMigrationsCommand command that prevents the balancer to migrate chunks on shards.

* Added a flag for the config server that prevents new migrations to start and ongoing migrations to commit.

* Improved the duplicate key handler behavior if the exact key already exists in the table. This fixes availability loss during the index build that was caused by checking many false duplicates.

* Added periodic clean up of logical sessions cache on arbiters

*Percona Backup for MongoDB* 1.6.1 improvements include the following:

* Improved backup and point-in-time recovery routines alignment by using sequential `delete-pitr`/`install-backup` operations instead of in-memory backup intent. This fixes the inability of a backup to start.

* Added support for automated access to S3 buckets using an EC2 instance profile. When Percona Backup for MongoDB is deployed using an EC2 instance, EC2 environment variables and metadata are used for S3 authentication, saving you from explicitly specifying S3 credentials in the Percona Backup for MongoDB configuration file. This comes handy for architectures deployed using the services like Amazon EC2, kiam, kube2iam or irsa.

* Extended logging for `pbm-agents`. This improves user experience with Percona Backup for MongoDB.
