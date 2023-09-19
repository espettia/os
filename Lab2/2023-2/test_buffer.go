package main

import (
	"fmt"
	"sync"
)

var (
	wg sync.WaitGroup
)

func f(c chan int){
	for i:= range c{
		fmt.Println("hole ", i)
	}
	wg.Done()
}

func main(){
	c := make(chan int, 100)
	wg.Add(1)
	for i:=0; i < 10; i++ {
		c<-i
	}
	go f(c)
	wg.Wait()
}

