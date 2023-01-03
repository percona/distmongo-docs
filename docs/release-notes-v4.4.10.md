# Percona Distribution for MongoDB 4.4.10 (2021-11-10)

| **Release date** | November 10, 2021  |
| ---------------- | ------------------ |
| **Installation** | [Install Percona Distribution for MongoDB](installation.md)|
    

Percona Distribution for MongoDB is a freely available MongoDB database alternative, giving you a single solution that combines enterprise components from the open source community, designed and tested to work together. The aim of Percona Distribution for MongoDB is to enable you to run and operate your
MongoDB efficiently with the data being consistently backed up.

Percona Distribution for MongoDB includes the following components:

* *Percona Server for MongoDB* is a fully compatible source-available, drop-in replacement
for MongoDB.

* *Percona Backup for MongoDB* is a distributed, low-impact solution for achieving
consistent backups of MongoDB sharded clusters and replica sets.

This release of Percona Distribution for MongoDB is based on [Percona Server for MongoDB 4.4.10-11](https://docs.percona.com/percona-server-for-mongodb/4.4/release_notes/4.4.10-11.html) and [Percona Backup for MongoDB 1.6.1](https://docs.percona.com/percona-backup-mongodb/release-notes/1.6.1.html).

## Release Highlights

This release of Percona Distribution for MongoDB includes bug fixes, provided by MongoDB and included in Percona Server for MongoDB. The most notable from  them are the following:

* Fixed delays in establishing egress connections on `mongos` due to delayed responses from `libcrypto.so`

*Percona Backup for MongoDB* 1.6.1 improvements include the following:

* Improved backup and point-in-time recovery routines alignment by using sequential `delete-pitr`/`install-backup` operations instead of in-memory backup intent. This fixes the inability of a backup to start.

* Added support for automated access to S3 buckets using an EC2 instance profile. When Percona Backup for MongoDB is deployed using an EC2 instance, EC2 environment variables and metadata are used for S3 authentication, saving you from explicitly specifying S3 credentials in the Percona Backup for MongoDB configuration file. This comes handy for architectures deployed using the services like Amazon EC2, kiam, kube2iam or irsa.

* Extended logging for `pbm-agents`. This improves user experience with Percona Backup for MongoDB.
