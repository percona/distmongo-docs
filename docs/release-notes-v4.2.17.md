# Percona Distribution for MongoDB 4.2.17 (2021-10-11)

| **Release date** | October 11, 2021   |
| ---------------- | ------------------ |
| **Installation** | [Install Percona Distribution for MongoDB](installation.md)|


Percona Distribution for MongoDB is a collection of solutions to run and operate your
MongoDB efficiently with the data being consistently backed up.

Percona Distribution for MongoDB includes the following components:

* *Percona Server for MongoDB* is a fully compatible source-available, drop-in replacement
for MongoDB.

* *Percona Backup for MongoDB* is a distributed, low-impact solution for achieving
consistent backups of MongoDB sharded clusters and replica sets.

This release of Percona Distribution for MongoDB is based on [Percona Server for MongoDB 4.2.17-17](https://docs.percona.com/percona-server-for-mongodb/4.2/release_notes/4.2.17-17.html) and [Percona Backup for MongoDB 1.6.0](https://docs.percona.com/percona-backup-mongodb/release-notes/1.6.0.html).

## Release Highlights

The bug fixes, provided by MongoDB and included in Percona Server for MongoDB 4.2.17-17 and Percona Distribution for MongoDB 4.2.17 are the following:

* The `libsasl2` dependencies are added for DEB-based operating systems to enable GSSAPI and Kerberos authentication to work out-of-the box after installing MongoDB ([SERVER-54729](https://jira.mongodb.org/browse/SERVER-54729))

* The number of modify updates in WiredTiger is now limited to prevent performance issues ([WT-7776](https://jira.mongodb.org/browse/WT-7776))

* Errors related to proxy connections receive new error codes so that they don’t change the behavior of clients’ drivers ([SERVER-50549](https://jira.mongodb.org/browse/SERVER-50549))

* Pre-warming of connection pools in mongos tier ([SERVER-44152](https://jira.mongodb.org/browse/SERVER-44152))

* Improvements to Secondary slowdowns or hangs ([SERVER-34938](https://jira.mongodb.org/browse/SERVER-34938))

*Percona Backup for MongoDB* 1.6.0 improvements include the following:

* Support for Percona Server for MongoDB and MongoDB Community 5.0

* Point-in-time recovery enhancements: ability to restore from any previous snapshot and configurable span of oplog events

* JSON output for [PBM commands](https://docs.percona.com/percona-backup-mongodb/pbm-commands.html) to simplify interfacing PBM with applications
