import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    def test_save_and_reload(self):
        storage = FileStorage()
        obj = BaseModel()
        storage.new(obj)
        storage.save()

        # create a new storage instance and reload objects.
        new_storage = FileStorage()
        new_storage.reload()

        self.assertEqual(len(new_storage.all()), 1)
        self.assertEqual(new_storage.all()
                         [f"{obj.__class__.__name__}.{obj.id}"])
        self.assertEqual(obj.to_dict(), new_storage.all()
                         [f"{obj.__class__.__name__}.{obj.id}"].to_dict())


if __name__ == '__main__':
    unittest.main()
