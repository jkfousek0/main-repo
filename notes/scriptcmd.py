
vscode_commands = {
     "Navigation": {
         "Command Palette": "Ctrl+Shift+P or F1",
         "Explorer Sidebar": "Ctrl+Shift+E",
         "Go to File": "Ctrl+P",
         "Go to Symbol": "Ctrl+Shift+O",
         "Go to Definition": "F12",
         "Peek Definition": "Alt+F12",
         "Switch Editor Tabs": "Ctrl+Tab"
     },
     "Editing": {
         "Copy Line Up/Down": "Alt+Shift+Up/Down Arrow",
         "Move Line Up/Down": "Alt+Up/Down Arrow",
         "Indent/Outdent Line": "Ctrl+] or Ctrl+[",
         "Toggle Comment": "Ctrl+/",
         "Format Document": "Shift+Alt+F",
         "Find/Replace": "Ctrl+F for find, Ctrl+H for replace"
     },
     "Integrated inal": {
         "Toggle inal": "Ctrl+`",
         "New inal": "Ctrl+Shift+`",
         "Switch inal Tabs": "Ctrl+Page Up/Page Down"
     },
     "Debugging": {
         "Start Debugging": "F5",
         "Stop Debugging": "Shift+F5",
         "Step Over": "F10",
         "Step Into": "F11",
         "Toggle Breakpoint": "F9"
     },
     "Version Control": {
         "Open Source Control": "Ctrl+Shift+G",
         "Stage Changes": "Ctrl+Shift+G, then A",
         "Commit Changes": "Ctrl+Enter"
     }
}

# Print the VS Code commands in an organized manner
for category, commands in vscode_commands.items():
    print(f"{category}:")
    for command, shortcut in commands.items():
        print(f"  {command}: {shortcut}")
    print()  # Empty line between categories
