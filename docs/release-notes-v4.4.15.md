# Percona Distribution for MongoDB 4.4.15 (2022-07-19)

| **Release date** | July 19, 2022   |
| ---------------- | ------------------ |
| **Installation** | [Install Percona Distribution for MongoDB](installation.md)|
    

Percona Distribution for MongoDB is a freely available MongoDB database alternative, giving you a single solution that combines enterprise components from the open source community, designed and tested to work together. The aim of Percona Distribution for MongoDB is to enable you to run and operate your
MongoDB efficiently with the data being consistently backed up.

Percona Distribution for MongoDB includes the following components:

* *Percona Server for MongoDB* is a fully compatible source-available, drop-in replacement
for MongoDB.

* *Percona Backup for MongoDB* is a distributed, low-impact solution for achieving
consistent backups of MongoDB sharded clusters and replica sets.

This release of Percona Distribution for MongoDB is based on [Percona Server for MongoDB 4.4.15-15](https://docs.percona.com/percona-server-for-mongodb/4.4/release_notes/4.4.15-15.html) and [Percona Backup for MongoDB 1.8.1](https://docs.percona.com/percona-backup-mongodb/release-notes/1.8.1.html).

## Release Highlights

This release of Percona Distribution for MongoDB includes improvements and bug fixes, provided by MongoDB and included in Percona Server for MongoDB. The most notable from them are the following:

* Support of multiple KMIP servers adds failover to your data-at-rest encryption setup.

* Ability to set KMIP client certificate password through a flag to simplify the migration from MongoDB Enterprise to Percona Server for MongoDB.

* Backported the check for user errors in case deadline on the migration destination manager is hit while waiting for a range to be cleared up. This prevents the balancer from getting blocked.

* Fixed the deadlock situation in cross shard transactions that could occur when the FCV (Feature Compatibility Version) was set after the “prepared” state of the transactions. That ended up with both the the [setFCV](https://www.mongodb.com/docs/manual/reference/command/setFeatureCompatibilityVersion/) thread and the TransactionCoordinator hung.

* A v6.0 backport fix to v4.4 that disables opportunistic read targeting (except for specified hedged reads) in order to prevent possible performance problems associated with uneven read distribution across the secondaries.

* Fixed an issue where competing/blocking network calls to the sync source can prevent selecting a new sync-source. This is resolved by canceling the ASIO session when SSL handshake times out.

*Percona Backup for MongoDB* 1.8.1 improvements include the following:

* Fixed the restore failure on a different cluster. Now the UUID of users and system collections are not preserved when replaying the oplog.

* The Point-in-Time recovery chunks display is now consistent in both `pbm status` and `pbm list` outputs

## Supported versions

Percona Distribution for MongoDB is now available on Ubuntu 22.04 (Jammy Jellyfish).
