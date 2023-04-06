import os
import unittest

from tests.helpers import TestContext, TestTaskRunner, temporary_root
from lekt import config as lekt_config


class TestContextTests(unittest.TestCase):
    def test_create_testcontext(self) -> None:
        with temporary_root() as root:
            context = TestContext(root)
            config = lekt_config.load_full(root)
            runner = context.job_runner(config)
            self.assertTrue(os.path.exists(context.root))
            self.assertFalse(
                os.path.exists(os.path.join(context.root, lekt_config.CONFIG_FILENAME))
            )
            self.assertTrue(isinstance(runner, TestTaskRunner))
