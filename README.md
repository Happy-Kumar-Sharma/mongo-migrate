# **Mongrate**
A lightweight MongoDB migration tool.

---
[![Documentation](https://readthedocs.org/projects/mongrate/badge/?version=latest)](https://readthedocs.org/projects/mongrate/badge/?version=latest)
[![PyPI version](https://badge.fury.io/py/mongrate.svg)](https://badge.fury.io/py/mongrate.svg)
[![Python](https://img.shields.io/pypi/pyversions/mongrate.svg)](https://pypi.org/project/mongrate/)
[![Security Check](https://github.com/Happy-Kumar-Sharma/mongo-migrate/actions/workflows/bandit.yml/badge.svg)](https://github.com/Happy-Kumar-Sharma/mongo-migrate/actions/workflows/bandit.yml/badge.svg)
[![CI-CD Pipeline](https://github.com/Happy-Kumar-Sharma/mongo-migrate/actions/workflows/cicd.yml/badge.svg)](https://github.com/Happy-Kumar-Sharma/mongo-migrate)
[![CodeQL](https://github.com/Happy-Kumar-Sharma/mongo-migrate/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/Happy-Kumar-Sharma/mongo-migrate)
[![GitHub Repo stars](https://img.shields.io/github/stars/Happy-Kumar-Sharma/mongo-migrate)](https://github.com/Happy-Kumar-Sharma/mongo-migrate)

## **Overview**
Mongrate simplifies managing schema changes in MongoDB. It provides a robust migration system to track, apply, and rollback changes to your MongoDB database.

---

## **Features**
- Initialize a MongoDB migration system with a single command.
- Create migration scripts effortlessly.
- Apply migrations incrementally or all at once.
- Rollback specific migrations or all migrations.
- View migration history, including applied and pending migrations.

---

## **Installation**

Install Mongrate using pip:

```bash
pip install mongrate
```

---

## **Getting Started**

### 1. Initialize the System
Set up Mongrate in your project:

```bash
mongrate init
```

This command creates a configuration file (`mongrate_config.yaml`) and a migrations directory.

### 2. Configuration
Update the `mongrate_config.yaml` file with your database details:

```yaml
db_url: "mongodb://localhost:27017"
db_name: "my_database"
migrations_dir: "migrations"
```

### 3. Create a Migration
Generate a new migration file:

```bash
mongrate create add_users_collection
```

This creates a new script in the migrations directory.

### 4. Define Migration
Edit the generated migration script to specify your database changes:

```python
# Example: 20241228230118_add_users_collection.py

def upgrade(db):
    db.create_collection("users")
    db["users"].insert_one({"name": "admin", "role": "superuser"})

def downgrade(db):
    db.drop_collection("users")
```

### 5. Apply Migrations
Apply all pending migrations:

```bash
mongrate upgrade all
```

Apply a specific migration:

```bash
mongrate upgrade 20241228230118_add_users_collection.py
```

### 6. Rollback Migrations
Rollback all migrations:

```bash
mongrate downgrade all
```

Rollback a specific migration:

```bash
mongrate downgrade 20241228230118_add_users_collection.py
```

### 7. View Migration History
Check applied and pending migrations:

```bash
mongrate history
```

Example output:

```yaml
Applied Migrations:
  - 20241228230118_add_users_collection.py

Pending Migrations:
  - 20241228233045_add_orders_collection.py
```

---

## **Commands Overview**

| Command                        | Description                           |
|--------------------------------|---------------------------------------|
| `mongrate init`                | Initializes the migration system.     |
| `mongrate create <name>`       | Creates a new migration script.       |
| `mongrate upgrade all`         | Applies all pending migrations.       |
| `mongrate upgrade <file>`      | Applies a specific migration.         |
| `mongrate downgrade all`       | Rolls back all applied migrations.    |
| `mongrate downgrade <file>`    | Rolls back a specific migration.      |
| `mongrate history`             | Displays applied and pending migrations. |

---

## **Example Workflow**

### Initialize Mongrate:

```bash
mongrate init
```

### Create a migration:

```bash
mongrate create add_users_collection
```

### Edit the migration file:

```python
def upgrade(db):
    db.create_collection("users")
```

### Apply migrations:

```bash
mongrate upgrade all
```

### View migration history:

```bash
mongrate history
```

### Rollback a migration:

```bash
mongrate downgrade add_users_collection.py
```

---

## **Why Use Mongrate?**
- Simplifies MongoDB migration management.
- Tracks applied and pending migrations automatically.
- Provides an easy-to-use CLI.
- Designed specifically for MongoDB workflows.

---

## **License**
Mongrate is licensed under the MIT License.

---
