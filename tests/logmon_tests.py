import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../src"))

from testslide.dsl import context
import tempfile
import logmon.logmon
from pathlib import Path

@context
def logmon_tests(context):

    @context.sub_context
    def find_log_files(context):

        @context.example
        def it_will_return_zero_log_files_for_empty_dir(self):
            with tempfile.TemporaryDirectory() as dir:
                result = logmon.logmon.find_log_files(dir)
                self.assertEqual(result,[])

        @context.example
        def it_will_return_one_log_file_name(self):
            with tempfile.TemporaryDirectory() as dir:
                path = Path(os.path.join(dir, "test.log"))
                path.touch()
                result = logmon.logmon.find_log_files(dir)
                self.assertEqual(result,[str(path)])

        @context.example
        def it_will_return_multiple_file_names(self):
            with tempfile.TemporaryDirectory() as dir:
                paths = [
                    Path(os.path.join(dir, "test.log")),
                    Path(os.path.join(dir, "test2.log"))
                ]
                expected_result = []
                for path in paths:
                    path.touch()
                    expected_result.append(str(path))
                result = logmon.logmon.find_log_files(dir)
                self.assertEqual(result,expected_result)

        @context.example
        def it_will_ignore_other_files(self):
            with tempfile.TemporaryDirectory() as dir:
                paths = [
                    Path(os.path.join(dir, "test.notalog")),
                    Path(os.path.join(dir, "test2.notalog"))
                ]
                expected_result = []
                for path in paths:
                    path.touch()
                result = logmon.logmon.find_log_files(dir)
                self.assertEqual(result,expected_result)

        @context.example
        def it_will_find_files_in_subdirs(self):
            with tempfile.TemporaryDirectory() as dir:
                subdir = os.path.join(dir, "subdir")
                os.mkdir(subdir)
                paths = [
                    Path(os.path.join(subdir, "test.log")),
                    Path(os.path.join(subdir, "test2.log"))
                ]
                expected_result = []
                for path in paths:
                    path.touch()
                    expected_result.append(str(path))
                result = logmon.logmon.find_log_files(dir)
                self.assertEqual(result,expected_result)
