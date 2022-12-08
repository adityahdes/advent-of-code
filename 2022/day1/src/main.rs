mod utils;

fn main() {
    let input = utils::read_input_file();

    let part1_start = utils::start_timer();
    let part1_answer = part1(&input);
    let part1_time = part1_start.elapsed();
    println!("Part 1: {} ({:.2?})", part1_answer, part1_time);

    let part2_start = utils::start_timer();
    let part2_answer = part2(&input);
    let part2_time = part2_start.elapsed();
    println!("Part 2: {} ({:.2?})", part2_answer, part2_time)
}

fn part1(raw: &str) -> i32 {
    raw
        .split("\r\n\r\n")
        .into_iter()
        .map(|elf| {
            elf.lines()
                .map(|cal_str| cal_str.parse::<i32>().unwrap())
                .sum::<i32>()
        })
        .max()
        .unwrap()
}

fn part2(raw: &str) -> i32 {
    let mut elf_cal: Vec<i32> = raw
    .split("\r\n\r\n")
    .into_iter()
    .map(|elf| {
        elf.lines()
            .map(|cal_str| cal_str.parse::<i32>().unwrap())
            .sum::<i32>()
    }).collect();
    elf_cal.sort();
    elf_cal.iter().rev().take(3).sum()
}