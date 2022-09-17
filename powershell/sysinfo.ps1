
function getip{
    (Get-NetIPAddress).IPv4Address | Select-String "192"
    }
write-host(getip)
$IP = getip 

$User = "Administrator"
write-host($user)

$host = hostname
write-host($host)

$version= $host.version
write-host($version)

$date= date
wrtie-host($date)

Write-Host("This machine's IP is $IP. User is $User. Hostname is $host. Powershell version $version.Today's date is $date")




