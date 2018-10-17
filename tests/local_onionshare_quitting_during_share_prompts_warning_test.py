#!/usr/bin/env python3
import unittest
from PyQt5 import QtCore, QtTest

from .GuiShareTest import GuiShareTest

class LocalQuittingDuringSharePromptsWarningTest(unittest.TestCase, GuiShareTest):
    @classmethod
    def setUpClass(cls):
        test_settings = {
            "close_after_first_download": False
        }
        cls.gui = GuiShareTest.set_up(test_settings, 'LocalQuittingDuringSharePromptsWarningTest')

    @classmethod
    def tearDownClass(cls):
        GuiShareTest.tear_down()

    def test_gui(self):
        self.run_all_common_setup_tests()
        self.run_all_share_mode_tests(False, True)
        # Prepare our auto-accept of prompt
        QtCore.QTimer.singleShot(5000, self.accept_dialog)
        # Try to close the app
        self.gui.close()
        # Server should still be running (we've been prompted first)
        self.server_is_started(self.gui.share_mode, 0)
        self.web_server_is_running()

if __name__ == "__main__":
    unittest.main()
