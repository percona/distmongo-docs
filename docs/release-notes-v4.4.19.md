# Percona Distribution for MongoDB 4.4.19 (2023-03-20)


| **Release date** | March 20, 2023 |
|----------------- | ---------------- | 
| **Installation** | [Install Percona Distribution for MongoDB](installation.md) |

Percona Distribution for MongoDB is a freely available MongoDB database alternative, giving you a single solution that combines enterprise components from the open source community, designed and tested to work together. The aim of Percona Distribution for MongoDB is to enable you to run and operate your
MongoDB efficiently with the data being consistently backed up.

Percona Distribution for MongoDB includes the following components:

* *Percona Server for MongoDB* is a fully compatible source-available, drop-in replacement
for MongoDB.

* *Percona Backup for MongoDB* is a distributed, low-impact solution for achieving
consistent backups of MongoDB sharded clusters and replica sets.

This release of Percona Distribution for MongoDB is based on [Percona Server for MongoDB 4.4.19-19](https://docs.percona.com/percona-server-for-mongodb/4.4/release_notes/4.4.19-19.html) and [Percona Backup for MongoDB 2.0.4](https://docs.percona.com/percona-backup-mongodb/release-notes/2.0.4.html).


## Release Highlights

* The support for authentication using [AWS IAM](https://docs.percona.com/percona-server-for-mongodb/4.4/aws-iam.html) enables you to natively integrate Percona Server for MongoDB with AWS services, increase security of your infrastructure by setting up password-less authentication and offload your DBAs from managing different sets of secrets. This is a [technical preview feature](https://docs.percona.com/percona-server-for-mongodb/4.4/glossary.html#technical-preview-feature)
* Improved master key rotation for data at rest encrypted with HashiCorp Vault enables you to use the same secret key path on every server in your entire deployment thus significantly simplifying the secrets management and key rotation process.

The bug fixes and improvements provided by MongoDB and included in Percona Server for MongoDB 4.4.19-19 are the following:

* Fixed the issue with adding a new unencrypted node into an encrypted replica set by removing options which might not apply for this node.
* Changed the yielding policy of dataSize command to YIELD_AUTO for both when the command is called with estimate:true or false
* Fixed the incorrect behavior of the `mapReduce` command with single reduce optimization in sharded clusters
* Disallowed creating the ‘admin’, ‘local’, and ‘config’ databases with alternative cases in names on sharded clusters
* Fixed the issue with the upgrade from 4.2 to 4.4 when the UUID of the collections don't match by skipping the creation of range deletion documents upon upgrade

Percona Backup for MongoDB 2.0.4 provides the ability to [specify the custom path to `mongod` binaries](https://docs.percona.com/percona-backup-mongodb/usage/restore#define-mongod-binary-location) to simplify the physical restore process.

