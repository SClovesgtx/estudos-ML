library(CSeqpat)

setwd("/home/cloves/Documents/estudos-ML/Pattern-Mining/Mining-Quality-Phrases-from-Text-Data")
file_name = "reviews_sample.txt"

result = CSeqpat(filepath = file_name,
                 minsupport = 100,
                 phraselenmin = 1, phraselenmax = 99999,
                 docdelim = "\n")

write.table(result, file = "result.txt", sep = ":",
            row.names = FALSE)
