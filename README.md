## Text To Piet
Text To Piet is a program that converts a string of text into a Piet image, using characters to represent each pixels, for people that are more comfortable working with text.

This project was originally meant for personal use, so not all characters make perfect sense, it is nonetheless in a fonctional state currently.


Some features planned for better public usage are:
- [ ] Reworking the character list to make more sense
- [ ] Refactoring to be an importable module
- [ ] Upload to PyPi
- [ ] Add a CLI
- [ ] Error handling in case of bad input

Each characters and their corresponding colors are:
- `0`: light red
- `r`: red
- `R`: dark red
- `1`: light yellow
- `y`: yellow
- `Y`: dark yellow
- `2`: light green
- `g`: green
- `G`: dark green
- `3`: light cyan
- `c`: cyan
- `C`: dark cyan
- `4`: light blue
- `b`: blue
- `B`: dark blue
- `5`: light magenta
- `m`: magenta
- `M`: dark magenta
- `.`: white
- `#`: black

In it's current state, this program read the file `text.txt` as input, and outputs the image as `output.png`.