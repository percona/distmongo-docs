# Percona Distribution for MongoDB 4.4.9 (2021-10-07)

* **Date**

    October 7, 2021

* **Installation**

    [Installing Percona Distribution for MongoDB](https://www.percona.com/doc/percona-distribution-for-mongodb/4.4/installation.html)

Percona Distribution for MongoDB is a freely available MongoDB database alternative, giving you a single solution that combines enterprise components from the open source community, designed and tested to work together. The aim of Percona Distribution for MongoDB is to enable you to run and operate your
MongoDB efficiently with the data being consistently backed up.

Percona Distribution for MongoDB includes the following components:

* *Percona Server for MongoDB* is a fully compatible source-available, drop-in replacement
for MongoDB.

* *Percona Backup for MongoDB* is a distributed, low-impact solution for achieving
consistent backups of MongoDB sharded clusters and replica sets.

This release of Percona Distribution for MongoDB is based on [Percona Server for MongoDB 4.4.9-10](https://www.percona.com/doc/percona-server-for-mongodb/4.4/release_notes/4.4.9-10.html) and [Percona Backup for MongoDB 1.6.0](https://www.percona.com/doc/percona-backup-mongodb/release-notes/1.6.0.html).

!!! warning

    Beginning with MongoDB 4.4.2, several data impacting or corrupting bugs were introduced. Find the details below.

    These bugs are fixed in MongoDB 4.4.9. Percona Server for MongoDB 4.4.9-10, as part of Percona Distribution for MongoDB 4.4.9, includes the upstream fixes of these bugs.

    Please [upgrade](minor-upgrade.md#minor-upgrade) your Percona Distribution for MongoDB to version 4.4.9 as soon as possible.

!!! admonition "Additional upgrade planning note"

    If you are running MongoDB version 4.4.4 / Percona Distribution for MongoDB 4.4.4 or below, please skip upgrading to version 4.4.8 as that has been found to trigger the Duplicate Key error most consistently. Two WiredTiger bugs ([WT-7984](https://jira.mongodb.org/browse/WT-7984) and [WT-7995](https://jira.mongodb.org/browse/WT-7995)) are found in all versions of MongoDB 4.4.x except 4.4.1. Ideally, upgrade directly from version 4.4.1 to 4.4.9 to attempt to avoid those data impacting or corrupting bugs.

## Release Highlights

The bug fixes, provided by MongoDB and included in Percona Server for MongoDB and Percona Distribution for MongoDB are the following:


* [WT-7426](https://jira.mongodb.org/browse/WT-7426) - After upgrade to v4.4.5, startups or restarts can trigger WiredTigers RTS bug which can corrupt page metadata causing documents on affected pages to become invisible to MongoDB. This can lead to temporary query incorrectness or more likely a fatal error and inability to restart . Affects only MongoDB 4.4.5 and Percona Distribution for MongoDB 4.4.5.


* [SERVER-58936](https://jira.mongodb.org/browse/SERVER-58936) - Unique Index constraint violations possible - can cause duplicate data - fixed in version 4.4.8.


* [WT-7995](https://jira.mongodb.org/browse/WT-7995) - Checkpoint thread can read and persist inconsistent version of data to disk. Can cause Duplicate Key error on startup and prevent the node from starting. Unclean shutdowns can cause data inconsistency within documents, deleted documents to still exist, incomplete query results due to lost or inaccurate index entries, and/or missing documents. Affects MongoDB versions 4.4.2 through 4.4.8 and Percona Distribution for MongoDB 4.4.2 - 4.4.8 as well as MongoDB 5.0.0 through 5.0.2. Upgrade to fixed version of MongoDB 4.4.9 / Percona Distribution for MongoDB 4.4.9 as soon as possible.


* WT-7984 and associated Server Bug SERVER-60371.


* [WT-7984](https://jira.mongodb.org/browse/WT-7984) - Bug that could cause Checkpoint thread to omit a page of data. If the server experiences an unclean shutdown, an inconsistent checkpoint is used for recovery and causes data corruption. Fixed in version 4.4.9.
Requires the [validate](https://docs.mongodb.com/manual/reference/command/validate/)  command to be run and possible data remediation via complete initial sync.


* [SERVER-60371](https://jira.mongodb.org/browse/SERVER-60371) - Deployments, previously running version 4.4.8 and upgraded to 4.4.9, could still experience Duplicate Key error and Fatal assertion. Related to the two previous Wired Tiger bugs.

Requires the [validate](https://docs.mongodb.com/manual/reference/command/validate/)  command to be run and possible data remediation via complete initial sync. Currently under review.

*Percona Backup for MongoDB* 1.6.0 improvements include the following:


* Support for Percona Server for MongoDB and MongoDB Community 5.0


* Point-in-time recovery enhancements: ability to restore from any previous snapshot and configurable span of oplog events


* JSON output for PBM commands to simplify interfacing PBM with applications
