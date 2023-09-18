package main

import "fmt"

func main(){
	var a bool
	var b float32
	var c byte
	a=true
	b=2.4352
	c=123
	fmt.Println(a,b,c)
	fmt.Println("Arreglos:")
	var arr = [4]string {"Paul","Maria","Donald","Azucena"}
	for i:=0; i < len(arr); i++{
		fmt.Println(arr[i])
	}
	fmt.Println("SEgunda impresión:")
	for idx, el := range(arr){
		fmt.Println(idx, el)
	}

	//Slices
	frameworks := []string{"React","Vue","Angular","Django","Flask"}
	someframeworks := frameworks[0:2]
	fmt.Println(someframeworks)
}
