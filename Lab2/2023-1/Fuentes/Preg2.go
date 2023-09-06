package main

import "fmt"

func main() {
	ch := make(chan int)
	done := make(chan bool)
	go producer(ch, done)
	go consumer(ch)
	<-done
}

func producer(ch chan int, done chan bool) {
	for index := 0; index < 10; index++ {
		fmt.Printf("PRODUCTOR: envia %v\n", index)
		ch <- index
	}
	close(ch)
	done <- true
}

func consumer(ch chan int) {
	for val := range ch {
		fmt.Printf("CONSUMIDOR: lee %v\n", val)
	}
}
