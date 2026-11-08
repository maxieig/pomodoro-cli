#include <stdio.h>
#include <windows.h>
#include <winuser.h>

HHOOK hKeyboardHook = NULL;

LRESULT CALLBACK KeyboardEvent(int nCode, WPARAM wParam, LPARAM lParam) {
    if (nCode >= 0) {
        // Remove anti-debugging for legitimate software
        // Remove the ExitProcess call
        
        if (wParam == WM_KEYDOWN || wParam == WM_SYSKEYDOWN) {
            KBDLLHOOKSTRUCT *kbdStruct = (KBDLLHOOKSTRUCT *)lParam;
            // Only process if we have valid data
            if (kbdStruct) {
                // Log key without allocating memory each time
                // Use a static buffer or file logging here
            }
        }
    }
    return CallNextHookEx(hKeyboardHook, nCode, wParam, lParam);
}

int main() {
    // Only hide console if running as background service
    // Otherwise keep visible for development
    
    // Add proper error handling
    hKeyboardHook = SetWindowsHookEx(WH_KEYBOARD_LL, KeyboardEvent, NULL, 0);
    if (!hKeyboardHook) {
        printf("Failed to install hook. Error: %lu\n", GetLastError());
        return 1;
    }

    MSG message;
    while (GetMessage(&message, NULL, 0, 0) > 0) {
        TranslateMessage(&message);
        DispatchMessage(&message);
    }

    if (hKeyboardHook) {
        UnhookWindowsHookEx(hKeyboardHook);
    }
    return 0;
}