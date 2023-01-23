# Utility function to compare version 1 and version2
def compare(v1, v2):
    # make sure both version 1 and version 2 not null
    if not v1 or not v2:
        return 0
    
    # converting versions to string whether number or string
    # splitting versions to list
    v1, v2 = str(v1).split("."), str(v2).split(".")

    # 0 length means both v1 & v2 is impossible to compare
    if len(v1) == 0 or len(v2) == 0:
        return 0
    
    i, len1 = 0, len(v1)
    j, len2 = 0, len(v2)
    # compare sub versions until find correct answer
    # or one index will reach the its length and stop
    while (i < len1 and j < len2):
        sub_v1, sub_v2 = int(v1[i]), int(v2[j])
        if sub_v1 > sub_v2:
            return 1
        elif sub_v1 < sub_v2:
            return -1
        i += 1 
        j += 1
    
    # condition version1 would be greater
    if i < len1 and j == len2:
        return 1
    # condition version2 would be greater
    if i == len1 and j < len2:
        return -1

    # other cases
    return 0

tests = [
    # version1, version2, correct answer
    ("1.2", 1.2, 0),
    ("1.3", 1.2, 1),
    ("1.3", 1.9, -1),
    ("1.2", "1.2", 0),
    ("1.2.1", "1.2", 1),
    ("1.2.1", "1.2.1.9", -1),
    ("1.3.4", "1.10", -1),
]

for test in tests:
    v1, v2, corr_ans = test
    ans = compare(v1, v2)
    print ("Answer is %s with %r" % (
        "correct" if ans == corr_ans else "incorrect",
        (v1, v2))
    )

