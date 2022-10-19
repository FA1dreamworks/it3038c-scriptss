$RANDO=0

$Logfile = "C:\logs\rando.log"

for($i=0; $i -lt 5; $i++){
$RANDO=Get-Random -Maximum 1000 -Minimum 1
write-Host($RANDO)

Add-Content $LogFile "INFO: RAndom number is ${RANDO}"
}

$Mchines = 'localhost'

Foreach ($machine in $Machines)
{
    $RCounters = Get-Counter -ListSet * -ComputerName $machine
    "There are {0} counters on {1}" -f $RCounters.count, ($machine)
    }

$Mchines = 'localhost'

Foreach ($machine in $Machines)
{
   $pt = (Get-Counter -Counter "\Processor(_Total)\$ Processor Time").CounterSamples.CookedValue
   $pt
    }