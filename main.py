import masking_engine

def getOCROutput():
    """
    retrieve output from OCR engine
    """
    pass

def splitDocument():
    """
    split ocr output into sentences/(phrases?)
    """
    pass

def maskDocument():
    """
    mask each sentence as appropriate
    """
    pass

def correctDocument():
    """
    correct the masked ocr output
    """
    pass

def joinDocument():
    """
    join sentences/phrases(?) to form coherent document
    """
    pass

potentialDrawbacks = """
    -> too many masks in one input
    -> incorrect names
    -> incorrectly joined words due to omitted space
"""

# retrieve output from OCR engine
# we will call this output a document
ocr_output = getOCROutput()

# split document into sentences/(phrases?)
split_doc = splitDocument(ocr_output)

# mask each sentence as appropriate
meng = masking_engine.MaskingEngine()
masked_doc = maskDocument(split_doc)

# feed each sentence as input to post-correction model
    # get the top k predictions for each mask in a sentence
    # compare each of the k predictions with the masked output to obtain matched_character_count
    # select prediction with highest matched_character_count and replace
corrected_doc = correctDocument()

# join output as necessary to form a new document
final_doc = joinDocument()