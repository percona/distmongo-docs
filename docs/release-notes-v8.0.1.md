# Percona Distribution for MongoDB 8.0.1 ({{8_0_1.date}})

[Installation](installation.md){.md-button}

We are pleased to announce the release of the Percona Distribution for MongoDB for the recent major version 8.0.x.

Percona Distribution for MongoDB is a freely available MongoDB database alternative, giving you a single solution that combines enterprise components from the open source community, designed and tested to work together. Its aim is to enable you to run and operate your
MongoDB efficiently with the data being consistently backed up.

Percona Distribution for MongoDB includes the following components:

* *Percona Server for MongoDB* is a fully compatible source-available, drop-in replacement
for MongoDB.

* *Percona Backup for MongoDB* is a distributed, low-impact solution for achieving
consistent backups of MongoDB sharded clusters and replica sets.

This release of Percona Distribution for MongoDB is based on the production release of [Percona Server for MongoDB 8.0.1-1](https://docs.percona.com/percona-server-for-mongodb/8.0/release_notes/8.0.1-1.html) and [Percona Backup for MongoDB 2.7.0](https://docs.percona.com/percona-backup-mongodb/release-notes/2.7.0.html).

## Upgrade considerations

Starting with version 8.0, Percona Server for MongoDB uses the upgraded TCMalloc to handle memory requests more efficiently. The use of TCMalloc requires enabling Transparent Huge Pages (THP) and per-CPU caches before you start Percona Server for MongoDB. Read more about TCMalloc in [MongoDB documentation :octicons-external-link-16:](https://www.mongodb.com/docs/manual/administration/tcmalloc-performance/)

## Release Highlights

### Percona Server for MongoDB improvements

#### Prevent master encryption key loss on the Vault server

Before Percona Server for MongoDB puts a new master encryption key to the Vault server as the versioned secret, it now checks if the secret's version reached the defined maximum (10 by default). This prevents the loss of the old secret and the master encryption key it stores on the Vault server. 

Make sure Percona Server for MongoDB has read permissions for the secret's metadata and the secrets engine configuration. To learn more, refer to the [documentation](../vault.md#master-key-loss-prevention).

#### Join Percona Squad

Participate in monthly SWAG raffles, get an early access to new product features and invite-only “ask me anything” sessions with database performance experts. Interested? Fill in the form at [squad.percona.com/mongodb](squad.percona.com/mongodb).
  
#### Upstream changes

##### Performance improvements

* Insert, update or delete multiple collections in one request with the new [`bulkWrite`](https://www.mongodb.com/docs/manual/reference/command/bulkWrite/#mongodb-dbcommand-dbcmd.bulkWrite) command. Executing this command results in faster performance.
* Benefit from faster read performance when working with time series collections. Instead of processing documents individually, MongoDB now operates the abstraction of blocks of data. This also results in faster `$group` queries.
* Query plan execution has been optimized to reduce the number of scans and fetches. For single indexed and single equality queries, MongoDB skips regular query planning and executions and uses the [EXPRESS stages](https://www.mongodb.com/docs/manual/reference/explain-results/#std-label-explain-results) which improves write performance.
* MongoDB now writes and applies oplog entries for every batch in parallel. The writer and applier threads now work asynchronously, which increases replication throughput for secondaries. 
* The upgraded upgraded TCMalloc version is now the default in MongoDB. Together with THP and per-CPU cache, it reduces memory fragmentation by 18% which is especially useful during peak loads.

##### Workload management

* Analyze query performance and manage the workload in your system using [query shapes](https://www.mongodb.com/docs/manual/core/query-shapes/#std-label-query-shapes). A query shape is a set of specifications to group similar queries together. For a query shape, you add query settings instead of index filters. Query settings are persistent meaning that they remain after the cluster restart thus saving you from rerunning them in your application. A query shape has the `queryShapeHash` parameter using which you can check if the operation causes excessive workload and deny it using operation rejection filters.

##### Scaling improvements

* To better optimize resources or distribute the data more evenly across the shards, you can now [move a single unsharded collection to any shard](https://www.mongodb.com/docs/manual/core/moveable-collections/#std-label-moveable-collections) with the new `moveCollection` command. This operation is going online and the collection data is fully available during the migration. This new way to move data is flexible and the read and write behavior when you query data is transparent.
* Ensuring even data distribution across shards in your cluster is crucial. Starting with MongoDB 5.0, you can reshard a collection using a different shard key, although this operation is time-consuming. In MongoDB 8.0, you can reshard a collection using the same shard key, significantly boosting performance. This is especially beneficial for large collections, reducing resharding time from days to several hours. You can dynamically reallocate your resources based on the workload. The process is online, so your operations run uninterrupted. The ability to add or remove shards without changing the shard key makes the whole resharding process straightforward. 
* You can now [unshard a collection](https://www.mongodb.com/docs/manual/tutorial/unshard-collection/#std-label-unshard-collection-task) if it should reside on a single shard or the collection requires resource isolation. You can either specify the desired shard or the collection will be moved onto the shard with the least load. 
* You can now save costs on additional computing resources when deploying a sharded cluster. The config server replica set can now store both the configuration and the database data. Such a deployment is recommended for small clusters and is especially useful for evaluating the cluster without having to pay extra costs.
* You can now make self-managed backups in sharded clusters using `mongodump`. Run the `fsync` command with the `lock` field set to `true` from `mongos` to lock each shard and prevent further writes. Then, run `fsynckUnlock` to unlock shards.

##### Logging improvements

You can now configure database profiler to log slow operations based on the time MongoDB actually spent processing that operation. This gives you more accuracy when you analyze performance. 

##### Security improvements

* You can now run range queries on encrypted fields, specifically for numeric data types and dates. This expands the range of use cases for queryable encryption, including accounting operations, healthcare, financial services, and other strictly regulated data operations where data safety is crucial.
* The logging format in MongoDB is now [OCSF](Open Cybersecurity Schema Framework) compliant. This simplifies integration with external monitoring systems since the log output is compatible out of the box. This saves the time of your developers enabling them to focus on other tasks.

### Percona Backup for MongoDB 2.7.0 improvements:

#### Single authentication point for PBM running in Amazon EKS

Now PBM running in Amazon Elastic Kubernetes Service (EKS) can access AWS services using the credentials from the IAM role associated with the service account that is assigned to the Pod where PBM is running. Since with this improvement you don't have to pass the credentials to every individual Pods, the overall security of your infrastructure increases.

Consider the following limitation if you run Percona Operator for MongoDB: a restore does not work with this feature without the modification of default serviceAccount. It will be improved in future releases of the Operator to cover this case.