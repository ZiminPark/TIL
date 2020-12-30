16. Abstract Classes and Traits - 12/22
```
   traits vs abstract classes
   1 - traits do not have constructor parameters
   2 - multiple traits may be  inherited by the same class
   3 - traits = behavior, abstract class = "thing"
```

17. Generics - 12/30
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
