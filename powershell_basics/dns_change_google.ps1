$adapterName = "Ethernet"   # Değiştirmek istediğiniz ağ bağdaştırıcısının adını buraya girin
$dnsServer1 = "8.8.8.8"     # İlk DNS sunucusunun IP adresini buraya girin
$dnsServer2 = "8.8.4.4"     # İkinci DNS sunucusunun IP adresini buraya girin

$adapter = Get-WmiObject -Class Win32_NetworkAdapterConfiguration | Where-Object { $_.Description -eq $adapterName }
if ($adapter -ne $null) {
    $dnsServers = @($dnsServer1, $dnsServer2)
    $adapter.SetDNSServerSearchOrder($dnsServers)
    Write-Host "DNS ayarları güncellendi."
} else {
    Write-Host "Ağ bağdaştırıcısı bulunamadı."
}
