# Percona Distribution for MongoDB 4.4.16 (2022-08-30)

* **Date**

    August 30, 2022

* **Installation**

    [Install Percona Distribution for MongoDB](installation.md#install)

!!! warning

    Take caution when upgrading from earlier versions of v4.4.x to later versions of 4.4 or on to v5.0. See [SERVER-68511](https://jira.mongodb.org/browse/SERVER-68511) for more details.

Percona Distribution for MongoDB is a freely available MongoDB database alternative, giving you a single solution that combines enterprise components from the open source community, designed and tested to work together. The aim of Percona Distribution for MongoDB is to enable you to run and operate your
MongoDB efficiently with the data being consistently backed up.

Percona Distribution for MongoDB includes the following components:

* *Percona Server for MongoDB* is a fully compatible source-available, drop-in replacement
for MongoDB.

* *Percona Backup for MongoDB* is a distributed, low-impact solution for achieving
consistent backups of MongoDB sharded clusters and replica sets.

This release of Percona Distribution for MongoDB is based on [Percona Server for MongoDB 4.4.16-16](https://www.percona.com/doc/percona-server-for-mongodb/4.4/release_notes/4.4.16-16.html) and [Percona Backup for MongoDB 1.8.1](https://www.percona.com/doc/percona-backup-mongodb/release-notes/1.8.1.html).

## Release Highlights

This release of Percona Distribution for MongoDB includes improvements and bug fixes, provided by MongoDB and included in Percona Server for MongoDB. The most notable from them are the following:

* Fixed the server crash with the CLOCK_REALTIME set to forward by making the linearizable reads robust to primary catch-up and simultaneous stepdown.

* Improved handling of large/NaN (Not a Number) values for text index version.

* Improved handling of large/NaN (Not a Number) values for geo index version.

* Fixed the issue with bad projection created during dependency analysis due to string order assumption. It resulted in the `PathCollision` error. The issue is fixed by improving dependency analysis for projections by folding dependencies into ancestor dependencies where possible.

* Fixed the wrong key/value returning during search near when the key doesn’t exist.

* Adjusted the functioning of the range-deleter to prevent the balancer from getting blocked, hung, or ranges being scheduled behind other ranges.

* Fixed failed chunk migrations that could lead to recipient shard having different `config.transactions` records between primaries and secondaries - inconsistent data.

* Avoided server hang in chunk migration when a step-down occurs.

*Percona Backup for MongoDB* 1.8.1 improvements include the following:

* Fixed the restore failure on a different cluster. Now the UUID of users and system collections are not preserved when replaying the oplog.

* The Point-in-Time recovery chunks display is now consistent in both `pbm status` and `pbm list` outputs

## Packaging Notes

Debian 9 (“Stretch”) is no longer supported.
