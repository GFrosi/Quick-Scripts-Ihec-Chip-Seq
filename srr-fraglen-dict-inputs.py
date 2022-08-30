import os
import sys

"""script to generate a csv file with the SRR 
and fragment length for each sample (srr) analyzed
with all and corresponding inputs. The output will
have three columns: SRR, frag all and frag cctrl. 
Save this file into a csv file and load on jupyter 
to get the GSM information by merge"""

file_name_all = open(sys.argv[1], 'r') #file with a list of paths to the SRR files (bam files) generated by ihec pipeline with all ctrls
fraglen_all = open(sys.argv[2], 'r') #file with a list of fragmente length (numbers) for samples analyzed with all ctrls
file_name_cctrl = open(sys.argv[3], 'r') #file with a list of paths to the SRR files (bam files) generated by ihec pipeline with corresponding ctrls
fraglen_cctrl = open(sys.argv[4], 'r') #file with a list of fragmente length (numbers) for samples analyzed with corresponding ctrls

#creating a dict with SRR and fraglen information for samples generated with all inputs
list_srr_all = []
list_frag_all = []

for name_all in file_name_all:
    f_name_all = name_all.strip()
    f_name_all = os.path.basename(f_name_all)
    SRR_name_all = f_name_all.split('_')[0]
    list_srr_all.append(SRR_name_all)

#print(list_srr_all)

for frag_all in fraglen_all:
    frg_all = str(frag_all.strip())
    list_frag_all.append(frg_all)

#print(list_frag_all)

#creating dict_all
dict_all = {k:v for k,v in zip(list_srr_all, list_frag_all)}
#print(dict_all)

# corresponding cctrls lists and dicts
list_srr_cctrl = []
list_frag_cctrl = []

for name_cctrl in file_name_cctrl:
    f_name_cctrl = name_cctrl.strip()
    f_name_cctrl = os.path.basename(f_name_cctrl)
    SRR_name_cctrl = f_name_cctrl.split('_')[0]
    list_srr_cctrl.append(SRR_name_cctrl)

#print(list_srr_cctrl)

for frag_cctrl in fraglen_cctrl:
    frg_cctrl = str(frag_cctrl.strip())
    list_frag_cctrl.append(frg_cctrl)

#print(list_frag_cctrl)

dict_cctrl = {k:v for k, v in zip(list_srr_cctrl, list_frag_cctrl)}
#print(dict_cctrl)


#dict_final = {}
for key in dict_all.keys():
    if key in dict_cctrl:
        print(key + ',' + dict_all[key] + ',' + dict_cctrl[key])
        
