# Percona Distribution for MongoDB 4.2.22 (2022-09-06)


* **Date**

    September 6, 2022



* **Installation**

    [Install Percona Distribution for MongoDB](installation.md#install)


Percona Distribution for MongoDB is a collection of solutions to run and operate your
MongoDB efficiently with the data being consistently backed up.

Percona Distribution for MongoDB includes the following components:


* *Percona Server for MongoDB* is a fully compatible source-available, drop-in replacement
for MongoDB.


* *Percona Backup for MongoDB* is a distributed, low-impact solution for achieving
consistent backups of MongoDB sharded clusters and replica sets.

This release of Percona Distribution for MongoDB is based on [Percona Server for MongoDB 4.2.22-22](https://www.percona.com/doc/percona-server-for-mongodb/4.2/release_notes/4.2.22-22.html) and [Percona Backup for MongoDB 1.8.1](https://www.percona.com/doc/percona-backup-mongodb/release-notes/1.8.1.html).

## Release Highlights

!!! important

    With this release, the `kmipKeyIdentifier` option for data-at-rest encryption using the KMIP protocol (tech preview feature [^1]) is optional. This change serves to improve the user experience with Percona Server for MongoDB as the option names and behavior are similar to those of MongoDB Enterprise. However, if data-at-rest encryption using KMIP is configured, it is the breaking change because the standard upgrade procedure does not work. We do recommend to use the data-at-rest encryption using the KMIP protocol only for testing purposes until it is in the general availability stage.

    If you have configured data at rest encryption and it is absolutely necessary to upgrade your MongoDB instance, see the [upgrade instructions](https://docs.percona.com/percona-server-for-mongodb/4.2/kmip.html#minor-upgrade-of-psmdb-to-version-4-2-22-22-and-higher).

This release of Percona Distribution for MongoDB includes bug fixes and improvements provided by MongoDB and included in Percona Server for MongoDB and Percona Distribution for MongoDB. Among them are the following:

* Fixed an issue that occurred during the attempt to perform the collation-encoding of a document with a missing sort attribute. In this case an invariant is violated and `mongod` crashes.

* Fixed the TTLMonitor behavior to skip processing TTL indexes if the expireAfterSeconds option value is NaN (Not a Number).

* Changed the behavior of the ShardingTaskExecutorPoolSize parameter to control the connection pool size for config server replica set and shard nodes separately.

* Fixed the issue with bad projection created during dependency analysis due to string order assumption. It resulted in the `PathCollision` error. The issue is fixed by improving dependency analysis for projections by folding dependencies into ancestor dependencies where possible.

*Percona Backup for MongoDB* 1.8.1 improvements include the following:

* Fixed the restore failure on a different cluster. Now the UUID of users and system collections are not preserved when replaying the oplog.

* The Point-in-Time recovery chunks display is now consistent in both `pbm status` and `pbm list` outputs

## Packaging Notes

Debian 9 (“Stretch”) is no longer supported.

[^1]: Tech Preview Features are not yet ready for enterprise use and are not included in support via SLA. They are included in this release so that users can provide feedback prior to the full release of the feature in a future GA release (or removal of the feature if it is deemed not useful). This functionality can change (APIs, CLIs, etc.) from tech preview to GA.