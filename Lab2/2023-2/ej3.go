/*
Tener en cuenta que el index puede variar en el transcurso de la función
*/
package main

import (
	"fmt"
	"sync"
)

var (
	buffer	[5]int = [5]int{-1, -1, -1, -1, -1,}
	index 	int
	wg 	sync.WaitGroup
	mu 	sync.Mutex

	contador = make(chan int, 4)
	prev int
)

func productor() {
	for n:= 0; n < 20; {
		item := n
		mu.Lock()
		select{
		case contador<-n%5:
			index = n%5
			buffer[index] = item
			fmt.Printf("productor %d %d %v\n", index, item, buffer)
			n++
		default:
		}
		mu.Unlock()
	}
	wg.Done()
}

func consumidor(){
	var item int
	for n:=0; n < 20;{
		mu.Lock()
		select{
		case <-contador:
			index = n%5
			item = buffer[index]
			buffer[index] = -1
			fmt.Printf("consumidor %d %d %v\n", index, item, buffer)
			n++
		default:
		}
		mu.Unlock()
	}
	wg.Done()
}	

func main() {
	wg.Add(2)
	go consumidor()
	go productor()
	wg.Wait()
}
