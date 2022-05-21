"""
Checkstyle plugin for pylint
"""
from itertools import groupby
from typing import TYPE_CHECKING, Optional
from xml.dom import minidom

from pylint.interfaces import IReporter
from pylint.reporters.base_reporter import BaseReporter

if TYPE_CHECKING:
    from pylint.lint.pylinter import PyLinter
    from pylint.reporters.ureports.nodes import Section


class CheckstyleReporter(BaseReporter):
    """
    Outputs pylint errors in checkstyle format
    """
    __implements__ = IReporter
    name = "checkstyle"
    extension = "xml"

    def _display(self, layout) -> None:
        pass

    def display_messages(self, layout: Optional["Section"]) -> None:
        root = minidom.Document()
        checkstyle = root.createElement('checkstyle')
        root.appendChild(checkstyle)
        messages_by_file = {abspath: list(messages)
                            for abspath, messages in
                            (groupby(
                                sorted(self.messages, key=lambda x: x.abspath),
                                lambda x: x.abspath)
                            )}
        for abspath in messages_by_file:
            file = root.createElement("file")
            file.setAttribute("name", abspath)
            for msg in messages_by_file[abspath]:
                error = root.createElement("error")
                error.setAttribute("line", str(msg.line))
                error.setAttribute("column", str(msg.column))
                error.setAttribute("message", msg.msg)
                error.setAttribute("source", f"{msg.msg_id}:{msg.symbol}")
                error.setAttribute("severity", msg.category)
                file.appendChild(error)
                checkstyle.appendChild(file)
        print(root.toprettyxml(indent="  "))


def register(linter: "PyLinter") -> None:
    """
    Register our reporter as a plugin for pylint
    """
    linter.register_reporter(CheckstyleReporter)
