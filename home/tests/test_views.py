from django.contrib.auth.models import Group
from django.test import TestCase
from django.urls import reverse

from home.models import User


class HomepageTestCase(TestCase):
    def setUp(self):
        # You can use this method to set up any necessary preconditions for your tests
        pass

    def test_homepage_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_homepage_template_used(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'home/index.html')

    def test_homepage_content(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertContains(response, "Bella's Restaurant" )


class AboutPageTestCase(TestCase):
    def setUp(self):
        # You can use this method to set up any necessary preconditions for your tests
        pass
    def test_about_page_status_code(self):
        url = reverse('about')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_about_page_template_used(self):
        url = reverse('about')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'home/about.html')

    def test_about_page_content(self):
        url = reverse('about')
        response = self.client.get(url)
        self.assertContains(response, "You Are at Bella's Restaurant" )


class LoginPageTestCase(TestCase):
    def setUp(self):
        pass
    def test_login_page_status_code(self):
        url = reverse('login')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_login_page_template_used(self):
        url = reverse('login')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'home/login.html')

    def test_login_page_content(self):
        url = reverse('login')
        response = self.client.get(url)
        self.assertContains(response, "Welcome back to Bella's Restaurant" )


class RegisterPageTestCase(TestCase):
    def setUp(self):
        pass

    def test_register_page_status_code(self):
        url = reverse('register')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_register_page_template_used(self):
        url = reverse('register')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'home/register.html')

    def test_register_page_content(self):
        url = reverse('register')
        response = self.client.get(url)
        self.assertContains(response, "Welcome to Bella's Restaurant" )


class MenuPageTestCase(TestCase):
    def setUp(self):
        pass

    def test_menu_page_status_code(self):
        url = reverse('menu')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_menu_page_template_used(self):
        url = reverse('menu')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'home/menu.html')

    def test_menu_page_content(self):
        url = reverse('menu')
        response = self.client.get(url)
        self.assertContains(response, "Our Menu" )


class ReservationPageTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='test@user.com', password='testPassword')
        self.client.login(username='test@user.com', password='testPassword')

    def test_book_page_status_code(self):
        url = reverse('book')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_book_page_template_used(self):
        url = reverse('book')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'home/book.html')

    def test_book_page_content(self):
        url = reverse('book')
        response = self.client.get(url)
        self.assertContains(response, "Book A Table" )


class CartPageTestCase(TestCase):
    def setUp(self):
        pass

    def test_cart_page_status_code(self):
        url = reverse('cart')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_cart_page_template_used(self):
        url = reverse('cart')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'home/cart.html')

    def test_cart_page_content(self):
        url = reverse('cart')
        response = self.client.get(url)
        self.assertContains(response, "Order details" )


class CustomerAccountPageTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='test@user.com', password='testPassword')
        self.client.login(username='test@user.com', password='testPassword')

    def test_customer_account_page_status_code(self):
        url = reverse('account')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_customer_account_page_template_used(self):
        url = reverse('account')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'home/account.html')

    def test_customer_account_page_content(self):
        url = reverse('account')
        response = self.client.get(url)
        self.assertContains(response, "Your Orders" )
        self.assertContains(response, "Your Table Bookings")


class ManagerAccountPageTestCase(TestCase):
    def setUp(self):
        manager_role, _= Group.objects.get_or_create(name='manager')
        self.user = User.objects.create_user(email='test@user.com', password='testPassword')
        self.user.groups.add(manager_role)
        self.user.save()
        self.client.login(username='test@user.com', password='testPassword')

    def test_manager_account_page_status_code(self):
        url = reverse('manager-account')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_manager_account_page_template_used(self):
        url = reverse('manager-account')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'home/manager/account.html')

    def test_manager_account_page_content(self):
        url = reverse('manager-account')
        response = self.client.get(url)
        self.assertContains(response, "Orders:" )
        self.assertContains(response, "Table Bookings:")