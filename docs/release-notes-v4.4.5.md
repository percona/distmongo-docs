# Percona Distribution for MongoDB 4.4.5 (2021-04-19)

* **Date**

    April 19, 2021

* **Installation**

    [Installing Percona Distribution for MongoDB](https://www.percona.com/doc/percona-distribution-for-mongodb/4.4/installation.html)

!!! warning

    This version is not recommended for production use due to the following critical issues found in MongoDB Community: [WT-7984](https://jira.mongodb.org/browse/WT-7984) and [WT-7995](https://jira.mongodb.org/browse/WT-7995). They are fixed in [MongoDB 4.4.9 Community Edition](https://docs.mongodb.com/manual/release-notes/4.4/#4.4.9---sep-21--2021) and [Percona Server for MongoDB 4.4.9-10](https://www.percona.com/doc/percona-server-for-mongodb/4.4/release_notes/4.4.9-10.html). Percona Distribution for MongoDB 4.4.9 includes these fixes too.

    We recommend you to [upgrade](minor-upgrade.md#minor-upgrade) to Percona Distribution for MongoDB 4.4.9-10 as soon as possible and run the [validate](https://docs.mongodb.com/manual/reference/command/validate/) command on every collection on every replica set node.

Percona Distribution for MongoDB is a collection of solutions to run and operate your
MongoDB efficiently with the data being consistently backed up.

Percona Distribution for MongoDB includes the following components:

* *Percona Server for MongoDB* is a fully compatible source-available, drop-in replacement
for MongoDB.

* *Percona Backup for MongoDB* is a distributed, low-impact solution for achieving
consistent backups of MongoDB sharded clusters and replica sets.

This release of Percona Distribution for MongoDB is based on [Percona Server for MongoDB 4.4.5-7](https://www.percona.com/doc/percona-server-for-mongodb/4.4/release_notes/4.4.5-7.html) and [Percona Backup for MongoDB 1.4.1](https://www.percona.com/doc/percona-backup-mongodb/release-notes/1.4.1.html).
