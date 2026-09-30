// To test this program, run `cargo test`.

use std::error::Error;
use std::fmt::Display;

pub fn encode(s: &str) -> String {
	let mut output: Vec<(char, usize)> = vec![];
	for c in s.chars() {
		if let Some(top) = output.last_mut() && top.0 == c {
			top.1 += 1;
		} else {
			output.push((c, 1usize));
		}
	}
	output.into_iter().fold(String::new(), |mut out, chargroup| {
		out.push_str(&format!("{}{}", chargroup.0, chargroup.1));
		out
	})
}

#[derive(Debug, Clone, PartialEq, Eq)]
pub enum RleDecodingError {
	NoNumber(String, usize),
	UnexpectedNumber(String)
}

impl Display for RleDecodingError {
	fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
		match self {
			Self::NoNumber(string, idx) => write!(f, "Number expected but not found in {string} at position {idx}"),
			Self::UnexpectedNumber(string) => write!(f, "The first character cannot be a number. The description of this algorithm means properly decoding an encoded numeric string is impossible. Either this is what you are trying to do, or the input is malformed: {string}"),
		}
    }
}

impl Error for RleDecodingError {}

pub fn decode(s: &str) -> Result<String, RleDecodingError> {
	let mut output: Vec<(char, u32)> = vec![];
	for (i, c) in s.chars().enumerate() {
		if let Some(digit) = c.to_digit(10) {
			if let Some(top) = output.last_mut() {
				top.1 *= 10;
				top.1 += digit;
			} else {
				return Err(RleDecodingError::UnexpectedNumber(s.to_string()));
			}
		} else {
			if let Some(top) = output.last() && top.1 == 0 {
				return Err(RleDecodingError::NoNumber(s.to_string(), i));
			} else {
				output.push((c, 0));
			}
		}
	}
	Ok(output.into_iter().fold(String::new(), |mut string, (c, repeat)| {
		let mut character = [0; 4];
		string.push_str(&(c.encode_utf8(&mut character).repeat(repeat as usize)));
		string
	}))
}

#[cfg(test)]
mod tests {
	use std::assert_matches;
	use super::*;

	#[test]
	fn encoding_decoding() {
		// Successful encoding/decoding pairs
		let cases = vec![
			("aaabbc", "a3b2c1"),
			("abc", "a1b1c1"),
			("zzzzzzzzzzzz", "z12"),
			("aAAa", "a1A2a1"),
			("", ""),
			("x", "x1")
		];

		for (decoded, encoded) in cases {
			assert_eq!(encode(decoded).as_str(), encoded);
			assert_eq!(decoded, decode(encoded).unwrap().as_str());
		}
	}

	#[test]
	fn decoding_fails() {
		// Unsuccessful decoding inputs
		let fail_cases = vec![
			"b0e0t0",
			"328",
			"nyoom"
		];

		for case in fail_cases {
			assert_matches!(decode(case), Err(_));
		}
	}
}
