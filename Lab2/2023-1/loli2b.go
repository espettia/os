package main
import(
	"fmt"
	"sync"
)
var(
	 wg sync.WaitGroup
	 chCons chan bool = make(chan bool)
	 chProd chan bool = make(chan bool)
)


func main(){
	ch := make(chan int,100)
	wg.Add(3)
	go producer(ch,1)
	go producer(ch,2)
	go producer(ch,3)
	go consumer(ch,1)
	go consumer(ch,2)
	wg.Wait()
	fmt.Printf("Quedan %d productos\n", len(ch))
}

func producer(ch chan int, nProd int){
	for index :=  nProd * 10; index <= nProd * 10 + 10; index++{
		fmt.Printf("PRODUCTOR %v: envia %v\n",nProd,index)
		ch <- index 
		chCons <- true
		<- chProd
	}
	wg.Done()
}

func consumer(ch chan int, nCons int){
	for{
		<- chCons
		val := <- ch
		chProd <- true
		fmt.Printf("CONSUMIDOR %v: lee %v\n",nCons,val)
	}
}
