from django.test import TestCase
from .models import TimeStampMixin

class TestModels(TestCase):

    def test_models_that_inherit_timestampmixin_should_have_timestamp_defaults(self):
        class Test(TimeStampMixin):
            text = "test"

        self.assertTrue(hasattr(Test, 'created_at') and hasattr(Test, 'updated_at'))