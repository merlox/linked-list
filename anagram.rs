fn main() {
    println!("{}", is_anagram(String::from("loop"), String::from("pool")));
}

fn is_anagram(string1: String, string2: String) -> bool {
    let mut is_valid = false;
    if merge_sort(string1) == merge_sort(string2) {
        is_valid = true;
    }
    return is_valid;
}

fn merge_sort(my_string: String) -> String {
    if my_string.len() <= 1 {
        return my_string;
    }
    let mut result = String::from("");
    let mid = my_string.len() / 2;
    let mut left = merge_sort(String::from(&my_string[..mid]));
    let mut right = merge_sort(String::from(&my_string[mid..]));
    let mut left_index = 0;
    let mut right_index = 0;

    while left_index < left.len() && right_index < right.len() {
        let left_element = left.chars().nth(left_index).unwrap();
        let right_element = right.chars().nth(right_index).unwrap();
        if left_element < right_element {
            result.push(left_element);
            left_index += 1;
        } else {
            result.push(right_element);
            right_index += 1;
        }
    }

    while left_index < left.len() {
        result.push(left.chars().nth(left_index).unwrap());
        left_index += 1;
    }

    while right_index < right.len() {
        result.push(right.chars().nth(right_index).unwrap());
        right_index += 1;
    }

    return result;
}
