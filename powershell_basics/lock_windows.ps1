$signature = @"
[DllImport("user32.dll", SetLastError = true)]
public static extern bool LockWorkStation();
"@

$code = Add-Type -MemberDefinition $signature -Name NativeMethods -Namespace Win32Functions -PassThru

[Win32Functions.NativeMethods]::LockWorkStation()
