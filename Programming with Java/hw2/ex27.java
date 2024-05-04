abstract class Animal {

    String name;
    static int animals = 0;

    public Animal(String n) {
        name = n;
        animals++;
    }

    public abstract void speak();

    public static int numberOfAnimals() {
        return animals;
    }

} // Animal



class Dog extends Animal {

    String sound = "woof";
    static int dogs = 0;

    public Dog(String n) {
        super(n);
        dogs++;
    }

    public static int numberOfDogs() {
        return dogs;
    }

    @Override
    public void speak() {
        System.out.println(this.name + ": " + this.sound);
    }
} //Dog



class Cat extends Animal {

    private static int cats=0;
    String sound = "miaou";

    public Cat(String n) {
        super(n);
        cats++;
    }

    public static int numberOfCats() {
        return cats;
    }

    @Override
    public void speak() {
        System.out.println(this.name + ": " + this.sound);
    }
} // Cat

 

public class ex27 {

    public static void main(String[] args) {

        Animal[] animal = { new Cat("stella"), new Cat("ziggy"), new Dog("azor") };

        System.out.println("cats: "+Cat.numberOfCats());
        System.out.println("dogs: "+Dog.numberOfDogs());
        System.out.println("animals: "+Animal.numberOfAnimals());

        for ( int i = 0; i < animal.length; i++ )
            animal[i].speak();
    }
}