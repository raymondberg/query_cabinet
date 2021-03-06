## Query Cabinet

Query Cabinet is intended to be a personalizeable repository of common database queries used by all kinds of teams. The goal is to provide transparency and clarity to common SQL query development by incorporating the documentation and running of queries in a common Query Cabinet.

To use, simply fork this repository and start building your own queries. Maintain in a personal or private repository, and share with friends or colleagues. Worried your query isn't doing what you think? Add a great description and submit a pull request to solicit feedback.

It also works to help coach people through the process of running queries on their own. It's not so hard! Query Cabinet lets you define and name parameters that team members can fill-in as they generate reports or run informational queries.

Enough infomercial. Let's install it!

## Installation

You must have Python 3.x installed and `pip` installed. Once ready, run these commands:

```
pip install -r requirements.txt
copy db.config.sample db.config
```

Debian: There's also a handy `bin/setup` script that will install requirements for you if you need them.

Then fill in your database values in the `db.config` file using your editor of choice. You're ready to query!

## Example Usage

Use `bin/create` and `bin/run` to create and run your queries, respectively. Here's an example:

```
→ .bin/qc create

What group will this query be under? example
What would you like the short name of your query to be? (e.g. book_count_today_by_hour) users_by_email_address
Please paste a detailed description of this query:  (end with ..) This query will retrieve all users in the database whose email matches the email address parameter..
Please paste your query template:  (end with ;) select *
> from users
> where email = '{email_address}';
> A parameter was detected with the name `email_address`
>         How would you describe this parameter? the email addressed used to filter the results

→ ./bin/qc run --query_group example --query_name users_by_email_address
the email address of the user you are seeking
Value for `email_address` >bam@example.com
Trying to connect to localhost:5432/postgres as postgres
Password:
Executing query..........COMPLETE
Wrote csv with 1 records
```

After this script ran (on our test database), you would have a file called `query_output.csv` with the following data:

```
id,name,email
1,BamBam Rubble,bam@example.com
```

## More Help

This library implements click so you can add `--help` to any command you run.

```
./bin/qc run --help
```

It's designed to be interactive when you don't have all the info, so you can also just try running `run` or `create` without parameters at all.

## This is just the beginning

More information coming soon on:
  - Query Parameterization
  - Multi-database configuration support
  - Easier test db setup
  - More ???

## Testing

This repo comes with a very basic test database to run the basic queries. To get started you'll need docker-compose.

```
  # Start dockerized database
  docker-compose up
```

Once up, the configuration in the sample config file will allow you to run test queries.
