package main

import (
	"fmt"
	"time"
	"sync"
)

var (
	wg sync.WaitGroup
	a = make(chan bool)
	b = make(chan bool)
	c = make(chan bool)
	d = make(chan bool)
	e = make(chan bool)
)

func A() {
	for {
		<-e
		fmt.Printf("A")
		time.Sleep(time.Millisecond)
		a<- true
	}
}

func B() {
	for {
		<-a
		fmt.Printf("B")
		time.Sleep(time.Millisecond)
		b<- true
	}
}

func C() {
	for {
		<-b
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


