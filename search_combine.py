import searcher
import indexer
import data_load

fdict = indexer.indexer_data("fortunedata.db","raw_data.txt")
searcher.searchfile("fortunedata.db")
