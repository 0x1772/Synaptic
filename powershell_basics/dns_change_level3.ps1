$adapterName = "Ethernet"       # Değiştirmek istediğiniz ağ bağdaştırıcısının adını buraya girin
$dnsServer1 = "4.2.2.1"         # İlk DNS sunucusunun IP adresini buraya girin
$dnsServer2 = "4.2.2.2"         # İkinci DNS sunucusunun IP adresini buraya girin

$adapter = Get-WmiObject -Class Win32_NetworkAdapterConfiguration | Where-Object { $_.Description -eq $adapterName }
if ($adapter -ne $null) {
    $dnsServers = @($dnsServer1, $dnsServer2)
    $adapter.SetDNSServerSearchOrder($dnsServers)
    Write-Host "DNS updated."
} else {
    Write-Host "Cant find Network Adapter!."
}
