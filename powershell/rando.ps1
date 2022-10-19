$RANDO=0

$Logfile = "C:\logs\rando.log"

for($i=0; $i -lt 5; $i++){
$RANDO=Get-Random -Maximum 1000 -Minimum 1
write-Host($RANDO)

Add-Content $LogFile "INFO: RAndom number is ${RANDO}"
}