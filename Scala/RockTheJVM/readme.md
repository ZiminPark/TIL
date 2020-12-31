16. Abstract Classes and Traits - 12/22
```
   traits vs abstract classes
   1 - traits do not have constructor parameters
   2 - multiple traits may be  inherited by the same class
   3 - traits = behavior, abstract class = "thing"
```

18. Generics - 12/30
```Scala
   class Animal

   class CovariantList[+A]
   class InvariantList[A]
   class Trainer[-A]
   class Cage[A <: Animal](animal: A)
   
   class MyList[+A] {
      def add[B >: A](element: B): MyList[A] = ???
   }
   
```
19.Anonymous Class - 12/31
```Scala
   trait Aniaml {
      def eat: Unit
   }
   
   val predator = new Animal {
      override def eat: Unit = println("RAW")
   }
```


21. Case Classes - 12//31
![CaseClass](https://github.com/ZiminPark/TIL/blob/master/Scala/RockTheJVM/IMG_A94EEF25B52A-1.jpeg)
