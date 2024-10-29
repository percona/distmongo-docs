# Percona Distribution for MongoDB 6.0.18 ({{date.6_0_18}})

[Upgrade now](minor-upgrade.md){.md-button}


Percona Distribution for MongoDB is a freely available MongoDB database alternative, giving you a single solution that combines enterprise components from the open source community, designed and tested to work together. The aim of Percona Distribution for MongoDB is to enable you to run and operate your
MongoDB efficiently with the data being consistently backed up.


Percona Distribution for MongoDB includes the following components:

* *Percona Server for MongoDB* is a fully compatible source-available, drop-in replacement
for MongoDB.

* *Percona Backup for MongoDB* is a distributed, low-impact solution for achieving
consistent backups of MongoDB sharded clusters and replica sets.

This release of Percona Distribution for MongoDB is based on the production release of [Percona Server for MongoDB 6.0.18-15](https://docs.percona.com/percona-server-for-mongodb/6.0/release_notes/6.0.18-15.html) and [Percona Backup for MongoDB 2.7.0](https://docs.percona.com/percona-backup-mongodb/release-notes/2.7.0.html).


## Release Highlights

### Percona Server for MongoDB improvements

### Prevent master encryption key loss on the Vault server

Before Percona Server for MongoDB puts a new master encryption key to the Vault server as the versioned secret, it now checks if the secret's version reached the defined maximum (10 by default). This prevents the loss of the old secret and the master encryption key it stores on the Vault server. 

Make sure Percona Server for MongoDB has read permissions for the secret's metadata and the secrets engine configuration. To learn more, refer to the [documentation](https://docs.percona.com/percona-server-for-mongodb/6.0/vault.html#master-key-loss-prevention).

### Join Percona Squad

Participate in monthly SWAG raffles, get an early access to new product features and invite-only “ask me anything” sessions with database performance experts. Interested? Fill in the form at [squad.percona.com/mongodb](squad.percona.com/mongodb). 

#### Upstream Improvements

Improvements and bug fixes, provided by MongoDB and included in Percona Distribution for MongoDB are the following:

* Added current thread count to extra_info in serverStatus on Linux
* Disabled slot-based query execution engine (SBE query engine) in v6.0
* Ensured that JournalFlusher is run on ServiceContext it is bound to 
 
### Percona Backup for MongoDB 2.7.0 improvements:

#### Single authentication point for PBM running in Amazon EKS

Now PBM running in Amazon Elastic Kubernetes Service (EKS) can access AWS services using the credentials from the IAM role associated with the service account that is assigned to the Pod where PBM is running. Since with this improvement you don't have to pass the credentials to every individual Pods, the overall security of your infrastructure increases.

Consider the following limitation if you run Percona Operator for MongoDB: a restore does not work with this feature without the modification of default serviceAccount. It will be improved in future releases of the Operator to cover this case.

