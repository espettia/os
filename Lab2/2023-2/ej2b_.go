package main

import (
	"fmt"
	"time"
	"sync"
)

//Idea 1 para obtener ACDEBCDEACDEBCDE
//Tener un cananl con buffer, pues estos no se bloquean
//A o B leerían el valor del buffer y verían si les corresponde o no el turno

//Idea 2 como el canal con buffer se bloquea solamente cuando se llena
//Podemos jugar con dos estados: vacío (se quiere recibir)
//lleno(se quiere mandar mensaje)

var (
	wg sync.WaitGroup
	mu sync.Mutex
	ab = make(chan bool)
	b = make(chan bool)
	c = make(chan bool)
	d = make(chan bool)
	e = make(chan bool)
	s = make(chan bool)
	t = make(chan bool)
)

func A() {
	for {
		<- s
		<- e
		fmt.Printf("A")
		time.Sleep(time.Millisecond)
		ab<- true
		t<- true
	}
}

func B() {
	for {
		<- t
		<- e
		fmt.Printf("B")
		time.Sleep(time.Millisecond)
		ab<- true
		s<- true
	}
}

func C() {
	for {
		<-ab	
		fmt.Printf("C")
		time.Sleep(time.Millisecond)
		c<- true
	}
}

func D() {
	for {
		<-c
		fmt.Printf("D")
		time.Sleep(time.Millisecond)
		d<- true
	}
}

func E() {
	for {
		<-d
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
	s<- true
	e<- true
	time.Sleep(5*time.Second)
}

