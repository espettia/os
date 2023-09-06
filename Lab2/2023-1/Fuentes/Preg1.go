package main

import (
	"fmt"
	"os"
	"sync"
)

var wg sync.WaitGroup

func admin() {
	// Aqui va el código del administrador
}

func worker1() {
	for {
		fmt.Printf("A")
	}
	wg.Done()
}

func worker2() {
	for {
		fmt.Printf("B")
	}
	wg.Done()
}

func worker3() {
	for {
		fmt.Printf("C")
	}
	wg.Done()
}

func worker4() {
	for {
		fmt.Printf("D")
	}
	wg.Done()
}

func worker5() {
	for {
		fmt.Printf("E")
	}
	wg.Done()
}

func main() {
	var cadena string
	for i := 1; i < len(os.Args); i++ {
		cadena = os.Args[i]
		switch cadena {
		case "A":
			fmt.Println(cadena)
		case "B":
			fmt.Println(cadena)
		case "C":
			fmt.Println(cadena)
		case "D":
			fmt.Println(cadena)
		case "E":
			fmt.Println(cadena)
		}
	}
	wg.Add(5)
	go admin()
	go worker1()
	go worker2()
	go worker3()
	go worker4()
	go worker5()
	wg.Wait()
}
