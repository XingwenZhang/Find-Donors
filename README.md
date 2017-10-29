# Political Donors Analysis

## Author:

Xingwen Zhang (xingwenz@usc.edu)

## Requirements:

Python==3.6.1

## Usage:

The Python version is 3.6.

In MAC or Ubuntu: `bash run.sh`

The four parameters in run.sh are py file, input file, zip_code output file, date output file

To run the test:

`cd insight_testsuite`

`bash my_own_tests.sh`

After finishing, it will show `————Finished—————`in command line

## Validation Check

1. Check run.sh parameters number: if 4(.py, input, two outputs), then execute
2. Try to open file, if not, close the file that already opened
3. Check each line's length, only 21 is valid.
4. If ID or AMT is empty, skip; if other_id is not empty, skip
5. if zip_code is invalid, skip for zip_code output
6. if date is invalid, skip for date output

##  Directory Structure

```
├── README.md 
├── run.sh
├── src
│   └── find_political_donors.py
├── input
│   └── itcont.txt
├── output
|   └── medianvals_by_zip.txt
|   └── medianvals_by_date.txt
├── insight_testsuite
    └── run_tests.sh
    └── my_own_tests.sh
    └── tests
        └── test_1
        |   ├── input
        |   │   └── itcont.txt
        |   |__ output
        |   │   └── medianvals_by_zip.txt
        |   |__ └── medianvals_by_date.txt
        ├── my_own_test
            ├── input
            │   └── itcont.txt
            |── output
                └── medianvals_by_zip.txt
                └── medianvals_by_date.txt
```

## Test

In my-own-test's input, it contains empty line, random input and other invalid input.

## Contact

[LinkedIn](https://www.linkedin.com/in/xingwen-zhang/)

[Github](https://github.com/XingwenZhang)

[Blog](https://xingwenzhang.github.io/)



