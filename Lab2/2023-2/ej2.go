package main

import (
	"fmt"
	"time"
	"sync"
)

var (
	wg sync.WaitGroup
)

func A() {
	for {
		fmt.Printf("A")
	}
}

func B() {
	for {
		fmt.Printf("B")
	}
}

func C() {
	for {
		fmt.Printf("C")
	}
}

func D() {
	for {
		fmt.Printf("D")
	}
}

func E() {
	for {
		fmt.Printf("E")
	}
}
func main(){
	go A()
	go B()
	go C()
	go D()
	go E()
	time.Sleep(5*time.Second)
}


