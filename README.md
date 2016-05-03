# hexs

This is a very small package which contains functions that format hex strings.
The purpose of this formatting is to make a given hex string of even length,
remove a "0x" prefix if present, and remove a "L" suffix if present.

It also includes a convenience function, `hexs()`, which calls the built-in `hex()`
function and formats the result.

## Usage

```
>>> from hexs import is_hex, hexs, format_hex
>>> hexs(5)
'05'
>>> format_hex('0x5')
'05'
>>> is_hex('g')
False
>>> is_hex(29)
False
>>> is_hex('f')
True
```

## License

MIT License.
