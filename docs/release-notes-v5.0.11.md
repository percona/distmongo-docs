# Percona Distribution for MongoDB 5.0.11 (2022-09-01)

| Release date:     | September 1, 2022      |
|:------------------|:----------------------|
| **Installation**: | [Installing Percona Distribution for MongoDB](installation.md) |


Percona Distribution for MongoDB is a freely available MongoDB database alternative, giving you a single solution that combines enterprise components from the open source community, designed and tested to work together. The aim of Percona Distribution for MongoDB is to enable you to run and operate your
MongoDB efficiently with the data being consistently backed up.

Percona Distribution for MongoDB includes the following components:

* *Percona Server for MongoDB* is a fully compatible source-available, drop-in replacement
for MongoDB.

* *Percona Backup for MongoDB* is a distributed, low-impact solution for achieving
consistent backups of MongoDB sharded clusters and replica sets.

This release of Percona Distribution for MongoDB is based on [Percona Server for MongoDB 5.0.11-10](https://docs.percona.com/percona-server-for-mongodb/5.0/release_notes/5.0.11-10.html) and [Percona Backup for MongoDB 1.8.1](https://docs.percona.com/percona-backup-mongodb/release-notes/1.8.1.html).

## Release Highlights

!!! important

    With this release, the `kmipKeyIdentifier` option for data-at-rest encryption using the KMIP protocol (tech preview feature [^1]) is optional. This change serves to improve the user experience with Percona Server for MongoDB as the option names and behavior are similar to those of MongoDB Enterprise. However, if data-at-rest encryption using KMIP is configured, it is the breaking change because the standard upgrade procedure does not work. We do recommend to use the data-at-rest encryption using the KMIP protocol only for testing purposes until it is in the general availability stage.

    If you have configured data at rest encryption and it is absolutely necessary to upgrade your MongoDB instance, see the [upgrade instructions](https://docs.percona.com/percona-server-for-mongodb/5.0/kmip.html#upgrade-kmip).

This release of Percona Distribution for MongoDB includes bug fixes and improvements provided by MongoDB and included in Percona Server for MongoDB and Percona Distribution for MongoDB. Among them are the following:

* Fixed the issue that caused inconsistency in sharding metadata when running the `movePrimary` command on the database that has the Feature Compatibility Version (FCV) set to 4.4 or earlier. Affects MongoDB versions 5.0.0 through 5.0.10 and MongoDB 6.0.0. Upgrade to the the fixed version of MongoDB 5.0.11 / Percona Server for MongoDB 5.0.11-10 as soon as possible.

* Improved handling of large/NaN (Not a Number) values for text index and geo index version.

* Prevented potential server crash or lost writes when a resharding retry happens after the primary node failover. This is fixed by refreshing the routing information on the primary node during resharding.

* Prevented rollback to stable operation to generate wrong updates/tombstones by always reading the cell time window information to decide the history store update visibility.

* Fixed memory leak in update restore eviction.

* Failed chunk migrations can lead to recipient shard having different config.transactions records between primaries and secondaries - inconsistent data.

* Fixed the issue when resharding a collection with a very large number of zones configured may have stalled on config server primary indefinitely.

* Fixed the issue when retrying a failed resharding operation after a primary failover could lead to server crash or lost writes.

* Prevented sharding DDL coordinator to lock itself out in distlock retry loop.

*Percona Backup for MongoDB* 1.8.1 improvements include the following:

* Fixed the restore failure on a different cluster. Now the UUID of users and system collections are not preserved when replaying the oplog.

* The Point-in-Time recovery chunks display is now consistent in both `pbm status` and `pbm list` outputs

## Packaging Notes

Debian 9 (“Stretch”) is no longer supported.

!!! admonition "See also"

    Percona Blog: [OS Platform End of Life (EOL) Announcement for Debian Linux 9](https://www.percona.com/blog/os-platform-end-of-life-eol-announcement-for-debian-linux-9/)

[^1]: Tech Preview Features are not yet ready for enterprise use and are not included in support via SLA. They are included in this release so that users can provide feedback prior to the full release of the feature in a future GA release (or removal of the feature if it is deemed not useful). This functionality can change (APIs, CLIs, etc.) from tech preview to GA.