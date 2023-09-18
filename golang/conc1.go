package main

import (
	"fmt"
	"time"
)

func main(){
	go count("hola")
	go count("chao")
	time.Sleep(1*time.Second)
}

func count(nom string){
	for i:=0; true ; i++{
		fmt.Println(i,nom)
		time.Sleep(time.Millisecond*500)
	}
}
