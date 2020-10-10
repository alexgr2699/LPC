#!/bin/bash
function dolares(){
	dol= $(($x/20))
	echo "dolares: $" $dol
}
function euros(){
	eur= $(($x/24))
	echo  "euros: $" $eur
}

function menu(){
	read -p "ingresa una cantidad en pesos: $" x
}

while :
do
	menu
	echo "	############## Conversion a ##############  "
	echo "1) dolares"
	echo "2) euros"	
	echo "3) Salir"
	read var
	
	case $var in
		1)
			clear
			dolares
		;;

		2)
			clear
			euros
		;;

		3)
			clear
			echo "Gracias"
      			echo "Saliendo..."
			sleep 3
			break
		;;
	esac
done
