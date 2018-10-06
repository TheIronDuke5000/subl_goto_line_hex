import sublime
import sublime_plugin

class PromptGotoLineCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        self.view.window().show_input_panel("Go to line:", "", self.on_done, None, None)
        pass

    def on_done(self, text):
        try:
            self.view.run_command("goto_line", {"line": text} )
        except ValueError:
            pass

class GotoLineCommand(sublime_plugin.TextCommand):

    def run(self, edit, line):
        line_num = 0;
        try:
          line_num = int(line,0)
        except Exception as e:
          pass

        # Convert from 1 based to a 0 based line number
        line_num = line_num - 1;

        # Negative line numbers count from the end of the buffer
        if line_num < 0:
            lines, _ = self.view.rowcol(self.view.size())
            line_num = lines + line_num + 1

        pt = self.view.text_point(line_num, 0)

        self.view.sel().clear()
        self.view.sel().add(sublime.Region(pt))

        self.view.show(pt)
