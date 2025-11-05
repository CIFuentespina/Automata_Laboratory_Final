

MEALY = {
    'A': {'0': ('A', 'A'), '1': ('A', 'B')},
    'B': {'0': ('C', 'A'), '1': ('D', 'B')},
    'C': {'0': ('D', 'C'), '1': ('B', 'B')},
    'D': {'0': ('B', 'B'), '1': ('C', 'C')},
    'E': {'0': ('D', 'C'), '1': ('E', 'C')},
}

def build_moore_from_mealy(mealy, start='A'):
   
    moore_trans = {}
    outputs = {}

  
    moore_states = set()
    for p in mealy:
        for sym in ('0', '1'):
            q, o = mealy[p][sym]
            moore_states.add((q, o))

    # Name them like "Q_O" (e.g., "A_A")
    for (q, o) in moore_states:
        name = f"{q}_{o}"
        outputs[name] = o
        moore_trans[name] = {}

    
    for (p, op) in moore_states:
        pname = f"{p}_{op}"
        for sym in ('0','1'):
            q, o = mealy[p][sym]
            moore_trans[pname][sym] = f"{q}_{o}"

   
    start_name = f"{start}_init"
    moore_trans[start_name] = {}
    outputs[start_name] = None 
    for sym in ('0','1'):
        q,o = mealy[start][sym]
        moore_trans[start_name][sym] = f"{q}_{o}"

    return start_name, moore_trans, outputs

def moore_process(inp, start_name, moore_trans, outputs):
    state = start_name
    out = []
    for ch in inp:
        # transition
        state = moore_trans[state][ch]
        out.append(outputs[state])
    return ''.join(out)

if __name__ == "__main__":
    start_name, moore_trans, outputs = build_moore_from_mealy(MEALY, start='A')

    tests = ["00110", "11001", "1010110", "101111"]

    for t in tests:
        o = moore_process(t, start_name, moore_trans, outputs)
        print(f"input: {t}   output: {o}")
