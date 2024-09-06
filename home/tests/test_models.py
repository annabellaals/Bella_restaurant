from django.contrib.auth.models import Group
from django.test import TestCase

from home.models import User, FoodType


class CustomerUserModelTestCase(TestCase):
    def setUp(self):
        customer_role, _ = Group.objects.get_or_create(name='customer')
        self.user = User.objects.create_user(email='test@user.com', password='testPassword')
        self.user.groups.add(customer_role)
        self.user.save()
        self.user.first_name = 'Test'
        self.user.last_name = 'Customer'
        self.user.save()

    def test_customer_user_creation(self):
        self.assertEqual(self.user.first_name, 'Test')
        self.assertEqual(self.user.last_name, 'Customer')
        self.assertEqual(self.user.email, 'test@user.com')
        self.assertTrue(self.user.groups.filter(name="customer").exists())

    def test_customer_user_str_method(self):
        self.assertEqual(str(self.user), 'test@user.com')

    def test_customer_user_saving(self):
        user = User.objects.get(email='test@user.com')
        self.assertTrue(user.first_name, 'Test')
        self.assertTrue(user.last_name, 'Customer')

    def test_customer_user_update(self):
        self.user.first_name = 'Updated Test name'
        self.user.save()
        updated_user = User.objects.get(id=self.user.id)
        self.assertEqual(updated_user.first_name, 'Updated Test name')

    def test_customer_user_deletion(self):
        self.user.delete()
        with self.assertRaises(User.DoesNotExist):
            User.objects.get(id=self.user.id)


class ManagerUserModelTestCase(TestCase):
    def setUp(self):
        manager_role, _ = Group.objects.get_or_create(name='manager')
        self.user = User.objects.create_user(email='test@user.com', password='testPassword')
        self.user.groups.add(manager_role)
        self.user.save()
        self.user.first_name = 'Test'
        self.user.last_name = 'Manager'
        self.user.save()

    def test_manager_user_creation(self):
        self.assertEqual(self.user.first_name, 'Test')
        self.assertEqual(self.user.last_name, 'Manager')
        self.assertEqual(self.user.email, 'test@user.com')
        self.assertTrue(self.user.groups.filter(name="manager").exists())

    def test_manager_user_str_method(self):
        self.assertEqual(str(self.user), 'test@user.com')

    def test_manager_user_saving(self):
        user = User.objects.get(email='test@user.com')
        self.assertTrue(user.first_name, 'Test')
        self.assertTrue(user.last_name, 'Manager')

    def test_manager_user_update(self):
        self.user.first_name = 'Updated Test name'
        self.user.save()
        updated_user = User.objects.get(id=self.user.id)
        self.assertEqual(updated_user.first_name, 'Updated Test name')

    def test_manager_user_deletion(self):
        self.user.delete()
        with self.assertRaises(User.DoesNotExist):
            User.objects.get(id=self.user.id)


class AdminUserModelTestCase(TestCase):
    def setUp(self):
        manager_role, _ = Group.objects.get_or_create(name='admin')
        self.user = User.objects.create_superuser(email='test@user.com', password='testPassword')
        self.user.groups.add(manager_role)
        self.user.save()
        self.user.first_name = 'Test'
        self.user.last_name = 'Admin'
        self.user.save()

    def test_admin_user_creation(self):
        self.assertEqual(self.user.first_name, 'Test')
        self.assertEqual(self.user.last_name, 'Admin')
        self.assertEqual(self.user.email, 'test@user.com')
        self.assertTrue(self.user.is_superuser)
        self.assertTrue(self.user.groups.filter(name='admin').exists())

    def test_admin_user_str_method(self):
        self.assertEqual(str(self.user), 'test@user.com')

    def test_admin_user_saving(self):
        user = User.objects.get(email='test@user.com')
        self.assertTrue(user.first_name, 'Test')
        self.assertTrue(user.last_name, 'Admin')

    def test_admin_user_update(self):
        self.user.first_name = 'Updated Test name'
        self.user.save()
        updated_user = User.objects.get(id=self.user.id)
        self.assertEqual(updated_user.first_name, 'Updated Test name')

    def test_admin_user_deletion(self):
        self.user.delete()
        with self.assertRaises(User.DoesNotExist):
            User.objects.get(id=self.user.id)


class FoodTypeModelTestCase(TestCase):
    def setUp(self):
        self.food_type = FoodType.objects.create(name="Pizza")


    def test_food_type_creation(self):
        self.assertEqual(self.food_type.name, 'Pizza')

    def test_food_type_str_method(self):
        self.assertEqual(str(self.food_type), 'Pizza')

    def test_food_type_saving(self):
        food_type = FoodType.objects.get(name='Pizza')
        self.assertTrue(food_type.name, 'Pizza')

    def test_food_type_update(self):
        self.food_type.name = 'Updated Pizza'
        self.food_type.save()
        food_type = FoodType.objects.get(id=self.food_type.id)
        self.assertEqual(food_type.name, 'Updated Pizza')

    def test_food_type_deletion(self):
        self.food_type.delete()
        with self.assertRaises(FoodType.DoesNotExist):
            FoodType.objects.get(id=self.food_type.id)