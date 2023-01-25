# Percona Distribution for MongoDB 6.0.4 (2023-01-30)

| Release date:     | January 30, 2023      |
|:------------------|:----------------------|
| **Installation**: | [Installing Percona Distribution for MongoDB](installation.md)


Percona Distribution for MongoDB is a freely available MongoDB database alternative, giving you a single solution that combines enterprise components from the open source community, designed and tested to work together. The aim of Percona Distribution for MongoDB is to enable you to run and operate your
MongoDB efficiently with the data being consistently backed up.


Percona Distribution for MongoDB includes the following components:

* *Percona Server for MongoDB* is a fully compatible source-available, drop-in replacement
for MongoDB.

* *Percona Backup for MongoDB* is a distributed, low-impact solution for achieving
consistent backups of MongoDB sharded clusters and replica sets.

This release of Percona Distribution for MongoDB is based on the production release of [Percona Server for MongoDB 6.0.4-3](https://docs.percona.com/percona-server-for-mongodb/6.0/release_notes/6.0.4-3.html) and [Percona Backup for MongoDB 2.0.3](https://docs.percona.com/percona-backup-mongodb/release-notes/2.0.3.html).


## Release Highlights
  
* Added availability on Red Hat Enterprise Linux 9 and compatible derivatives
* A Docker image for Percona Server for MongoDB (Release Candidate) is now available for ARM64 architectures. The support of ARM64 will be extended in subsequent releases. 

Bug fixes and improvements introduced in MongoDB and included in Percona Distribution for MongoDB are the following:

* Fixed the issue with incorrect projection parsing when a collection level collation is specified
* Changed the yielding policy of `dataSize` command to `YIELD_AUTO` for both when the command is called with `estimate:true` or `false`
* Fixed the issue with a BSON object exceeding the max allowed size during chunks merge in a shard 
* Fixed the incorrect behavior of the `mapReduce` command with single reduce optimization in sharded clusters

  
Percona Backup for MongoDB 2.0.3 improvements are the following:

* [Incremental physical backups](https://docs.percona.com/percona-backup-mongodb/usage/incremental-backup.html) enable you to reduce storage costs and facilitate data safety for business crucial data. By saving only the differences results in faster completion time and makes IB much smaller in size compared to full backups. As such, you save on storage space and data transfer in case of cloud setups. This is the [technical preview feature](https://docs.percona.com/percona-backup-mongodb/reference/glossary.html#technical-preview-feature), yet we welcome your feedback to improve the functionality.
* Now you can selectively back up and restore unsharded collections in sharded clusters. This extends the data set to work with.
* [Support of AWS IRSA (Identity Roles for Service Accounts)](https://docs.percona.com/percona-backup-mongodb/manage/automate-s3-access.html?h=irsa#iam-roles-for-service-accounts-irsa) credentials allows Percona Backup for MongoDB running in a pod to access the AWS storage using the IAM roles. This increases the security of your cloud infrastructure and enables you to control the access to it from a single place.

