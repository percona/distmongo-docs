# Percona Distribution for MongoDB 5.0.29 ({{date.5_0_29}})

[Upgrade now](minor-upgrade.md){.md-button}

Percona Distribution for MongoDB is a freely available MongoDB database alternative, giving you a single solution that combines enterprise components from the open source community, designed and tested to work together. The aim of Percona Distribution for MongoDB is to enable you to run and operate your
MongoDB efficiently with the data being consistently backed up.

Percona Distribution for MongoDB includes the following components:

* *Percona Server for MongoDB* is a fully compatible source-available, drop-in replacement
for MongoDB.

* *Percona Backup for MongoDB* is a distributed, low-impact solution for achieving
consistent backups of MongoDB sharded clusters and replica sets.

This release of Percona Distribution for MongoDB is based on [Percona Server for MongoDB 5.0.29-25](https://docs.percona.com/percona-server-for-mongodb/5.0/release_notes/5.0.29-25.html) and [Percona Backup for MongoDB 2.6.0](https://docs.percona.com/percona-backup-mongodb/release-notes/2.6.0.html).

## Release Highlights

### Percona Server for MongoDB improvements

#### Prevent master encryption key loss on the Vault server

Before Percona Server for MongoDB puts a new master encryption key to the Vault server as the versioned secret, it now checks if the secret's version reached the defined maximum (10 by default). This prevents the loss of the old secret and the master encryption key it stores on the Vault server. 

Make sure Percona Server for MongoDB has read permissions for the secret's metadata and the secrets engine configuration. To learn more, refer to the [documentation](docs.percona.com/percona-server-for-mongodb/5.0/vault.html#master-key-loss-prevention).

#### Upstream fixes

The bug fixes and improvements provided by MongoDB and included in Percona Distribution for MongoDB are the following:

* Improved inserting unique index keys behavior by preventing an oplog application to check for duplicates on unique indexes except for when building an index and inserting into the `_id` index. 

* Fixed the deadlock between external abort and internal abort on index build.

* Provided a way for external tools to insert/update/upsert documents without triggering the "replace Timestamp(0,0) with current time" behavior by adding the "bypassEmptyTsReplacement" parameter to those operations.

* Avoided marking the page dirty for empty pages to prevent unnecessary page reconciliation.

### Percona Backup for MongoDB 2.6.0 improvements

#### Multiple storages for backups and restores

You can now define multiple storages for making backups and instruct PBM on what storage to save a backup: on the main or on any additional (external) one. This ability helps you save on data transfer costs when using cloud storage, as well as enables you to follow closely with the requirements of your organization’s backup policy.

To learn more, read [Multiple storages for backups](https://docs.percona.com/percona-backup-mongodb/features/multi-storage.html
).

#### Adjust node priority for point-in-time recovery oplog slicing

You can now redefine node priorities not only for making backups but also for point-in-time recovery oplog slices. For example, you can instruct PBM to save oplog slices either from a dedicated node or from nodes in the geographically closest location, thus reducing network latency. 

See the [Adjust node priority for oplog slices](https://docs.percona.com/percona-backup-mongodb/features/point-in-time-recovery.html#adjust-node-priority-for-oplog-slices) section for guidelines.

#### Additional control over PBM command execution

You can now configure the waiting time for a command execution by passing the `--wait-time` flag for the following commands:

* pbm config --force-resync --wait --wait-time="5m"
* pbm backup --wait --wait-time="5m"
* pbm restore --wait --wait-time="5m"
* pbm oplog-replay --wait --wait-time="5m"
* pbm profile add --sync --wait --wait-time="5m"
* pbm profile remove --wait --wait-time="5m"
* pbm profile sync --wait --wait-time="5m"
* pbm delete-pitr --older-than --wait --wait-time="5m"
* pbm cleanup --older-than --wait --wait-time="5m"

This way you have more control over the PBM operation. This enhancement also improves the error logging.

#### Snapshot-based physical backups are generally available

With [snapshot-based physical backups](https://docs.percona.com/percona-backup-mongodb//features/snapshots.html) now generally available, you can use this functionality in production environments and enjoy all the benefits of faster restores from snapshots with almost immediate access to data. 

#### Dropped support of MongoDB 4.4

Percona Backup for MongoDB drops support of MongoDB 4.4. Existing functionality in Percona Backup for MongoDB remains compatible with MongoDB 4.4 and Percona Server for MongoDB 4.4; however, further enhancements and bug fixes are no longer tested against this version.

## Packaging Changes

* Percona Distribution for MongoDB 5.0.29 is no longer supported for Debian 10 and Red Hat Enterprise 7 and derivatives as these operating systems reached End-Of-Life.