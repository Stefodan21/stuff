def ip(s):
    u = set()
    
    for c in s:
        if c.isalpha():
            u.add(c.lower())
        
    return len(u) == 26  
        

s = "The quick brown fox jumps over the lazy dog"
print(ip(s))

s = "The dog jumped"
print(ip(s))

def rs(s):
    
    return s[::-1]

s = "live"
print(rs(s))

def runi(s):
    
    freq = {}
    
    for c in s:
        freq[c] = freq.get(c, 0) + 1
        
    for i, (letters, count) in enumerate(freq.items()):
        if count == 1:
            return i
        
    return -1

s = "leetcode"
print(runi(s))

s = "loveleetcode"
print(runi(s))

s = "aabb"
print(runi(s))
        
        
# def min_distance(words, word1, word2):
#     idx1 = [i for i, w in enumerate(words) if w == word1]
#     idx2 = [i for i, w in enumerate(words) if w == word2]
#     return min(abs(i - j) for i in idx1 for j in idx2)


def remove_char(s, n):
    
    return "".join(c for i, c in enumerate(s) if i != n)

s = "typpo"
fixed_s = remove_char(s, 3)
print(fixed_s)
            

def vowel_count(s):
    v = set("aeiou")
    
    return sum(c.lower() in v for c in s)

my_str = "hello world"
my_str2 = "aAaAaAaAAA"
my_str3 = "ths strng s mssng vwls"

count1 = vowel_count(my_str)
print(count1)
count2 = vowel_count(my_str2)
print(count2)
count3 = vowel_count(my_str3)
print(count3)

def reverse_sentence(sentence):
    words = sentence.split()

    return " ".join(words[::-1])

sentence = "I solemnly swear I am up to no good"
print(reverse_sentence(sentence))

def compress_string(my_str):
    freq = {}
    
    for c in my_str:
        freq[c] = freq.get(c, 0) + 1
        
    return "".join(f"{c}{v}" for c, v in freq.items())

my_str = "aaaaabbcccd"
compressed_Str = compress_string(my_str)
print(compressed_Str)

my_str2 = "abcde"
compressed_Str2 = compress_string(my_str2)
print(compressed_Str2)
    
def find_the_needle(haystack, needle):
    
    return haystack.find(needle)

haystack = "tobeornottobe"
needle = "be"
print(find_the_needle(haystack, needle))

haystack2 = "leetcode"
needle2 = "leeto"
print(find_the_needle(haystack2, needle2))


def choose_pokemon(my_pokemon):
	for pokemon in my_pokemon:
		print(f"{pokemon} I choose you!")
  
my_pokemon = ["Eevee", "Charizard", "Pikachu" ]

choose_pokemon(my_pokemon)

def rotate_left(s, n):
    return s[n:] + s[:n]
        
    

s = "rotation"
print(rotate_left(s, 2))


def first_repeated_char(s):
    seen = set()

    for i, c in enumerate(s):
        if c in seen:
            return i
        seen.add(c)

    return None


def find_difference(s1, s2):
    m = set(s1)
    
    for i , s in enumerate(s2):
        if s not in m:
            return s
        
s1 = "abcd"
s2 = "baedc"
print(find_difference(s1, s2))
        
def length_of_longest_substring(s):
    seen = set()
    left = 0
    longest = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        longest = max(longest, right - left + 1)

    return longest
    