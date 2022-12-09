# Percona Distribution for MongoDB 4.4.17 (2022-11-10)

* **Date**

    November 10, 2022

* **Installation**

    [Install Percona Distribution for MongoDB](installation.md#install)

Percona Distribution for MongoDB is a freely available MongoDB database alternative, giving you a single solution that combines enterprise components from the open source community, designed and tested to work together. The aim of Percona Distribution for MongoDB is to enable you to run and operate your
MongoDB efficiently with the data being consistently backed up.

Percona Distribution for MongoDB includes the following components:

* *Percona Server for MongoDB* is a fully compatible source-available, drop-in replacement
for MongoDB.

* *Percona Backup for MongoDB* is a distributed, low-impact solution for achieving
consistent backups of MongoDB sharded clusters and replica sets.

This release of Percona Distribution for MongoDB is based on [Percona Server for MongoDB 4.4.17-17](https://www.percona.com/doc/percona-server-for-mongodb/4.4/release_notes/4.4.17-17.html) and [Percona Backup for MongoDB 2.0.2](https://www.percona.com/doc/percona-backup-mongodb/release-notes/2.0.2.html).

## Release Highlights

This release of Percona Distribution for MongoDB includes improvements and bug fixes, provided by MongoDB and included in Percona Server for MongoDB. The most notable from them are the following:

* [Data-at-rest encryption using the Key Management Interoperability Protocol (KMIP)](https://docs.percona.com/percona-server-for-mongodb/4.4/kmip.html) is generally available enabling you to use it in your production environment

* [$backupCursor and $backupCursorExtend aggregation stages](https://docs.percona.com/percona-server-for-mongodb/4.4/backup-cursor.html) functionality is generally available, enabling your application developers to use it for building custom backup solutions.

!!! note

    Percona provides [Percona Backup for MongoDB](https://docs.percona.com/percona-backup-mongodb/index.html) - the open source tool for consistent backups and restores in MongoDB sharded clusters.

* Fixed security vulnerability [CVE-2022-3602](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3602) for Percona Distribution for MongoDB 4.4.15-15 and higher installed from tarballs on Ubuntu 22.04.

* Detected and resolved table logging inconsistencies for WiredTiger tables at startup

* Fixed retryable writes on update and delete commands to not execute more than once if chunk is migrated and shard key pattern uses nested fields

* Verified that any unique indexes are prefixed by the new shard key pattern

* Prevented the use of `clientReadable` function in `AutoSplitVector` when reordering shard key fields

* Fixed the global time window state before performing the rollback to stable operation by updating the pinned timestamp as part of the transaction setup.

*Percona Backup for MongoDB* 2.0.x improvements are the following:

* Physical backups and restores are now generally available. This enables you to use them in production environments.

* [Data-at-rest encryption](https://docs.percona.com/percona-backup-mongodb/usage/restore.html#physical-restores-with-data-at-rest-encryption) is supported for physical backups and restores. This enables you to comply to data security regulations and save time on operating with large data sets.

* By [tracking physical restore progress](https://docs.percona.com/percona-backup-mongodb/usage/restore-progress.html), you have a clear picture of your restore operations and can timely react to any changes or issues.

* [Logical backups and restores can now be done selectively](https://docs.percona.com/percona-backup-mongodb/usage/selective-backup.html). This is a tech preview feature [^1] yet it enables you to work only with the desired subset of data and thereby save time on database maintenance and costs on storage.

*Percona Backup for MongoDB* 2.0.2 fixes the usability issues for applications operating with Percona Backup for MongoDB by providing the error messages for the status output in the JSON format.

[^1]: Tech Preview Features are not yet ready for enterprise use and are not included in support via SLA. They are included in this release so that users can provide feedback prior to the full release of the feature in a future GA release (or removal of the feature if it is deemed not useful). This functionality can change (APIs, CLIs, etc.) from tech preview to GA.