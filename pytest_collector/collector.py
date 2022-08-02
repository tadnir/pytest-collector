import pytest
import inspect


def reindent(string):
    if not string:
        return string

    # Calculate the leading spaces for the first line of the string.
    # ignore '\t' as it isn't common to indent with (and will mess the logic here).
    leading_spaces = len(string) - len(string.lstrip(' '))
    lines = []
    for line in string.splitlines():
        # We use lstrip to remove white spaces at the start of each line,
        # If we will let lstrip work on the whole line it might remove too much...
        # (lets say a double indent for a `for` loop in a function...)
        # So it's only allowed to strip `leading_spaces` at maximum.
        lines.append(line[:leading_spaces].lstrip() + line[leading_spaces:])

    return "\n".join(lines)


class CollectorPlugin:
    def __init__(self):
        self._modules = None

    @property
    def modules(self):
        return self._modules

    def pytest_collection_finish(self, session):
        modules = {}
        for test in session.items:
            test_module = self.get_test_module_hierarchy(test)
            if test_module["name"] not in modules:
                modules[test_module["name"]] = test_module
            else:
                self.merge_child_to_parent(modules[test_module["name"]], list(test_module["children"].values())[0])

        self._modules = [self.collect_data(module) for module in modules.values()]

    def get_test_module_hierarchy(self, test):
        level = test.parent
        hierarchy = {"name": test.name, "obj": test}
        while level.parent is not None:
            hierarchy = {"name": level.name, "obj": level, "children": {hierarchy["name"]: hierarchy}}
            level = level.parent

        return hierarchy

    def merge_child_to_parent(self, parent, child):
        if child["name"] not in parent["children"]:
            parent["children"][child["name"]] = child
        elif "children" in child:
            for grandchild in child["children"].values():
                self.merge_child_to_parent(parent["children"][child["name"]], grandchild)

    def collect_data(self, item):
        item_obj = item["obj"]
        item_data = {
            "type": type(item_obj).__name__,
            "title": item_obj.name,
            "doc": reindent(item_obj.obj.__doc__),
        }

        if type(item_obj).__name__ == "Function":
            item_data["src"] = reindent(inspect.getsource(item_obj.obj))
        else:
            item_data["children"] = [self.collect_data(child) for child in item["children"].values()]

        return item_data


def collect(tests_dir):
    collector_plugin = CollectorPlugin()
    ret = pytest.main(["--collect-only", "-qq", tests_dir], [collector_plugin])
    # ret = pytest.main(["--setup-plan", "-qq", tests_dir], [collector_plugin])
    if ret != pytest.ExitCode.OK:
        raise ValueError(ret)

    return collector_plugin.modules
