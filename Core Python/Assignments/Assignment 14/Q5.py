strings = ["flower", "flow", "flight"]

if not strings:
    print("Longest common prefix = ''")
else:
    prefix = strings[0]
    for s in strings[1:]:
        temp_prefix = ""
        for i in range(min(len(prefix), len(s))):
            char_set = {prefix[i], s[i]}
            if len(char_set) == 1:
                temp_prefix += prefix[i]
            else:
                break
        prefix = temp_prefix

    print("Longest common prefix =", prefix)