## Problem 2: This problem was asked by Amazon

Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent repeated successive characters as 
a single count and character. For example, the string **"AAAABBBCCDAA"** would be encoded as **"4A3B2C1D2A"**.

Implement run-length encoding and decoding. You can assume the string to be encoded have no digits and consists solely of 
alphabetic characters. You can assume the string to be decoded is valid.

### Output

With the driver function implemented in the algorithm:

```
if __name__ == "__main__":  # Driver function
    print("The encode version of AAAABBBCCDAA is:")
    print(encode("AAAABBBCCDAA"))
    print("The decode version of 1a2b3c is:")
    print(decode("1a2b3c"))

```

The output when you run it on the terminal is:
```
C:\>python Problem2.py
The encode version of AAAABBBCCDAA is:
4A3B2C1D2A
The decode version of 1a2b3c is:
abbccc

```
