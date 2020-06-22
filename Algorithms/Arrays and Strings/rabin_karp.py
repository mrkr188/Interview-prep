def rabin_karp(txt, pat):
    m, n = len(pat), len(txt)
    if m > n:
        return []
    res = []

    # base value for the rolling hash function
    a = 26
    # modulus value for the rolling hash function to avoid overflow
    modulus = 2**31
    
    # lambda-function to convert character to integer
    txt_to_int = lambda i : ord(txt[i]) - ord('a')
    pat_to_int = lambda i : ord(pat[i]) - ord('a')
    
    # compute the hash of strings txt[:m], pat[:m]
    txt_hash = pat_hash = 0
    for i in range(m):
        txt_hash = (txt_hash * a + txt_to_int(i)) % modulus
        pat_hash = (pat_hash * a + pat_to_int(i)) % modulus
    if txt_hash == pat_hash:
        return 0
            
    # const value to be used often : a**m % modulus
    am = pow(a, m, modulus) 
    for start in range(1, n-m+1):
        # compute rolling hash in O(1) time
        txt_hash = (txt_hash*a - txt_to_int(start-1)*am + txt_to_int(start+m-1)) % modulus
        if txt_hash == pat_hash:
            res.append(start)

    return res

txt = "ABABDABACDABABCABABABABCABAB"
pat = "ABABCABAB"

print(rabin_karp(txt, pat))

