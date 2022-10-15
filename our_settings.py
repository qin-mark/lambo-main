RESUME=True
from enum import Enum
AKT='MSDVAIVKEGWLHKRGEYIKTWRPRYFLLKNDGTFIGYKERPQDVDQREAPLNNFSVAQCQLMKTERPRPNTFIIRCLQWTTVIERTFHVETPEEREEWTTAIQTVADGLKKQEEEEMDFRSGSPSDNSGAEEMEVSLAKPKHRVTMNEFEYLKLLGKGTFGKVILVKEKATGRYYAMKILKKEVIVAKDEVAHTLTENRVLQNSRHPFLTALKYSFQTHDRLCFVMEYANGGELFFHLSRERVFSEDRARFYGAEIVSALDYLHSEKNVVYRDLKLENLMLDKDGHIKITDFGLCKEGIKDGATMKTFCGTPEYLAPEVLEDNDYGRAVDWWGLGVVMYEMMCGRLPFYNQDHEKLFELILMEEIRFPRTLGPEAKSLLSGLLKKDPKQRLGGGSEDAKEIMQHRFFAGIVWQHVYEKKLSPPFKPQVTSETDTRYFDEEFTAQMITITPPDQDDSMECVDSERRPHFPQFSYSASGTA'
# AKT='MSDVA'
#Example: anchor_before='MDH:'. If you don't use anchor, please set anchor to ''
# anchor_before='MPSRLEEELRRRLTEPGGGGSGGGGSGGGGSGGGGS'
anchor_before=''
#Example: anchor_after=':ASDAD'. If you don't use anchor, please set anchor to ''
# anchor_after='GGGGSGGGGSGGGGSGGGGSGGGGSEVQLQESGGGLVQPGGSLRLSCTASGVTISALNAMAMGWYRQAPGERRVMVAAVSERGNAMYRESVQGRFTVTRDFTNKMVSLQMDNLKPEDTAVYYCHVLEDRVDSFHDYWGQGTQVTVSS'
anchor_after=''
#please select two metrics from [energy, SASA, ratio_AKT, ratio_AKT_domain, ratio_peptide]
scoring_metrics=['SASA','ratio_peptide']
#weight of [ratio_AKT, ratio_AKT_domain, ratio_peptide]
ratio_weight=100
#sleep time(s) when colabfold run failed
sleep_time=100
#the number of trying cycle when colabfold running failed
try_num=5
#ratio of binding sites settings
cutoff=5
AKT_domain_start=149
AKT_domain_end=409