
try: 
    from vcfParser import parse_vcf
except:
    print("awshucks_no_function")
try:
    parse_vcf("random_snippet.vcf")
except:
    print("achnodice_no_snippet")
parse_vcf("dbSNP_snippet.vcf")