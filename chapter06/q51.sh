pcregrep -o ".+?[.;:?!]\s(?=[A-Z])" data/nlp.txt |
pcregrep -o "[a-zA-Z]+?[\s\.]" | tr "." "\n" | tee work/nlp_parsed.txt | head -n30