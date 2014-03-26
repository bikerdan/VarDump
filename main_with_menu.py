import sublime_plugin, sublime


# Extends TextCommand so that run() receives a View to modify.
class VardumpCommand(sublime_plugin.TextCommand):

    selection = None
    edit = None
    line_end = None
    regions = []

    def run(self, edit):
        self.edit = edit
        reg_counter = 0

        # Walk through each region in the selection
        for region in self.view.sel():
            # Get the text of the current region (what's selected)
            selection = self.view.substr(region)
            # Get a region representing the entire line of the current region (The whole line containing the selection)
            line = self.view.line(region)
            # At the end of the line, insert some new text
            #self.view.insert(edit, line.end(), '\nexit(var_dump(' + selection + '));')

            reg_counter += 1
            self.regions.append({'selection': selection, 'line_end': line.end()})

            self.view.show_popup_menu(['exit','no exit'], self.on_done)

        sublime.status_message('VAR DUMPING!')

    def on_done(self, item):
        if item == -1:
            self.regions = []
            return
        for i in self.regions:
            if item == 0:
                self.view.insert(self.edit, i['line_end'], '\nexit(var_dump(' + i['selection'] + '));')
            else:
                self.view.insert(self.edit, i['line_end'], '\nvar_dump(' + i['selection'] + ');')
        self.regions = []