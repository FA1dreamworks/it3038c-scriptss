Get-service | format-list displayname, status ##displays list of service
get-service |format-table DisplayName, status ##displays list of service in a table 

get-service | format-table * ##displays a list of services in a table with all parameters 
get-service | Sort-Object -Property status -Descending | Format-table displayname, status ## displays a list sorted by a property 
Get-Service | Sort-Object -Property Status -Descending | Format-Table DisplayName, Status | Out-File C:\services.txt notepad C:\services.txt
    Remove-Item C:\services.txt ##sending output to a file 

##GRidview
get-service | Out-gridview
Get-Service | select-object displayname, status | Out-GridView
get-service | Select-Object * | Out-GridView

##Variables
$Hello = "Hello, Powershell"
Write-Host($Hello)

Set-ExecutionPolicy -ExecutionPolicy Unrestricted
##confrim the popup with "yes"

function getip{
    (Get-NetIPAddress).IPv4Address | Select-String "192"
    }
write-host(getip)
$IP = getip 
Write-Host("This machine's IP is $IP")
