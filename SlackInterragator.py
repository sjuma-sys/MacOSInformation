import Cocoa
from Foundation import NSURL
from ApplicationServices import AXUIElementCreateApplication, kAXValueAttribute

def analyze_slack_ui():
    # Get all running apps
    workspace = Cocoa.NSWorkspace.sharedWorkspace()
    apps = workspace.runningApplications()
    
    slack = next((app for app in apps if app.localizedName() == "Slack"), None)
    
    if not slack:
        print("Slack is not running.")
        return

    # Create an Accessibility element for Slack
    pid = slack.processIdentifier()
    slack_ax = AXUIElementCreateApplication(pid)
    
    # Example: Get the window title
    _, title = Cocoa.AXUIElementCopyAttributeValue(slack_ax, "AXTitle", None)
    print(f"Analyzing Slack Window: {title}")

    # To read inputs/outputs, you would recursively iterate through 
    # AXChildren to find 'AXTextArea' or 'AXStaticText'
    
if __name__ == "__main__":
    analyze_slack_ui()
