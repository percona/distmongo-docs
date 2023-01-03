# Minor upgrade of Percona Distribution for MongoDB

To receive bug fixes and feature enhancements that come with minor releases, keep your Percona Distribution for MongoDB upgraded to the latest version.

This document describes the upgrade from Percona repositories as the recommended method. 

Before the upgrade, we recommend to back up your data in order to be on the safe side if anything goes wrong.

## Prerequisites

1. [Update **percona-release**](https://docs.percona.com/percona-software-repositories/percona-release.html#updating-percona-release-to-the-latest-version) repository management tool to the latest version. This is required to install new version packages of Percona Distribution for MongoDB.

2. Enable the repository

    If you installed Percona Distribution for MongoDB from the Major release repository, this step is optional. This repository automatically includes new version packages and you receive a prompt for an upgrade from the package manager of your operating system.

    If you installed Percona Distribution for MongoDB from the Minor release repository, you must enable the new version repository (for example, `pdmdb-5.0.1`) to upgrade. We recommend to use the `setup` subcommand:

    ```{.bash data-prompt="$"}
    $ sudo percona-release setup pdmdb-5.0.1
    ```

## Procedure

Run the following commands as root or by using the **sudo** command.

### Stop the service

Stop Percona Server for MongoDB:

```{.bash data-prompt="$"}
$ sudo systemctl mongod stop
```

Stop **pbm-agent**:

```{.bash data-prompt="$"}
$ sudo systmectl pbm-agent stop
```

### Install new version packages

[Install a new version of Percona Distribution for MongoDB](installation.md) using the package manager of your operating system. 

### Restart the service

Start Percona Server for MongoDB:

```{.bash data-prompt="$"}
$ sudo systemctl mongod start
```

Start **pbm-agent**:

```{.bash data-prompt="$"}
$ sudo systmectl pbm-agent start
```
