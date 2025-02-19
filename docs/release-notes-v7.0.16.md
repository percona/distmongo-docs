# Percona Distribution for MongoDB 7.0.16 ({{date.7_0_16}})

[Upgrade now](installation.md){.md-button}

Percona Distribution for MongoDB is a freely available MongoDB database alternative, giving you a single solution that combines enterprise components from the open source community, designed and tested to work together. Its aim is to enable you to run and operate your
MongoDB efficiently with the data being consistently backed up.

Percona Distribution for MongoDB includes the following components:

* *Percona Server for MongoDB* is a fully compatible source-available, drop-in replacement
for MongoDB.

* *Percona Backup for MongoDB* is a distributed, low-impact solution for achieving
consistent backups of MongoDB sharded clusters and replica sets.

This release of Percona Distribution for MongoDB is based on the production release of [Percona Server for MongoDB 7.0.16-10](https://docs.percona.com/percona-server-for-mongodb/7.0/release_notes/7.0.16-10.html) and [Percona Backup for MongoDB 2.9.0](https://docs.percona.com/percona-backup-mongodb/release-notes/2.9.0.html).

## Release Highlights

### Improved security for Docker images

Docker images for Percona Server for MongoDB and Percona Backup for MongoDB are now based on Universal Base Image (UBI) version 9, which includes the latest security fixes. This makes the images compliant with the Red Hat certification and ensures the seamless work of containers on Red Hat OpenShift Container Platform.

### Amazon Linux 2023 support

Percona Distribution for MongoDB is now available and fully supported on Amazon Linux 2023 (AL23), simplifying its AWS deployment. You can safely run Percona Distribution for MongoDB on AL23 to build a secure, stable, high-performance environment for developing and running cloud applications, with seamless integration with various AWS services and development tools.  

#### Upstream Improvements

* Fixed time rounding for timeseries control block of dates prior to 1970
* Ensured there are no buckets with the same OID both within a stripe and across stripes for time-series collections 
* Made list databases consistent to a given storage snapshot
* Fixed the issue with tracking the archived bucket based on the minTime in the bucket registry for time series measurements by leaving the bucket’s minTime unchanged when performing user deletes/updates on it
* Handled multiple batches per bucket in time-series insert

### Percona Backup for MongoDB 2.9.0 improvements:

#### Centralized management of `pbm-agent` setup

You can now define a `pbm-agent` configuration in a single file and start the agent using it. The configuration includes the MongoDB connection URI, the custom log path and the number of parallel workers for a backup. In addition, you can adjust the log level on runtime without having to restart the `pbm-agent`.