# Percona Distribution for MongoDB 6.0.21 ({{date.6_0_21}})

[Upgrade now](minor-upgrade.md){.md-button}


Percona Distribution for MongoDB is a freely available MongoDB database alternative, giving you a single solution that combines enterprise components from the open source community, designed and tested to work together. The aim of Percona Distribution for MongoDB is to enable you to run and operate your
MongoDB efficiently with the data being consistently backed up.


Percona Distribution for MongoDB includes the following components:

* *Percona Server for MongoDB* is a fully compatible source-available, drop-in replacement
for MongoDB.

* *Percona Backup for MongoDB* is a distributed, low-impact solution for achieving
consistent backups of MongoDB sharded clusters and replica sets.

This release of Percona Distribution for MongoDB is based on the production release of [Percona Server for MongoDB 6.0.21-18](https://docs.percona.com/percona-server-for-mongodb/6.0/release_notes/6.0.21-18.html) and [Percona Backup for MongoDB 2.9.1](https://docs.percona.com/percona-backup-mongodb/release-notes/2.9.1.html).

## Release Highlights

### Improved compatibility of Percona Server for MongoDB with MongoDB Enterprise Advanced for data-at-rest encryption using KMIP 

We have added the `security.kmip.useLegacyProtocol` configuration option to improve compatibility of Percona Server for MongoDB with MongoDB Enterprise Advanced. Now you can migrate from MongoDB Enterprise Advanced to Percona Server for MongoDB without having to modify the configuration file. Since Percona Server for MongoDB uses KMIP protocol version 1.0 by default, it ignores this option and prints the log message about it.


### Audit log improvements

Enjoy a better user experience with these improvements to audit logging:

* You can output logging information either to a syslog, a file or to print in the console. Now Percona Server for MongoDB correctly parses the specified destination and creates a logging file only if you explicitly defined the `file` as its value. This helps keep the system clean from unnecessary files

* By default, Percona Server for MongoDB saves the log file at the server's configured log path or to a directory from where `mongod` was started if the server's log path is undefined. You can also set a custom path to output a log file. For both cases, Percona Server for MongoDB checks if the audit log file can be opened for writing to ensure that logging information is written and available. 

### Compatibility with Amazon Linux 2023

We build and test Percona Distribution for MongoDB only on the latest versions of Amazon Linux 2023. Because of the way Amazon Linux updates their libraries, Percona Distribution for MongoDB 6.0.21 is compatible only with Amazon Linux 2023.7.x and won't work on Amazon Linux 2023.6.x and older. 

To upgrade to 6.0.21-18, make sure that you run Amazon Linux 2023.7.x. Use the [update instructions :octicons-link-external-16:](https://docs.aws.amazon.com/linux/al2023/ug/updating.html)  

### Upstream Improvements

Improvements and bug fixes, provided by MongoDB and included in Percona Distribution for MongoDB are the following:

* Re-enable autosplitting on the sessions collection when downgrading to version 5.0.x and setting the Feature Compatibility Version (FCV) to 5.0
* Fixed the issue with upgrading to a new FCV when there are range deletion tasks and no hashed shard key index by setting the number of orphan documents to zero
* Added redaction of the BSON command for "Plan executor error" warning logs to prevent the entire command text (possibly including PII) to end up in the logs
* Limited JSON recursion to 200 levels
* Removed acquisition of database and collection locks when acquiring the global lock in compaction
* Fixed the issue with MongoDB CPU usage spikes with a newer version of OpenSSL on RHEL 9

### Percona Backup for MongoDB 2.9.1 improvements:

* Fixed the issue that prevented PBM from taking physical backups in deployments using both MongoDB Community and Percona Server for MongoDB.

