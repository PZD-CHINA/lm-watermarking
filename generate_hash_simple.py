import poseidon

def main():
    poseidon_simple, t = poseidon.parameters.case_simple()

    for i in range(0, 100):
        input_vec = [i] 
        poseidon_digest = poseidon_simple.run_hash(input_vec)
        print(f"Input {i}: Hash = {hex(int(poseidon_digest))}")

if __name__ == "__main__":
    main()
