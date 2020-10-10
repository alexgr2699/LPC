function dolares{
   $b = $a/21.13
   "dolares:"
   $b
}
function euros{
   $b = $a/24.99
   "euros:"
   $b
}

function Menu{
     param ([string]$Menu = 'Menu' )
     Write-Host "############## $Menu ##############"
    
     Write-Host "1: Presione '1' para conversion a dolares."
     Write-Host "2: Presione '2' para conversion a euros."
     Write-Host "Q: Presione 'Q' para salir."
     }
do{
    "Ingrese un el numero de pesos que quiera convertir"
    $a = read-Host "Ingresa tu dinero en Pesos"
    Menu
    $input = Read-Host "Seleccione una opcion"
    switch($input){
        '1'{
            cls
            dolares
        }
        '2'{
            cls
            euros    
        }
        'q'{
            return
        }
    }
    
}Until ($strQuit -eq "q")
clear