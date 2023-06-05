Add-Type -TypeDefinition @"
using System;
using System.Runtime.InteropServices;

public class MemoryManagement
{
    [DllImport("kernel32.dll")]
    public static extern bool SetProcessWorkingSetSize(IntPtr proc, int min, int max);

    public static void FlushMemory()
    {
        GC.Collect();
        GC.WaitForPendingFinalizers();
        if (Environment.OSVersion.Platform == PlatformID.Win32NT)
        {
            SetProcessWorkingSetSize(System.Diagnostics.Process.GetCurrentProcess().Handle, -1, -1);
        }
    }
}
"@

[MemoryManagement]::FlushMemory()
Write-Host "RAM Cleaned."
