import poseidon

def gen_n_hash(n):
    security_level = 128
    input_rate = 3
    t_opt = 4
    full_round = 8
    partial_round = 56
    alpha = 5
    poseidon_pre_generated = poseidon.OptimizedPoseidon(poseidon.HashType.CONSTINPUTLEN, poseidon.parameters.prime_255, 
                                                    security_level, alpha, input_rate, t_opt,
                                                    full_round=full_round, partial_round=partial_round,
                                                    rc_list=poseidon.parameters.round_constants_neptune, 
                                                    mds_matrix=poseidon.parameters.matrix_neptune)
    
    sk =12345
    with open(f"{n}_hash.txt", 'w') as file:
        for i in range(0, n):
            input_vec_2 = [sk, i]
            #print("Input: ", input_vec_2)
            poseidon_output = poseidon_pre_generated.run_hash(input_vec_2)
            #print("Output: ", hex(int(poseidon_output)))
            file.write(hex(int(poseidon_output)) + "\n")

if __name__ == "__main__":
    gen_n_hash(100000)