from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase
from .models import BaseManagerModel, RenameManagerModel, ReplaceManagerModel, MultipleManagerModel


class TestModelIdent(TestCase):
    def setUp(self):
        self.base_model = BaseManagerModel.create()
        self.rename_model = RenameManagerModel.create()
        self.replace_model = ReplaceManagerModel.create()
        self.multiple_model = MultipleManagerModel.create()

    def test_created(self):
        self.assertEqual(BaseManagerModel.objects.get(pk=1), self.base_model)
        self.assertEqual(RenameManagerModel.instances.get(pk=1), self.rename_model)
        self.assertEqual(MultipleManagerModel.objects.get(pk=1), self.multiple_model)
        with self.assertRaises(ObjectDoesNotExist):
            ReplaceManagerModel.objects.get(pk=1)
        with self.assertRaises(ObjectDoesNotExist):
            MultipleManagerModel.instances.get(pk=1)

    def test_ident(self):
        self.assertEquals(BaseManagerModel.ident_(1).pk, 1)

    def test_non_existant_pk(self):
        with self.assertRaises(ObjectDoesNotExist):
            BaseManagerModel.ident_(2)
