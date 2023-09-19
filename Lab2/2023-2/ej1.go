package main

import (
	"fmt"
	"sync"
)

var (
	wg sync.WaitGroup
	c2 = make(chan int)
	c3 = make(chan int)
	c4 = make(chan int)
)

func worker1(){
	defer wg.Done()
	<-c2
	fmt.Printf("Sistemas ")
	c3<- 1
	close(c3)
}

func worker2(){
	defer wg.Done()
	fmt.Printf("INF239 ")
	c2<- 1
	close(c2)
}

func worker3(){
	defer wg.Done()
	<-c3
	fmt.Printf("Operativos ")
	c4<- 1
	close(c4)
}

func worker4(){
	<-c4
	fmt.Printf("\n")
	wg.Done()
}

func main(){
	wg.Add(4)
	go worker1()
	go worker2()
	go worker3()
	go worker4()
	wg.Wait()
	fmt.Println()
}
