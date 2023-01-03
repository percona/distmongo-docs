# Percona Distribution for MongoDB 4.2.20 (2022-05-23)

| **Release date** | May 23, 2022   |
| ---------------- | ------------------ |
| **Installation** | [Install Percona Distribution for MongoDB](installation.md)|


Percona Distribution for MongoDB is a collection of solutions to run and operate your
MongoDB efficiently with the data being consistently backed up.

Percona Distribution for MongoDB includes the following components:


* *Percona Server for MongoDB* is a fully compatible source-available, drop-in replacement
for MongoDB.


* *Percona Backup for MongoDB* is a distributed, low-impact solution for achieving
consistent backups of MongoDB sharded clusters and replica sets.

This release of Percona Distribution for MongoDB is based on [Percona Server for MongoDB 4.2.20-20](https://docs.percona.com/percona-server-for-mongodb/4.2/release_notes/4.2.20-20.html) and [Percona Backup for MongoDB 1.7.0](https://docs.percona.com/percona-backup-mongodb/release-notes/1.7.0.html).

!!! important

    To make physical backups and restores, the `pbm-agent` must have the read/write access to the `dataDir`. If you use the filesystem-based backup storage, the `pbm-agent` must also have the read/write access to the backup directory. Therefore, starting from version 1.7.0, the user running the `pbm-agent` is changed from `pbm` to `mongod` in Percona Backup for MongoDB packages.

    To upgrade Percona Backup for MongoDB to version 1.7.0, do the following:

    1. Stop the `pbm-agent` process

    2. Upgrade new version packages

    3. Reload the `systemd` process to update the unit file with the following command:

       ```{.bash data-prompt="$"}
       $ sudo  systemctl daemon-reload
       ```

    4. If you have a filesystem-based backup storage, grant read/write permissions to the backup directory to the `mongod` user.

    5. Restart the `pbm-agent` process.

    If MongoDB runs under a different user than mongod (the default configuration for Percona Server for MongoDB), use the same user to run the `pbm-agent`. For filesystem-based storage, grant the read/write permissions to the backup directory for this user.

## Release Highlights

The bug fixes, provided by MongoDB and included in Percona Server for MongoDB 4.2.20-20 and Percona Distribution for MongoDB 4.2.20 are the following:

* Support of the master key rotation for data encrypted using the  Keys Management Interoperability Protocol (KMIP) protocol (tech preview feature [^1]). This improvement allows users to comply with regulatory standards for data security.

* Abort the WiredTiger transaction after releasing Client lock to avoid deadlocks.

* Check if the host has `cgroups` v2 enabled and read the memory limits according to that.

* Return the shutdown error as the top level error when batch writing command fails due to mongos shutdown.

* Fixed the double free state for the `DocumentSource::optimizeAt()` pipeline by making sure all pointers are in place before disposing the pipeline prefix.

*Percona Backup for MongoDB* 1.7.0 improvements include the following:

* Support for [physical backups](https://docs.percona.com/percona-backup-mongodb/backup-types.html#backup-types) in *Percona Server for MongoDB* starting from versions 4.2.15-16 and 4.4.6-8 and higher. Physical backups drastically speed up backup and restore performance for large databases (several terabytes). This is a technical preview feature [^1].

* [Oplog replay](https://docs.percona.com/percona-backup-mongodb/oplog-replay.html) from the arbitrary start time. This reduces Recovery Point Objective (RPO) when database is recovered from physical or storage-level backups.

* Ability to configure compression method and level for point-in-time recovery chunks and compression level for backups.

* Ability to configure the number of S3 multipart upload chunks to comply with various S3-compatible storage provider requirements.

* Ability to configure the number of upload retries. This facilitates data upload in case of unstable network connection.

[^1]: Tech Preview Features are not yet ready for enterprise use and are not included in support via SLA. They are included in this release so that users can provide feedback prior to the full release of the feature in a future GA release (or removal of the feature if it is deemed not useful). This functionality can change (APIs, CLIs, etc.) from tech preview to GA.

