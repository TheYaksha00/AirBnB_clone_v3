#!/usr/bin/python3
<<<<<<< HEAD
"""
Unit Test for BaseModel Class
"""
import unittest
from datetime import datetime
import models
from models import engine
from models.engine.file_storage import FileStorage
import json
import os

User = models.user.User
State = models.state.State
City = models.city.City
BaseModel = models.base_model.BaseModel
FileStorage = engine.file_storage.FileStorage
storage = models.storage
F = './dev/file.json'
storage_type = os.environ.get('HBNB_TYPE_STORAGE')


@unittest.skipIf(storage_type == 'db', 'skip if environ is db')
class TestFileStorageDocs(unittest.TestCase):
    """Class for testing BaseModel docs"""

    @classmethod
    def setUpClass(cls):
        print('\n\n.................................')
        print('..... Testing Documentation .....')
        print('..... For FileStorage Class .....')
        print('.................................\n\n')

    def test_doc_file(self):
        """... documentation for the file"""
        expected = ("\nHandles I/O, writing and reading, of JSON for storage "
                    "of all class instances\n")
        actual = models.file_storage.__doc__
        self.assertEqual(expected, actual)

    def test_doc_class(self):
        """... documentation for the class"""
        expected = 'handles long term storage of all class instances'
        actual = FileStorage.__doc__
        self.assertEqual(expected, actual)

    def test_doc_all(self):
        """... documentation for all function"""
        expected = 'returns private attribute: __objects'
        actual = FileStorage.all.__doc__
        self.assertEqual(expected, actual)

    def test_doc_new(self):
        """... documentation for new function"""
        expected = ("sets / updates in __objects the obj with key <obj class "
                    "name>.id")
        actual = FileStorage.new.__doc__
        self.assertEqual(expected, actual)

    def test_doc_save(self):
        """... documentation for save function"""
        expected = 'serializes __objects to the JSON file (path: __file_path)'
        actual = FileStorage.save.__doc__
        self.assertEqual(expected, actual)

    def test_doc_reload(self):
        """... documentation for reload function"""
        expected = ("if file exists, deserializes JSON file to __objects, "
                    "else nothing")
        actual = FileStorage.reload.__doc__
        self.assertEqual(expected, actual)

    def test_doc_get(self):
        """... documentation for get function"""
        expected = ' retrieves one object '
        actual = FileStorage.get.__doc__
        self.assertEqual(expected, actual)

    def test_doc_count(self):
        """... documentation for count function"""
        expected = ' counts number of objects of a class in storage '
        actual = FileStorage.count.__doc__
        self.assertEqual(expected, actual)


@unittest.skipIf(storage_type == 'db', 'skip if environ is db')
class TestBmFsInstances(unittest.TestCase):
    """testing for class instances"""

    @classmethod
    def setUpClass(cls):
        print('\n\n.................................')
        print('...... Testing FileStorate ......')
        print('..... For FileStorage Class .....')
        print('.................................\n\n')

    def setUp(self):
        """initializes new storage object for testing"""
        self.storage = FileStorage()
        self.bm_obj = BaseModel()

    def test_instantiation(self):
        """... checks proper FileStorage instantiation"""
        self.assertIsInstance(self.storage, FileStorage)

    def test_storage_file_exists(self):
        """... checks proper FileStorage instantiation"""
        if os.path.isfile(F):
            os.remove(F)
        self.bm_obj.save()
        self.assertTrue(os.path.isfile(F))

    def test_obj_saved_to_file(self):
        """... checks proper FileStorage instantiation"""
        if os.path.isfile(F):
            os.remove(F)
        self.bm_obj.save()
        bm_id = self.bm_obj.id
        actual = 0
        with open(F, mode='r', encoding='utf-8') as f_obj:
            storage_dict = json.load(f_obj)
        for k in storage_dict.keys():
            if bm_id in k:
                actual = 1
        self.assertTrue(1 == actual)

    def test_to_json(self):
        """... to_json should return serializable dict object"""
        my_model_json = self.bm_obj.to_json()
        actual = 1
        try:
            serialized = json.dumps(my_model_json)
        except:
            actual = 0
        self.assertTrue(1 == actual)

    def test_reload(self):
        """... checks proper usage of reload function"""
        if os.path.isfile(F):
            os.remove(F)
        self.bm_obj.save()
        bm_id = self.bm_obj.id
        actual = 0
        new_storage = FileStorage()
        new_storage.reload()
        all_obj = new_storage.all()
        for k in all_obj.keys():
            if bm_id in k:
                actual = 1
        self.assertTrue(1 == actual)

    def test_save_reload_class(self):
        """... checks proper usage of class attribute in file storage"""
        if os.path.isfile(F):
            os.remove(F)
        self.bm_obj.save()
        bm_id = self.bm_obj.id
        actual = 0
        new_storage = FileStorage()
        new_storage.reload()
        all_obj = new_storage.all()
        for k, v in all_obj.items():
            if bm_id in k:
                if type(v).__name__ == 'BaseModel':
                    actual = 1
        self.assertTrue(1 == actual)


class TestUserFsInstances(unittest.TestCase):
    """testing for class instances"""

    @classmethod
    def setUpClass(cls):
        print('\n\n.................................')
        print('...... Testing FileStorage ......')
        print('.......... User  Class ..........')
        print('.................................\n\n')

    def setUp(self):
        """initializes new user for testing"""
        self.user = User()
        self.bm_obj = BaseModel()

    @unittest.skipIf(storage_type == 'db', 'skip if environ is db')
    def test_storage_file_exists(self):
        """... checks proper FileStorage instantiation"""
        if os.path.isfile(F):
            os.remove(F)
        self.user.save()
        self.assertTrue(os.path.isfile(F))

    @unittest.skipIf(storage_type == 'db', 'skip if environ is db')
    def test_obj_saved_to_file(self):
        """... checks proper FileStorage instantiation"""
        if os.path.isfile(F):
            os.remove(F)
        self.user.save()
        u_id = self.user.id
        actual = 0
        with open(F, mode='r', encoding='utf-8') as f_obj:
            storage_dict = json.load(f_obj)
        for k in storage_dict.keys():
            if u_id in k:
                actual = 1
        self.assertTrue(1 == actual)

    @unittest.skipIf(storage_type == 'db', 'skip if environ is db')
    def test_reload(self):
        """... checks proper usage of reload function"""
        if os.path.isfile(F):
            os.remove(F)
        self.bm_obj.save()
        u_id = self.bm_obj.id
        actual = 0
        new_storage = FileStorage()
        new_storage.reload()
        all_obj = new_storage.all()
        for k in all_obj.keys():
            if u_id in k:
                actual = 1
        self.assertTrue(1 == actual)


@unittest.skipIf(storage_type == 'db', 'skip if environ is not db')
class TestGetCountFS(unittest.TestCase):
    """testing get and count methods"""

    @classmethod
    def setUpClass(cls):
        print('\n\n.................................')
        print('...... Testing Get and Count ......')
        print('.......... FS Methods ..........')
        print('.................................\n\n')

    def setUp(self):
        """initializes new state and cities for testing"""
        if os.path.isfile(F):
            os.remove(F)
        storage.reload()
        self.state = State()
        self.state.name = 'California'
        self.state.save()
        self.city1 = City()
        self.city1.name = 'Fremont'
        self.city1.state_id = self.state.id
        self.city1.save()
        self.city2 = City()
        self.city2.name = 'San_Francisco'
        self.city2.state_id = self.state.id
        self.city2.save()

    def test_get(self):
        """check if get method returns state"""
        real_state = storage.get("State", self.state.id)
        fake_state = storage.get("State", "12345")
        no_state = storage.get("", "")

        self.assertEqual(real_state, self.state)
        self.assertNotEqual(fake_state, self.state)
        self.assertIsNone(no_state)

    def test_count(self):
        """checks if count method returns correct numbers"""
        state_count = storage.count("State")
        city_count = storage.count("City")
        place_count = storage.count("Place")
        all_count = storage.count(None)

        self.assertEqual(state_count, 1)
        self.assertEqual(city_count, 2)
        self.assertEqual(place_count, 0)
        self.assertEqual(all_count, 18)

if __name__ == '__main__':
    unittest.main
=======
'''
    Testing the file_storage module.
    '''

    import os
    import time
    import json
    import unittest
    import models
    from models import storage
    from models.base_model import BaseModel
    from models.state import State
    from models.engine.file_storage import FileStorage

    db = os.getenv("HBNB_TYPE_STORAGE")


    @unittest.skipIf(db == 'db', "Testing DBstorage only")
    class testFileStorage(unittest.TestCase):
            '''
                    Testing the FileStorage class
                        '''

                            def setUp(self):
                                        '''
                                                    Initializing classes
                                                            '''
                                                                    self.storage = FileStorage()
                                                                            self.my_model = BaseModel()

                                                                                def tearDown(self):
                                                                                            '''
                                                                                                        Cleaning up.
                                                                                                                '''

                                                                                                                        try:
                                                                                                                                        os.remove("file.json")
                                                                                                                                                except FileNotFoundError:
                                                                                                                                                                pass

                                                                                                                                                                def test_all_return_type(self):
                                                                                                                                                                            '''
                                                                                                                                                                                        Tests the data type of the return value of the all method.
                                                                                                                                                                                                '''
                                                                                                                                                                                                        storage_all = self.storage.all()
                                                                                                                                                                                                                self.assertIsInstance(storage_all, dict)

                                                                                                                                                                                                                    def test_new_method(self):
                                                                                                                                                                                                                                '''
                                                                                                                                                                                                                                            Tests that the new method sets the right key and value pair
                                                                                                                                                                                                                                                        in the FileStorage.__object attribute
                                                                                                                                                                                                                                                                '''
                                                                                                                                                                                                                                                                        self.storage.new(self.my_model)
                                                                                                                                                                                                                                                                                key = str(self.my_model.__class__.__name__ + "." + self.my_model.id)
                                                                                                                                                                                                                                                                                        self.assertTrue(key in self.storage._FileStorage__objects)

                                                                                                                                                                                                                                                                                            def test_objects_value_type(self):
                                                                                                                                                                                                                                                                                                        '''
                                                                                                                                                                                                                                                                                                                    Tests that the type of value contained in the FileStorage.__object
                                                                                                                                                                                                                                                                                                                                is of type obj.__class__.__name__
                                                                                                                                                                                                                                                                                                                                        '''
                                                                                                                                                                                                                                                                                                                                                self.storage.new(self.my_model)
                                                                                                                                                                                                                                                                                                                                                        key = str(self.my_model.__class__.__name__ + "." + self.my_model.id)
                                                                                                                                                                                                                                                                                                                                                                val = self.storage._FileStorage__objects[key]
                                                                                                                                                                                                                                                                                                                                                                        self.assertIsInstance(self.my_model, type(val))

                                                                                                                                                                                                                                                                                                                                                                            def test_save_file_exists(self):
                                                                                                                                                                                                                                                                                                                                                                                        '''
                                                                                                                                                                                                                                                                                                                                                                                                    Tests that a file gets created with the name file.json
                                                                                                                                                                                                                                                                                                                                                                                                            '''
                                                                                                                                                                                                                                                                                                                                                                                                                    self.storage.save()
                                                                                                                                                                                                                                                                                                                                                                                                                            self.assertTrue(os.path.isfile("file.json"))

                                                                                                                                                                                                                                                                                                                                                                                                                                def test_save_file_read(self):
                                                                                                                                                                                                                                                                                                                                                                                                                                            '''
                                                                                                                                                                                                                                                                                                                                                                                                                                                        Testing the contents of the files inside the file.json
                                                                                                                                                                                                                                                                                                                                                                                                                                                                '''
                                                                                                                                                                                                                                                                                                                                                                                                                                                                        self.storage.save()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                self.storage.new(self.my_model)

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        with open("file.json", encoding="UTF8") as fd:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        content = json.load(fd)

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                self.assertTrue(type(content) is dict)

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    def test_the_type_file_content(self):
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                '''
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            testing the type of the contents inside the file.
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    '''
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            self.storage.save()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    self.storage.new(self.my_model)

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            with open("file.json", encoding="UTF8") as fd:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            content = fd.read()

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    self.assertIsInstance(content, str)

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        def test_reaload_without_file(self):
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    '''
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                Tests that nothing happens when file.json does not exists
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            and reload is called
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    '''

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            try:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            self.storage.reload()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        self.assertTrue(True)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                except:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                self.assertTrue(False)

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    def test_delete(self):
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                '''
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            Test delete method
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    '''
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            fs = FileStorage()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    new_state = State()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            fs.new(new_state)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    state_id = new_state.id
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            fs.save()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    fs.delete(new_state)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            with open("file.json", encoding="UTF-8") as fd:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            state_dict = json.load(fd)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    for k, v in state_dict.items():
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    self.assertFalse(state_id == k.split('.')[1])

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        def test_model_storage(self):
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    '''
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                Test State model in Filestorage
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        '''
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                self.assertTrue(isinstance(storage, FileStorage))

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    def test_filestorage_get(self):
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                '''
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            Testing Get method
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    '''
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            filestor = FileStorage()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    new = State()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            new.name = "Alabama"
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    filestor.new(new)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            new_id = new.id
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    filestor.save()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            state = filestor.get("State", new_id)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    self.assertEqual(state.name, "Alabama")

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        def test_filestorage_count(self):
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    '''
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                Testing Count method
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        '''
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                filestor = FileStorage()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        old_count = filestor.count("State")
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                new = State(name="Alabama")
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        filestor.new(new)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                filestor.save()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        new_count = filestor.count("State")
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                self.assertEqual(old_count + 1, new_count)
>>>>>>> 6e7511263a25b22fb7180a2a53d1daa63c24a997
