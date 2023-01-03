# Percona Distribution for MongoDB 4.4.2 (2020-12-01)

| **Release date** | December 1, 2020   |
| ---------------- | ------------------ |
| **Installation** | [Install Percona Distribution for MongoDB](installation.md)|

 
!!! warning

    This version is not recommended for production use due to the following critical issues found in MongoDB Community: [WT-7984](https://jira.mongodb.org/browse/WT-7984) and [WT-7995](https://jira.mongodb.org/browse/WT-7995). They are fixed in [MongoDB 4.4.9 Community Edition](https://docs.mongodb.com/manual/release-notes/4.4/#4.4.9---sep-21--2021) and [Percona Server for MongoDB 4.4.9-10](https://docs.percona.com/percona-server-for-mongodb/4.4/release_notes/4.4.9-10.html). Percona Distribution for MongoDB 4.4.9 includes these fixes too.

    We recommend you to [upgrade](minor-upgrade.md#minor-upgrade) to Percona Distribution for MongoDB 4.4.9-10 as soon as possible and run the [validate](https://docs.mongodb.com/manual/reference/command/validate/) command on every collection on every replica set node.

Percona Distribution for MongoDB is a collection of solutions to run and operate your
MongoDB efficiently with the data being consistently backed up.

Percona Distribution for MongoDB includes the following components:

* *Percona Server for MongoDB* is a fully compatible source-available, drop-in replacement
for MongoDB.

* *Percona Backup for MongoDB* is a distributed, low-impact solution for achieving
consistent backups of MongoDB sharded clusters and replica sets.

This release of Percona Distribution for MongoDB is based on [Percona Server for MongoDB 4.4.2-4](https://docs.percona.com/percona-server-for-mongodb/4.4/release_notes/4.4.2-4.html) and [Percona Backup for MongoDB 1.3.4](https://docs.percona.com/percona-backup-mongodb/release-notes/1.3.4.html).
