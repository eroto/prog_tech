use std::io;

fn main()
{
    let name = "Juan";
    let mut name2 = String::new();
    println!("Hello world,{name}");

    println!("Enter a name:");

    io::stdin()
        .read_line(&mut name2)
        .expect("Failed to read line");

    println!("Hello {name2}!");
}
