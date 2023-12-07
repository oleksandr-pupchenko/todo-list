from django.test import TestCase, Client
from django.urls import reverse
from django.shortcuts import get_object_or_404
from todolist.models import Task, Tag


class TaskTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.task = Task.objects.create(
            content="Task 1",
            is_done="False",
        )

    def test_toggle_task_status(self):
        url = reverse("todolist:toggle_task_status", kwargs={"pk": self.task.id})
        response = self.client.post(url)

        self.assertRedirects(response, reverse("todolist:index"))
        task = get_object_or_404(Task, id=self.task.id)
        self.assertEqual(task.is_done, True)

    def test_create_task(self):
        url = reverse("todolist:task-create")
        data = {"content": "clean room", "is_done": "False", }
        response = self.client.post(url, data)

        self.assertRedirects(response, reverse("todolist:index"))
        self.assertEqual(Task.objects.count(), 2)

    def test_update_task(self):
        response = self.client.post(
            reverse("todolist:task-update", kwargs={"pk": self.task.id}),
            {
                "content": "new test",
                "is_done": self.task.is_done,
            },
        )
        Task.objects.get(id=self.task.id).refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.get(id=self.task.id).content, "new test")

    def test_delete_task(self):
        url = reverse("todolist:task-delete", kwargs={"pk": self.task.id})
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Task.objects.filter(id=self.task.id).exists())


class TagTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.tag = Tag.objects.create(name="work")

    def test_create_tag(self):
        url = reverse("todolist:tag-create")
        data = {"name": "home"}
        response = self.client.post(url, data)

        self.assertRedirects(response, reverse("todolist:tag-list"))
        self.assertEqual(Tag.objects.count(), 2)

    def test_update_tag(self):
        response = self.client.post(
            reverse("todolist:tag-update", kwargs={"pk": self.tag.id}),
            {
                "name": "shop",
            },
        )
        Tag.objects.get(id=self.tag.id).refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Tag.objects.get(id=self.tag.id).name, "shop")

    def test_delete_tag(self):
        url = reverse("todolist:tag-delete", kwargs={"pk": self.tag.id})
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Tag.objects.filter(id=self.tag.id).exists())
