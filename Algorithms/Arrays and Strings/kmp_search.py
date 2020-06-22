
'''
KMP String Search Algorithm
'''
def kmp_search(pat, txt):
    m = len(pat)
    n = len(txt) 

    res = []

    lps = compute_lps_array(pat)
    j = 0 
  
    i = 0 
    while i < n: 
        if pat[j] == txt[i]:
            i += 1
            j += 1
            
        # match found
        if j == m:
            res.append(i-j)
            j = lps[j-1]
  
        # mismatch after j matches 
        elif i < n and pat[j] != txt[i]:
            # fo not match lps[0..lps[j-1]] characters
            # they will match anyway 
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
    return res

def compute_lps_array(pat):
    m = len(pat)
    lps = [0]*m
    
    j = 0
    i = 1
    
    while i < m:
        if pat[i] == pat[j]:
            lps[i] = j+1
            j += 1
            i += 1
        
        else:
            if j != 0:
                j = lps[j-1]
            else:
                lps[i] = 0
                i += 1
    return lps
  
txt = "ABABDABACDABABCABABABABCABAB"
pat = "ABABCABAB"

print(kmp_search(pat, txt))
