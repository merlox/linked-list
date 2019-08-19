fn main() {
    println!("Are the words 'camara' and 'macaar' anagrams?: {}", is_anagram(String::from("camara"), String::from("macaar")));
    println!("Are the words 'doggy' and 'carrds' anagrams?: {}", is_anagram(String::from("doggy"), String::from("carrds")));
    println!("Are the words 'magic' and 'agicm' anagrams?: {}", is_anagram(String::from("magic"), String::from("agicm")));
}

fn is_anagram(string_one: String, string_two: String) -> bool {
    let mut result = false;
    if merge_sort(string_one) == merge_sort(string_two) {
        result = true;
    }
    return result;
}

fn merge_sort(my_string: String) -> String {
    if my_string.len() <= 1 {
        return my_string;
    }

    let mut sorted_string = String::from("");
    let mid = my_string.len() / 2;
    let left = merge_sort(String::from(&my_string[..mid]));
    let right = merge_sort(String::from(&my_string[mid..]));
    let mut left_index = 0;
    let mut right_index = 0;

    while left_index < left.len() && right_index < right.len() {
        let left_element = left.chars().nth(left_index).unwrap();
        let right_element = right.chars().nth(right_index).unwrap();
        if left_element < right_element {
            sorted_string.push(left_element);
            left_index += 1;
        } else {
            sorted_string.push(right_element);
            right_index += 1;
        }
    }

    while left_index < left.len() {
        let left_element = left.chars().nth(left_index).unwrap();
        sorted_string.push(left_element);
        left_index += 1;
    }

    while right_index < right.len() {
        let right_element = right.chars().nth(right_index).unwrap();
        sorted_string.push(right_element);
        right_index += 1;
    }

    return sorted_string;
}
