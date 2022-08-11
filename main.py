from wordhoard import Synonyms

synonym = Synonyms(search_string='mother')
synonym_results = synonym.find_synonyms()
print(synonym_results)
['ancestor', 'biological mother', 'birth mother', 'child-bearer', 'creator',
 'dam', 'female parent', 'forebearer', 'foster mother', 'ma', 'mama', 'mamma',
 'mammy', 'mater', 'mom', 'momma', 'mommy', 'mother-in-law', 'mum', 'mummy',
 'old lady', 'old woman', 'origin', 'para i', 'parent', 'predecessor',
 'primipara', 'procreator', 'progenitor', 'puerpera', 'quadripara',
 'quintipara', 'source', 'supermom', 'surrogate mother']
