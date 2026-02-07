# freeCodeCamp Daily Coding Challenges

This repo tracks my daily (or not) solutions to freeCodeCamp challenges.

#### Programming Language: Python

## Challenges

- **2025-11-18** — [100 Characters](./2025-11-18_100_characters.py)
    - Needed help a little bit, also it is been while since I use `while` loop, I used index with `modulo` or `%` to loop this one to loop the same string over and over again.
    
- **2025-12-01** — [Miles to Kilometers](./2025-12-01_miles_to_kilometers.py)
    - Simple conversion, just multiply miles with `1.60934`.

- **2025-12-02** — [Camel to Snake](./2025-12-02_camel_to_snake.py)
    - Also similar to `vOwElcAsE` and `Consonant Case` with a little bit of parsing... Is this even considered a parsing? Actually, I am about to study it.

- **2025-12-23** — [Re:Fwd:Fw:Count](./2025-12-23_re_fwd_fw_count.py)
    - Man, if I did not know what is `regular expression` or `import re`, I will use a loop that check if the current character is `:` and then check the previous characters if it is `fwd` or `fw` or `re` by using index.

- **2026-01-06** — [vOwElcAsE](./2026-01-06_vowelcase.py)
    - Quite the same as `Consonant Case`, but I just made the `aeiouAEIOU` as a variable `vowel`.

- **2026-01-08** — [Sorted Array?](./2026-01-08_sorted_array.py)
    - Ez.

- **2026-01-10** — [Tic Tac Toe](./2026-01-10_tic-tac-toe.py)
    - It looks pretty inefficient, I mean I think there is a better way to do this. I suppose if statement conditions is the most easy to do.

- **2026-01-11** — [Par for the Hole](./2026-01-11_par_for_the_hole.py)
    - Took me while, I have no idea what is the rules or scoring in golf. I just ball it like, if I saw a hole, ball must go in.

- **2026-01-12** - [Plant the Crop](./2026-01-12_plant_the_crop.py)
    - I am thinking of using `while` or `for` in getting the... the that... I do not know. The plants things, yes. Well I will just give an example. `corn = 1` square meter, `wheat = 0.1` square meters, `soybeans = 0.5` square meter, `tomatoes = 0.25` square meters, `lettuce = 0.2` square meters. corn is already 1 so it is ok, but if soybeans is 0.5, in the math it should by times 2, if tomatoes then times 4, if wheat then times 10. With that, I think we get the point and know what is lettuce output. What I want to do is to automatically convert the square meter/s of crops to the times of it. `soybeans = 0.5, then soybeans = 2` or `if tomatoes = 0.25, then tomatoes = 4` like that, but I did not do it then just raw dog it once more.

- **2026-01-15** — [Array Swap](./2026-01-15_array_swap.py)
    - It seems I just raw dog this one, but hey, it works.

- **2026-01-16** — [Integer Hypotenuse](./2026-01-16_integer_hypotenuse.py)
    - It took me while that what I only need to know is if it is `perfect square` or not, so I should just return in `True` or `False` through some kind of condition. What really took me long is this part `c_root = int(c ** 0.5)`, I have to put `int()` in it for it to work properly with other test cases.

- **2026-01-18** — [Free Shipping](./2026-01-18_free_shipping.py)
    - It is pretty simple, I just review `dict` earlier so I have done it easily.

- **2026-01-19** — [Energy Consumption](./2026-01-19_energy_consumption.py)
    - Another day that took me while, I only need to times `calories_burned` with `calorie` and `watt_hours_used` with `watt_hour` and call it a day.

- **2026-01-20** — [Consonant Case](./2026-01-20_consonant_case.py)
    - The `elif case in ("aeiou" or "AEIOU")` stuck me up for too long, because the code reads the `"aeiou"` part only and call it a day, I changed it to `"aeiouAEIOU"` and I call it a night (night because it took me so long, it is so simple, very simple).

- **2026-01-21** — [Markdown Inline Code](./2026-01-21_markdown_inline_code_parser.py)
    - I use my smartness, my intelligence and my knowledge to make the most *inefficient* way of `parsing` this thing out.

- **2026-01-22** — [Class Average](./2026-01-22_class_average.py)
    - Simply `if` `else` statements, but took me a little bit of time to get the `print(get_average_grade([63, 69, 65, 66, 71, 64, 65]))` for it does not return `D` but the average score. Just need to do `average_score = int(average_score)` and done.

- **2026-01-24** — [Bingo! Letter](./2026-01-24_bingo_letter.py)
    - Same as `Class Average`, but shorter and better in eyes.

- **2026-01-25** — [Scaled Image](./2026-01-25_scaled-image.py)
    - I should have use `map()`, but as the sayings says, "if it ain't broke, don't fix it".

- **2026-01-26** — [Fuzzbizz Mini](./2026-01-26_fuzzbizz-mini.py)
    - Aboslutely easy.

- **2026-01-28** — [Flatten the Array](./2026-01-28_flatten_the_array.py)
    - Ok sorry for saying easy yesterday or perhaps the other day (don't refer from the date in this README, refer to the commit message regarding to the date). This time I need help from my friend `GitHub Copilot`. I dislike recursion and guess what? The answer is recursion to these jagged arrays, oh also `extend()` method, oh my how did I miss that simple method. Also I left out the comment for me to remember I screw up this one. I tried doing error handling `try` and `except` at first, perhaps it will work but the most inefficient way possible.

- **2026-01-29** — [Letters-Numbers](./2026-01-25_scaled-image.py)
    - I finally used what I learned, error handling. I used `try`, `except` and `finally`. I did not put it in the `elif character in numbers:` part though, but if a user put a number as the first index of a string, the function will definitely get cooked. I am pretty sure the error will be `IndexError`.

- **2026-02-02** — [Groundhog Day](./2026-02-02_groundhog_day.py)
    - Bro, I thought the output should be `"Looks like we'll have six more weeks of winter."` instead of `Looks like we'll have six more weeks of winter.`, so I just erased the quotes and back slashes.

- **2026-02-03** — [String Mirror](./2026-02-03_string_mirror.py)
    - Make an empty string, add the original string in empty string, reverse the original string then add it to the not empty string. Done.

- **2026-02-04** — [Truncate the Text](./2026-02-04_truncate_the_text.py)
    - Pretty simple stuffs this month, slice the string then add `...` or else return the original string.

- **2026-02-05** — [Pocket Change](./2026-02-05_pocket_change.py)
    - It is my first time using `map()` and `lambda` function, did not need looping with it, nice.

- **2026-02-06** — [2026 Winter Games Day 1: Opening Day](./2026-02-06_2026_winter_games_day_1_opening_day.py)
    - I just asked an AI to make a list of dict, yup, I aint going to type all if else statements in that one.

- **2026-02-07** — [2026 Winter Games Day 2: Snowboarding](./2026-02-07_2026_winter_games_day_2_snowboarding.py)
    - It is like the golf thing `Par for the Hole` I did, I have no idea what is the scoring or law or whatever in the snowboard (Im into tropical stuffs), but here we go again. I just got stuck a little bit in negative rotations and it is my first time seeing `abs()` function. I think it is `absolute`? Well I have seen absolute before but not as a function.