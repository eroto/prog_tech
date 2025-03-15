//use std::io;

//Clone a variable

fn main()
{
    //hay un dueño, string1, de la memoria que contiene "Hello"
    let string1 = String::from("Hello");

    //Ahora string2 es el dueño de la memoria que contiene "Hello"
    let string2 = string1;

    {
        let string3 = string2.clone();
        println!("string3:{string3}");
    }
    //An error is arised because string3 is out of scope
    //println!("string3:{string3}");

}
