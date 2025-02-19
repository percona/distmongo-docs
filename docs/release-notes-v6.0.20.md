# Percona Distribution for MongoDB 6.0.20 ({{date.6_0_20}})

[Upgrade now](minor-upgrade.md){.md-button}


Percona Distribution for MongoDB is a freely available MongoDB database alternative, giving you a single solution that combines enterprise components from the open source community, designed and tested to work together. The aim of Percona Distribution for MongoDB is to enable you to run and operate your
MongoDB efficiently with the data being consistently backed up.


Percona Distribution for MongoDB includes the following components:

* *Percona Server for MongoDB* is a fully compatible source-available, drop-in replacement
for MongoDB.

* *Percona Backup for MongoDB* is a distributed, low-impact solution for achieving
consistent backups of MongoDB sharded clusters and replica sets.

This release of Percona Distribution for MongoDB is based on the production release of [Percona Server for MongoDB 6.0.20-17](https://docs.percona.com/percona-server-for-mongodb/6.0/release_notes/6.0.20-17.html) and [Percona Backup for MongoDB 2.9.0](https://docs.percona.com/percona-backup-mongodb/release-notes/2.9.0.html).


## Release Highlights

### Improved security for Docker images

Docker images for Percona Server for MongoDB and Percona Backup for MongoDB are now based on Universal Base Image (UBI) version 9, which includes the latest security fixes. This makes the images compliant with the Red Hat certification and ensures the seamless work of containers on Red Hat OpenShift Container Platform.

### Amazon Linux 2023 support

Percona Distribution for MongoDB is now available and fully supported on Amazon Linux 2023 (AL23), simplifying its AWS deployment. You can safely run Percona Distribution for MongoDB on AL23 to build a secure, stable, high-performance environment for developing and running cloud applications, with seamless integration with various AWS services and development tools.  

### Upstream Improvements

Improvements and bug fixes, provided by MongoDB and included in Percona Distribution for MongoDB are the following:

* Exposed number of prepareUnique indexes in serverStatus
* Fixed the behavior for the $documents pipeline by ensuring that enabled query stats don't change the validation rules.
* Checked that a sharded explain command with a value set for the lsid's uid field in the inner command invocation will ignore the lsid field and succeed so long as the user is authorized to run the command being explained
* Made session refresh parameters configurable
* Enabled CRL (Certificate Revocation List) checking for the entire certificate chain when establishing an SSL connection.

### Percona Backup for MongoDB 2.9.0 improvements:

#### Centralized management of `pbm-agent` setup

You can now define a `pbm-agent` configuration in a single file and start the agent using it. The configuration includes the MongoDB connection URI, the custom log path and the number of parallel workers for a backup. In addition, you can adjust the log level on runtime without having to restart the `pbm-agent`.

This helps you keep all your `pbm-agent` setup in a single place and simplifies its management. 

Learn more about all the ways to configure custom log path in the [documentation](https://docs.percona.com/percona-backup-mongodb/manage/logpath.html)
