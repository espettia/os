package main

import(
	"fmt"
	"os"
	"sync"
	"time"
)

var(
	wg sync.WaitGroup
	ch1 chan int = make(chan int)
	ch2 chan int = make(chan int)
	ch3 chan int = make(chan int)
	ch4 chan int = make(chan int)
	ch5 chan int = make(chan int)
) 

func admin(c chan string){
	var cad string
	for {
		cad = <- c
		switch cad{
			case "A":
				ch1 <- 1
			case "B":
				ch2 <- 1
			case "C":
				ch3 <- 1
			case "D":
				ch4 <- 1
			case "E":
				ch5 <- 1	
		}
		time.Sleep(time.Millisecond)
		c <- cad
	}
}


func worker1(){
	for{
		<- ch1
		fmt.Print("A")
	}
	wg.Done()
}

func worker2(){
	for{
		<- ch2
		fmt.Print("B")
	}
	wg.Done()
}
func worker3(){
	for{
		<- ch3
		fmt.Print("C")
	}
	wg.Done()
}
func worker4(){
	for{
		<- ch4
		fmt.Print("D")
	}
	wg.Done()
}
func worker5(){
	for{
		<- ch5
		fmt.Print("E")
	}
	wg.Done()
}
func main(){
	var cadena string

	c := make(chan string, 100)
	for i := 1; i < len(os.Args); i++{
		cadena = os.Args[i]
		c <- cadena
	}
	wg.Add(5)
	go admin(c)
	go worker1()
	go worker2()
	go worker3()
	go worker4()
	go worker5()
	wg.Wait()
}