package main
import (
	"fmt"
	"math/rand"
	"time"
	"sync"
)
//siempre HHO
var( 
	chSalto chan int = make(chan int)
	condVar sync.NewCond(&sync.Mutex{})
)

func Hidrogeno(){
	time.Sleep(time.Duration(rand.Float64()) * time.Second)
	fmt.Print("H")
	wg.Done()
}
func Oxigeno(){
	time.Sleep(time.Duration(rand.Float64()) * time.Second)
	fmt.Print("O")
	wg.Done()
}
func CambiodeLinea(){
	time.Sleep(time.Duration(rand.Float64()) * time.Second)
	<-chSalto
	fmt.Println()
	wg.Done()
}

func main(){
	wg.Add(40)
	for i := 0; i < 40; i++{
		go Hidrogeno()
	}
	for j := 0; j < 20; j++{
		go Oxigeno()
	}
	for z := 0; z < 10; z++{
		go CambiodeLinea()
	}
	wg.Wait()
}
