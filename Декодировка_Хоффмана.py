def huffman_encode(text):
    freq = {}
    
    for ch in text:
        if ch not in freq:
            freq[ch] = 0
        freq[ch] += 1

    nodes = []
    for ch in freq:
        nodes.append([freq[ch], ch])

    while len(nodes) > 1:
        nodes = sorted(nodes, key=lambda x: x[0])
        
        left = nodes[0]
        right = nodes[1]
        nodes = nodes[2:]

        new = [left[0] + right[0], [left, right]]
        nodes.append(new)

    tree = nodes[0]
    codes = {}

    def build(node, code):
        if isinstance(node[1], str):
            codes[node[1]] = code
            return
        
        build(node[1][0], code + "0")
        build(node[1][1], code + "1")

    build(tree, "")

    encoded = ""
    for ch in text:
        encoded += codes[ch]

    return encoded, codes

text = "python"
encoded, codes = huffman_encode(text)
print("Закодировано:", encoded)

def huffman_decode(encoded, codes):
    if len(codes) == 1:
        ch = list(codes.keys())[0]
        return ch * len(encoded)

    rev = {}
    for ch in codes:
        rev[codes[ch]] = ch

    cur = ""
    result = ""

    for bit in encoded:
        cur += bit
        if cur in rev:
            result += rev[cur]
            cur = ""

    return result

decoded = huffman_decode(encoded, codes)
print("Декодировано:", decoded)