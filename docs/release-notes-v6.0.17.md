# Percona Distribution for MongoDB 6.0.17 ({{date.6_0_17}})

[Upgrade now](minor-upgrade.md){.md-button}


Percona Distribution for MongoDB is a freely available MongoDB database alternative, giving you a single solution that combines enterprise components from the open source community, designed and tested to work together. The aim of Percona Distribution for MongoDB is to enable you to run and operate your
MongoDB efficiently with the data being consistently backed up.


Percona Distribution for MongoDB includes the following components:

* *Percona Server for MongoDB* is a fully compatible source-available, drop-in replacement
for MongoDB.

* *Percona Backup for MongoDB* is a distributed, low-impact solution for achieving
consistent backups of MongoDB sharded clusters and replica sets.

This release of Percona Distribution for MongoDB is based on the production release of [Percona Server for MongoDB 6.0.17-14](https://docs.percona.com/percona-server-for-mongodb/6.0/release_notes/6.0.17-14.html) and [Percona Backup for MongoDB 2.6.0](https://docs.percona.com/percona-backup-mongodb/release-notes/2.6.0.html).


## Release Highlights

### Percona Server for MongoDB improvements

#### Reduce mean time to resolve (MTTR) compromised encryption key incidents in KMIP

Starting with this release, Percona Server for MongoDB automatically activates all new master encryption keys at startup and periodically checks (polls) their status in a KMIP server. If a master encryption key for a node transitions to the state other than Active, the node reports an error and shuts down. This method allows security engineers to quickly identify which nodes require out-of-schedule master key rotation, such as in the case of compromised keys, without needing to rotate keys for the entire cluster. 

Learn more about key state polling from [the documentation](https://docs.percona.com/percona-server-for-mongodb/6.0/kmip.html#key-state-polling) 

#### Upstream Improvements

Improvements and bug fixes, provided by MongoDB and included in Percona Distribution for MongoDB are the following:

* Fixed the error in the `$merge` operation produced by the pipeline after the `$documents` stage by correcting the namespace for pipeline validation
* Provided a generic backportable solution not to miss top-level timeseries collection options
* Fixed performance issues by not copying a JavaScript “scope” object if a cached JsExecution object already exists in a query thread
* Allowed the `$match` aggregation stage to move ahead of mongoS change stream stages
* Fixed the issue with ineffective queuing of the pages by the eviction server in WoredTiger by introducing retries to find the ref in memory and thus avoiding returning NULL from the random descent function.
 
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

* Percona Distribution for MongoDB 6.0.17 is no longer supported for Ubuntu 18.04 (Bionic Beaver), Debian 10 and Red Hat Enterprise 7 and derivatives as these operating systems reached End-Of-Life.
