# Percona Distribution for MongoDB 5.0.8 (2022-05-10)

| Release date:     | May 10, 2022      |
|:------------------|:----------------------|
| **Installation**: | [Installing Percona Distribution for MongoDB](installation.md) |


!!! warning

    We don’t recommend this version for the production use due to the critical issue with sharding metadata inconsistency: [SERVER-68511](https://jira.mongodb.org/browse/SERVER-68511). The metadata inconsistency is observed when running the `movePrimary` command on the database that has the Feature Compatibility Version (FCV) set to 4.4 or earlier. Affects MongoDB versions 5.0.0 through 5.0.10 and MongoDB 6.0.0. Upgrade to the fixed version of MongoDB 5.0.11 / Percona Server for MongoDB 5.0.11-10 or Percona Distribution for MongoDB 5.0.11 as soon as possible.

    Please follow closely the upstream recommendations outlined in [SERVER-68511](https://jira.mongodb.org/browse/SERVER-68511) to work around this issue and for the remediation steps, if your cluster is affected.

Percona Distribution for MongoDB is a freely available MongoDB database alternative, giving you a single solution that combines enterprise components from the open source community, designed and tested to work together. The aim of Percona Distribution for MongoDB is to enable you to run and operate your
MongoDB efficiently with the data being consistently backed up.

Percona Distribution for MongoDB includes the following components:

* *Percona Server for MongoDB* is a fully compatible source-available, drop-in replacement
for MongoDB.

* *Percona Backup for MongoDB* is a distributed, low-impact solution for achieving
consistent backups of MongoDB sharded clusters and replica sets.

This release of Percona Distribution for MongoDB is based on [Percona Server for MongoDB 5.0.8-7](https://www.percona.com/doc/percona-server-for-mongodb/5.0/release_notes/5.0.8-7.html) and [Percona Backup for MongoDB 1.7.0](https://www.percona.com/doc/percona-backup-mongodb/release-notes/1.7.0.html).

## Release Highlights

This release of Percona Distribution for MongoDB includes the support of master key rotation for data encrypted using the Keys Management Interoperability Protocol (KMIP) (tech preview [^1] feature). Thus, users can comply with regulatory standards for data security.

The most notable bug fixes, provided by MongoDB and included in Percona Server for MongoDB are the following:

* Fixed a bug that causes replication to stall on secondary replica set members in a sharded cluster handling cross-shard transactions. It is caused by WiredTger to erroneously return a write conflict when deciding if an update to a record is allowed. If MongoDB decides to retry the operation that caused the conflict in WiredTiger, it will enter an indefinite retry loop, and oplog application will stall on secondary nodes.

If this bug is hit, the secondary nodes will experience indefinite growth in replication lag. Restart the secondary nodes to resume replication.

This bug affects MongoDB 4.4.10 through 4.4.13 and 5.0.4 to 5.0.7.

Update to the latest version to avoid the secondary replication stall and lag issues.

* Fixed the issue with a commitQuorum incorrectly allowing non-voting buildIndexes:false nodes to be included in the commitQuorum count. It also fixed an error message relating to data-bearing nodes and quorum regarding to non-voting nodes.

* Fixed the order of backup blocks returned to the user to match the order retrieved from WiredTiger.

* Fixed the issue reporting an incorrect number of documents deleted from a capped collection when utilizing a collection scan to perform the delete action.

[^1]: Tech Preview Features are not yet ready for enterprise use and are not included in support via SLA. They are included in this release so that users can provide feedback prior to the full release of the feature in a future GA release (or removal of the feature if it is deemed not useful). This functionality can change (APIs, CLIs, etc.) from tech preview to GA.