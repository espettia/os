
package main

import (
	"fmt"
	"time"
	"sync"
)

//No parece que fuera realmente random (A ó B)
//Go se encarga de intercalar automáticamente los hilos concurrentes?
//Intercalar en el sentido de que el planificador no 
//permita por ejemplo que un mismo hilo lea dos veces el channel 
//si termina por completo su programa?
//Hacer experimento . . .

//Qué restricciones hay para estos ejercicios, se podría implementar una solución
// en la que se imprima las variables de un buffer

var (
	wg sync.WaitGroup
	ab = make(chan bool)
	b = make(chan bool)
	c = make(chan bool)
	e = make(chan bool)
	r = make(chan bool,1)
	cc = make(chan bool)
	dd = make(chan bool)
	cd = make(chan bool)
)

func A() {
	for {
		<- e
		fmt.Printf("A")
		time.Sleep(time.Millisecond)
		select{
		case <-r:
			e<- true
		default:
			ab<- true
		}
	}
}

func B() {
	for {
		<- e
		fmt.Printf("B")
		time.Sleep(time.Millisecond)
		select{
		case <-r:
			e<- true
		default:
			ab<- true
		}
	}
}

func C() {
	for {
		<- cc
		<-ab	
		fmt.Printf("C")
		time.Sleep(time.Millisecond)
		dd<- true
		r<- true
		cd <- true
	}
}

func D() {
	for {
		<- dd
		<- ab
		fmt.Printf("D")
		time.Sleep(time.Millisecond)
		cc <- true
		cd <- true
	}
}

func E() {
	for {
		<-cd
		fmt.Printf("E")
		time.Sleep(time.Millisecond)
		e<- true
	}
}

func main(){
	go A()
	go B()
	go C()
	go D()
	go E()
	e<- true
	cc<- true
	time.Sleep(5*time.Second)
}


