
import UIKit

// Define a custom struct to represent a person
struct Person {
    var name: String
    var age: Int
}

// Create an array of Person objects
var people: [Person] = [
    Person(name: "Alice", age: 28),
    Person(name: "Bob", age: 35),
    Person(name: "Charlie", age: 20),
    Person(name: "David", age: 42)
]

// Filter the people array to get only those who are above 30 years old
let aboveThirty = people.filter { $0.age > 30 }

// Print the names of people above 30
for person in aboveThirty {
    print("\(person.name) is above 30 years old.")
}
