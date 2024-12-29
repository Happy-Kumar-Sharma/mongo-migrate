# Mongrate
A MongoDB migration tool.

## Installation

```bash
pip install mongrate
```

## Usage
### Initialize the system:

```bash
mongrate init
```
Create a migration:
```bash
mongrate create <migration_name>
```

Apply migrations:

```bash
mongrate upgrade all
```
```bash
mongrate upgrade 20241228230118_migration_file.py
```

Rollback migrations:

```bash
mongrate downgrade all
```
```bash
mongrate downgrade 20241228230118_migration_file.py
```

## Migration History

You can view the migration history using the `history` command:

```bash
mongrate history
```
