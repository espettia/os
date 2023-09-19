/*
La secuencia de ejecución consiste en los bloqueos y recepciones de mensajes
*/
//Qué pasa cuando varios hilos quieren acceder al mismo canal bufferizado?

package main

import "fmt"
import "sync"

var mu sync.Mutex
var muc sync.Mutex
var index int = 0
var wg sync.WaitGroup
var wgp sync.WaitGroup

func main() {
	ch := make(chan int,100)

	wg.Add(5)
	wgp.Add(3)

	go producer(ch)
	go producer(ch)
	go producer(ch)

	go consumer(ch)
	go consumer(ch)

	wgp.Wait()
	close(ch)
	wg.Wait()
}

func producer(ch chan int){
	defer wg.Done()
	defer wgp.Done()
	count := 0
	for count<10 {
		mu.Lock()
		fmt.Printf("PRODUCTOR: envia %v\n", index)
		ch<-index
		index++
		mu.Unlock()
		count++
	}
}

//Qué pasa cuando varios hilos quieren acceder al mismo canal bufferizado?
//Cómo leer hasta el último valor de un buffer?
func consumer(ch chan int){
	defer wg.Done()
	for val:= range ch{
		fmt.Printf("CONSUMIDOR: lee %v\n", val)
	}
}
