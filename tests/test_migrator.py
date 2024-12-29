import unittest
import os
from mongodb_migrator.core import MongoDBMigrator, create_default_config
from tests.conftest import TEST_DEFAULT_CONFIG_FILE

class TestMongoDBMigrator(unittest.TestCase):
    def setUp(self):
        create_default_config(config_file=TEST_DEFAULT_CONFIG_FILE)
        self.migrator = MongoDBMigrator(config_file=TEST_DEFAULT_CONFIG_FILE)

    def test_initialization(self):
        self.migrator.init()
        self.assertTrue(os.path.exists("tests_migrations"))

    def test_create_migration(self):
        self.migrator.init()
        self.migrator.create_migration("test_migration")
        migrations = os.listdir("tests_migrations")
        self.assertTrue(any("test_migration" in migration for migration in migrations))

    def test_migration_history(self):
        self.migrator.init()
        self.migrator.create_migration("test_migration1")
        self.migrator.create_migration("test_migration2")

        # Simulate applying one migration
        self.migrator.apply_migrations(target="test_migration1")

        history = self.migrator.get_migration_history()

        self.assertTrue(any("test_migration1.py" in history for history in history["applied"]))
        # self.assertTrue(any("test_migration2.py" in history for history in history["pending"]))

    def test_zzzz_delete_migration(self):
        import shutil
        self.migrator.rollback_migrations()
        history = self.migrator.get_migration_history()
        self.assertFalse(any("test_migration1.py" in history for history in history["applied"]))
        migrations = os.listdir("tests_migrations")
        self.assertTrue(any("test_migration" in migration for migration in migrations))
        shutil.rmtree("tests_migrations")

if __name__ == "__main__":
    unittest.main()
