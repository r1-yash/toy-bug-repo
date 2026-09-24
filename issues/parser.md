# Multiline parser drops the final line of input text

## Description
When parsing multiline string inputs into clean lines, `parse_lines` consistently omits the last line from the output list. For single-line inputs, it returns an empty list.

## Expected Behavior
All non-empty lines from the input text should be returned in the resulting list, including the final line.
