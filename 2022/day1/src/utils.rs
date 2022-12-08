use std::{fs, time::Instant};

pub fn read_input_file() -> String {
    let file_path = format!("../input.txt");
    fs::read_to_string(file_path).expect("Should have been able to read the file")
}

pub fn start_timer() -> Instant {
    Instant::now()
}