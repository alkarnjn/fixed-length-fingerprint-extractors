#%% code to compute hamming distance of 2 strings

def hamming_dist(s1, s2):
    if len(s1) != len(s2):
        return -1
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))

# driver code
s1 = "11110000"
s2 = "11111000"
print(f"{hamming_dist(s1, s2):=}")
# %%
