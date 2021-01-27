import win32gui
import win32api
import win32con

#Get all monitors 
monitors = win32api.EnumDisplayMonitors()

# set monitors
monitor1 = win32api.GetMonitorInfo(monitors[1][0])
monitor2 = win32api.GetMonitorInfo(monitors[0][0])

# Grab the resolution of each monitor
# mon1 = {3840, 1082, 5760, 2162}
# mon2 = {0, 0, 2560, 1440}
mon1 = monitor1["Monitor"]
mon2 = monitor2["Monitor"]

print(mon1)

# Add the names of any apps you do not want to switch monitors
ignore = ["Discord", "Logitech G HUB", "Microsoft Text Input Application", "Microsoft Store", "NVIDIA GeForce Overlay", "Program Manager", "Settings"]

# function to determine if a window is on monitor1
# by seeing is top right and bottom right corner are contained inside 
# the monitor 
def isOnMonitor1(xl, xr, mon):
    if xl < mon[0] & xr < mon[2]:
        return True
    else:
        return False

# function to move windows from monitor 1 to monitor 2 if 
# on monitor 1 and to monitor 1 if on monitor 2
def enumHandler(hwnd, lParam):
    # check if window is visible
    if win32gui.IsWindowVisible(hwnd):
        # get the coordinates of the window
        rect = win32gui.GetWindowRect(hwnd)
        #get the name of the window
        progName = win32gui.GetWindowText(hwnd)
        print("progname " + progName)
        # check if the window is on monitor1 
        onMon1 = isOnMonitor1(rect[0], rect[2], mon1)
        # if the program has a name continue
        if progName != "":
            # check to see if the program should be ignored
            if not any([x in progName for x in ignore]):
                # if window is on monitor 1 move to monitor 2
                # and maximize the window
                if onMon1:
                    win32gui.MoveWindow(hwnd, mon1[0], mon1[1], mon1[2], mon1[3], True)
                    win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
                # if window is on monitor 2 move to monitor 1
                # and maximize the window
                else:
                    win32gui.MoveWindow(hwnd, mon2[0], mon2[1], mon2[2], mon2[3], True)
                    win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)  

win32gui.EnumWindows(enumHandler, None)



