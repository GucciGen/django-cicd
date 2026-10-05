from django.test import SimpleTestCase
from django.urls import reverse


class PagesTests(SimpleTestCase):
    """Тести, які GitHub Actions запускає після кожного push."""

    def test_home_page(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pages/home.html")
        self.assertContains(response, "Головна")

    def test_about_page(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pages/about.html")
        self.assertContains(response, "GitHub Actions")

    def test_contact_page(self):
        response = self.client.get(reverse("contact"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pages/contact.html")
        self.assertContains(response, "Контакти")

    def test_navigation_links_on_every_page(self):
        for name in ["home", "about", "contact"]:
            response = self.client.get(reverse(name))
            self.assertContains(response, 'href="/about/"')
            self.assertContains(response, 'href="/contact/"')

    def test_unknown_page_returns_404(self):
        response = self.client.get("/no-such-page/")
        self.assertEqual(response.status_code, 404)