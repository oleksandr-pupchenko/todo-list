from django.test import TestCase

from todolist.models import Task, Tag


class TagModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Tag.objects.create(name="shop")

    def test_name_label(self):
        tag = Tag.objects.get(id=1)
        field_label = tag._meta.get_field("name").verbose_name
        self.assertEqual(field_label, "name")

    def test_name_max_length(self):
        tag = Tag.objects.get(id=1)
        max_length = tag._meta.get_field("name").max_length
        self.assertEqual(max_length, 255)

    def test_tag_str(self):
        tag = Tag.objects.get(id=1)
        expected_object_name = tag.name
        self.assertEqual(str(tag), expected_object_name)


class TaskModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Task.objects.create(
            content="clean windows",
            is_done=False,
        )

    def test_task_str(self):
        task = Task.objects.get(id=1)
        expected_object_name = f"Task {task.id}"
        self.assertEqual(str(task), expected_object_name)
        