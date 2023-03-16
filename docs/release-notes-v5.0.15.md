# Percona Distribution for MongoDB 5.0.15 (2023-03-16)

| Release date:     | March 16, 2023      |
|:------------------|:----------------------|
| **Installation**: | [Installing Percona Distribution for MongoDB](installation.md) |

Percona Distribution for MongoDB is a freely available MongoDB database alternative, giving you a single solution that combines enterprise components from the open source community, designed and tested to work together. The aim of Percona Distribution for MongoDB is to enable you to run and operate your
MongoDB efficiently with the data being consistently backed up.

Percona Distribution for MongoDB includes the following components:

* *Percona Server for MongoDB* is a fully compatible source-available, drop-in replacement
for MongoDB.

* *Percona Backup for MongoDB* is a distributed, low-impact solution for achieving
consistent backups of MongoDB sharded clusters and replica sets.

This release of |pdmdb| is based on [Percona Server for MongoDB 5.0.15-13](https://docs.percona.com/percona-server-for-mongodb/5.0/release_notes/5.0.15-13.html) and [Percona Backup for MongoDB 2.0.4](https://docs.percona.com/percona-backup-mongodb/release-notes/2.0.4.html).

## Release Highlights

* The support for authentication using [AWS IAM](https://docs.percona.com/percona-server-for-mongodb/5.0/aws-iam.html) enables you to natively integrate Percona Server for MongoDB with AWS services, increase security of your infrastructure by setting up password-less authentication and offload your DBAs from managing different sets of secrets. This is the [technical preview feature](https://docs.percona.com/percona-server-for-mongodb/5.0/glossary.html#technical-preview-feature)
* Improved master key rotation for data at rest encrypted with HashiCorp Vault enables you to use the same secret key path on every server in your entire deployment thus significantly simplifying the secrets management and key rotation process.


The bug fixes and improvements provided by MongoDB and included in Percona Server for MongoDB 5.0.15-13 are the following:

* Fixed the issue with blocked networking calls preventing the oplog fetching process to re-establish the connection to an unresponsive sync-source node 
* Fixed the issue with incorrect projection parsing when a collection level collation is specified
* Changed the yielding policy of dataSize command to YIELD_AUTO for both when the command is called with estimate:true or false
* Disallowed creating the ‘admin’, ‘local’, and ‘config’ databases with alternative cases in names on sharded clusters
* Fixed the incorrect behavior of the `mapReduce` command with single reduce optimization in sharded clusters

Percona Backup for MongoDB 2.0.4 provides the ability to [specify the custom path to `mongod` binaries](https://docs.percona.com/percona-backup-mongodb/usage/restore#define-mongod-binary-location) to simplify the physical restore process.

