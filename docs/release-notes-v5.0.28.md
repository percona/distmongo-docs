# Percona Distribution for MongoDB 5.0.28 ({{date.5_0_28}})

[Upgrade now](minor-upgrade.md){.md-button}

Percona Distribution for MongoDB is a freely available MongoDB database alternative, giving you a single solution that combines enterprise components from the open source community, designed and tested to work together. The aim of Percona Distribution for MongoDB is to enable you to run and operate your
MongoDB efficiently with the data being consistently backed up.

Percona Distribution for MongoDB includes the following components:

* *Percona Server for MongoDB* is a fully compatible source-available, drop-in replacement
for MongoDB.

* *Percona Backup for MongoDB* is a distributed, low-impact solution for achieving
consistent backups of MongoDB sharded clusters and replica sets.

This release of Percona Distribution for MongoDB is based on [Percona Server for MongoDB 5.0.28-24](https://docs.percona.com/percona-server-for-mongodb/5.0/release_notes/5.0.28-24.html) and [Percona Backup for MongoDB 2.5.0](https://docs.percona.com/percona-backup-mongodb/release-notes/2.5.0.html).

## Release Highlights

### Percona Server for MongoDB improvements

#### Enhanced Telemetry for better product usage reporting

The enhanced telemetry feature provides comprehensive information about how it works, its components and metrics as well as updated methods how to disable telemetry. Read more in [Telemetry on Percona Server for MongoDB](https://docs.percona.com/percona-server-for-mongodb/5.0/telemetry.html)

#### Reduce mean time to resolve (MTTR) compromised encryption key incidents in KMIP

Starting with this release, Percona Server for MongoDB automatically activates the master encryption keys at startup and periodically checks (polls) their status in a KMIP server. If a master encryption key for a node is not in the Active state, the node reports an error and shuts down. This method allows security engineers to quickly identify which nodes require out-of-schedule master key rotation, such as in the case of compromised keys, without needing to rotate keys for the entire cluster. 

Learn more about key state polling from [documentation](https://docs.percona.com/percona-server-for-mongodb/5.0/kmip.html#key-state-polling) 

#### Easier dependency management with thinner tarballs 

Tarballs are now available for each supported operating system individually and no longer include built-in libraries. This change reduces the tarball download size and increases their security by simplifying updates for required dependencies. 

#### Upstream fixes

The bug fixes and improvements provided by MongoDB and included in Percona Distribution for MongoDB are the following:

* Prevented shutdown command from hanging
* Improved handling of queries with $elemMatch with empty path in plan enumerator in case an index is used on another predicate of the query
* Fixed performance issues by not copying a JavaScript "scope" object if a cached JsExecution object already exists in a query thread
* Fixed the issue with incorrect handling of 'unique' and 'sparse' parameters in index signature when comparing indexes.

### Percona Backup for MongoDB 2.5.0 improvements

* The ability to restore the desired subset of [custom databases with users and roles](https://docs.percona.com/percona-backup-mongodb/features/selective-backup.html#restore-a-database-with-users-and-roles) created in them. This is useful for deployments where each user has an individual database and authenticates against it.
* Previous versions of PBM required that `readConcern` and `writeConcern` are set to `majority` in MongoDB. In Percona Backup for MongoDB 2.5.0 you can now explicitly override this behavior, and thus, ensure backups in clusters configured to operate without the majority or lost it for some reason.