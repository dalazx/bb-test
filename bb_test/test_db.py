import unittest

import db


class UserTestCase(unittest.TestCase):
    def setUp(self):
        db.Base.metadata.create_all()

    def test_base(self):
        db.Session.add(db.User(name='Test1', age=30, role='test'))
        db.Session.add(db.User(name='Test2', age=40, role='test'))
        db.Session.flush()
        users = db.Session.query(db.User).all()
        self.assertEqual(len(users), 2)
        self.assertEqual(users[0].name, 'Test1')
        self.assertEqual(users[1].name, 'Test2')

    def tearDown(self):
        db.Session.rollback()
