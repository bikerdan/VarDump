import sublime_plugin

# Extends TextCommand so that run() receives a View to modify.
class VarDumpCommand(sublime_plugin.TextCommand):

    def run(self, edit):

        # Walk through each region in the selection
        for region in self.view.sel():
            # Get the text of the current region (what's selected)
            selection = self.view.substr(region)
            # Get a region representing the entire line of the current region (The whole line containing the selection)
            line = self.view.line(region)
            # At the end of the line, insert some new text
            self.view.insert(edit, line.end(), '\nexit(var_dump(' + selection + '));')