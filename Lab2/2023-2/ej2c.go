
package main

import (
	"fmt"
	"time"
	"sync"
)

//No parece que fuera realmente random (A ó B)
//Encontrar una solución convincente

var (
	wg sync.WaitGroup
	ab = make(chan bool)
	b = make(chan bool)
	c = make(chan bool)
	d = make(chan bool)
	e = make(chan bool)
)

func A() {
	for {
		<- e
		fmt.Printf("A")
		time.Sleep(time.Millisecond)
		ab<- true
	}
}

func B() {
	for {
		<- e
		fmt.Printf("B")
		time.Sleep(time.Millisecond)
		ab<- true
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
	e<- true
	time.Sleep(5*time.Second)
}


