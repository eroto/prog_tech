

//Live cycles

/*
fn ret_reference<'a>(num: &'a i32) -> &'a i32
{
    num = &3;
    return num;
}*/

fn main()
{
    let var_x = 5;

    //let var_r = ret_reference(&var_x);

    println!("Value {}",var_x);


    //Signed ints
    let _var_integer_32: i32 = 10;
    let _var_integer_64: i64 = 8154;

    //Unsigned ints
    let _var_unsigned_8: u8 = 255;

    let var_big_number_64: i64 = 10_345_850;

    //float 32 bits
    let var_a_float: f32 = 3.1416;

    //tipos Booleanos
    let _var_a_bool: bool = true;
    let _var_a_bool: bool = false;

    //tipos char
    let _var_a_char: char = 'a';
    let var_emoji: char = '💯';

    //tuplas
    let tupla_32bits: (i32, f64, char) = (500,3.1416, 'W');

    //Aqui se hace un unpacking de la tupla
    let (var_x, _var_y, _var_z) = tupla_32bits;

    let un_arreglo: [i32; 3] = [777,2,3];

    let mut nums = vec![1,2,3,4,5];

    nums.push(6); //[1,2,3,4,5]

    //arreglos
    //let arreglo_32bits[]: int32;

    println!("var_a_float:{}",var_a_float);
    println!("var_big_number_64:{}",var_big_number_64);
    println!("var_emoji:{}",var_emoji);
    //println!("{} - {} - {}",tupla_32bits.0,tupla_32bits.1,tupla_32bits.2)
    println!("{}",var_x);
    println!("{}", un_arreglo[0]);
    nums

}
