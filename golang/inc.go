package main

import (
	"fmt"
	"sync"
)

var (	
	a int
	wg sync.WaitGroup
	mu sync.Mutex
)


func worker(){
	defer wg.Done()
	for i:=0; i< 1000000; i++ {
		mu.Lock()
		a++
		mu.Unlock()
	}
}

func main(){
	for i:=0; i < 5; i++ {
		go worker()
		wg.Add(1)
	}
	wg.Wait()
	fmt.Println("Valor esperado 5000000 | valor obtenido:", a)
}
