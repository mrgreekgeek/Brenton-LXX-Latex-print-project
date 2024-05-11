filenames = ["GEN_src.tex",
"EXO_src.tex",
"LEV_src.tex",
"NUM_src.tex",
"DEU_src.tex",
"JOS_src.tex",
"JDG_src.tex",
"RUT_src.tex",
"1SA_src.tex",
"2SA_src.tex",
"1KI_src.tex",
"2KI_src.tex",
"1CH_src.tex",
"2CH_src.tex",
"EZR_src.tex",
"ESG_src.tex",
"JOB_src.tex",
"PSA_src.tex",
"PRO_src.tex",
"ECC_src.tex",
"SNG_src.tex",
"ISA_src.tex",
"JER_src.tex",
"LAM_src.tex",
"EZK_src.tex",
"DAG_src.tex",
"HOS_src.tex",
"JOL_src.tex",
"AMO_src.tex",
"OBA_src.tex",
"JON_src.tex",
"MIC_src.tex",
"NAM_src.tex",
"HAB_src.tex",
"ZEP_src.tex",
"HAG_src.tex",
"ZEC_src.tex",
"MAL_src.tex",
"1ES_src.tex",
"TOB_src.tex",
"JDT_src.tex",
"WIS_src.tex",
"SIR_src.tex",
"BAR_src.tex",
"LJE_src.tex",
"SUS_src.tex",
"BEL_src.tex",
"1MA_src.tex",
"2MA_src.tex",
"3MA_src.tex",
"4MA_src.tex",
"MAN_src.tex"]

# Open the destination file in write mode
with open('concatenated.tex', 'w', encoding="utf-8") as outfile:
    # Loop through each filename in the list
    for name in filenames:
        # Open each file in read mode
        with open(name, 'r', encoding="utf-8") as infile:
            # Read the data from the file and write it to the new file
            outfile.write(infile.read())
            # Add a newline character to separate the contents of different files
            outfile.write("\n")