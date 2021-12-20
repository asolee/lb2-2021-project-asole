import sys

list = ['4XH9_A','6XD4_A','6X42_A','5M8R_A','5TSQ_A', '6PED_A', '5B19_A', '6MS4_A', '5L09_A', '5GMC_A', '6V4W_A', '6G5Q_A', '6E66_A', '6JYX_A', '6QWQ_A', '5T5I_B', '7D88_A', '5YXT_A', '5YX6_A', '7CT7_A', '6MV1_A', '6CVS_A', '5AZ4_A', '6NJ0_A', '6VOQ_A', '5CD2_A', '7A1R_A', '6KOY_A', '4YSI_A', '6R6M_A', '5GY3_A', '5IUY_A', '5ZON_A', '4XR9_A', '6TE7_A', '6NS4_A', '6MW4_A', '7NUW_A', '5YLW_A', '6TAE_A', '6GJT_A', '6XP9_A', '7A0T_A', '6ULY_A', '6X42_A', '7MMZ_A', '6S1V_A', '5M8R_A', '5H6S_A', '4ZEW_A', '5T9P_A', '5OLJ_A', '5EX2_A', '6KXT_A', '6DMF_A', '5XEF_A', '5AA5_C', '6GFL_A', '5ZQJ_A', '5JSI_A', '6VCL_B', '5OR3_A', '7BRF_A', '6BZ9_A', '6W6A_A', '5Z5M_A', '4YN3_A', '4Z8S_B', '4S0U_C', '6OM4_A', '6IEW_A', '4ZHB_A', '5IJA_A', '7LS4_A', '6KSF_A', '5EO9_A', '6HG6_A', '5J90_A', '5Z44_A', '5K4A_A', '5HIW_A', '7CGZ_A', '6LUG_A', '5JB2_A', '6NYC_A', '5ZI1_A', '5ZNI_A', '5UPQ_A', '5ZLQ_A', '6IUF_A', '5CA5_A', '6G1O_A', '7A0H_A', '6RLO_C', '5BS5_A', '7NZJ_A', '7RBQ_A', '5L95_A', '5LXZ_A', '6BTG_A', '5HKC_A', '4YLE_A', '4YV7_A', '6XN8_A', '7LOL_A', '5KIA_A', '6M7X_A', '7OW9_A', '6IBE_A', '6LED_A', '5MSX_A', '6WQ1_A', '5H7W_A', '6V98_A', '7CT6_A', '6G9P_A', '7DAI_A', '5YD6_A', '5FQ4_A', '5C92_A', '5IX3_A', '6FYW_A', '6YY3_D', '7L9W_A', '5JFZ_A', '5KZV_A', '4YXM_A', '6P2K_A', '6EFG_A', '6Q3T_A', '6MHL_A', '5ECX_A', '5CYG_A', '7EZL_A', '6I3Q_A', '5VE3_A', '6WH1_A', '5W39_A', '5TD6_A', '6U94_A', '5XKO_A', '7C1I_A', '6C3Y_A', '6OM8_A', '6P8E_A', '5MUA_A', '6K9Z_A', '5EV7_A', '6A77_A', '4ZIY_A', '5YRX_A', '4YN2_A', '5Z59_A', '5YZ1_A']
chain = ""
print(len(list))

def fasta_dssp(file,file2):
        input = open(file,"r")
        output = open(file2,"w")
        for i in range(28):
                next(input)
        seq = ""
        for line in input:
                aa = line.split()
                for C in list:
                        if file[:-5] == C[:-2]:
                                chain = C[5]
                                continue
                if aa[2] == chain:
                        if aa[1] == "!" or aa[1] == "!*":
                                continue
                        aa = aa[3]
                        if aa.islower():
                                seq = seq+"C"
                                continue
                        seq = seq+aa
        name = sys.argv[2]
        name = name[:-6]
        initial = ">"+name+"\n"
        output.write(initial)
        output.write(seq)
        input.close()
        output.close()






if __name__ == "__main__":
        file = (sys.argv[1])
        file2 = (sys.argv[2])

fasta_dssp(file,file2)
