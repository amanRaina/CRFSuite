import csv
import glob
import os
import sys


def get_utterances_from_file(dialog_csv_file):
    """Returns a list of DialogUtterances from an open file."""
    reader = csv.DictReader(dialog_csv_file)
    return [_dict_to_dialog_utterance(du_dict) for du_dict in reader]

def get_utterances_from_filename(dialog_csv_filename):
    """Returns a list of DialogUtterances from an unopened filename."""
    with open(dialog_csv_filename, "r") as dialog_csv_file:
        return get_utterances_from_file(dialog_csv_file)

DialogUtterance = namedtuple(
    "DialogUtterance", ("act_tag", "speaker", "pos", "text"))

DialogUtterance.__doc__ = """\
An utterance in a dialog. Empty utterances are None.

act_tag - the dialog act associated with this utterance
speaker - which speaker made this utterance
pos - a list of PosTag objects (token and POS)
text - the text of the utterance with only a little bit of cleaning"""

PosTag = namedtuple("PosTag", ("token", "pos"))

PosTag.__doc__ = """\
A token and its part-of-speech tag.

token - the token
pos - the part-of-speech tag"""

def _dict_to_dialog_utterance(du_dict):
    """Private method for converting a dict to a DialogUtterance."""

    # Remove anything with 
    for k, v in du_dict.items():
        if len(v.strip()) == 0:
            du_dict[k] = None

    # Extract tokens and POS tags
    if du_dict["pos"]:
        du_dict["pos"] = [
            PosTag(*token_pos_pair.split("/"))
            for token_pos_pair in du_dict["pos"].split()]
    return DialogUtterance(**du_dict)

def create_training(doc):
    named_tuple=get_utterances_from_filename(doc)
    # with open(sys.argv[2],'a') as op:
    count3=0
    speaker=None

    for utterance in named_tuple:
        print(utterance.act_tag+"\t",end=""); 
        if(count3==0):
            print("_BOS_"+"\t",end="")
        if(utterance.speaker!=speaker or speaker==None): 
            print("speaker"+"\t",end="");
        speaker=utterance.speaker    
        count=0
        if(utterance.pos is not None):
            for tokens in utterance.pos:
                if(tokens.token==":"):
                    print("w_"+"colon"+"\t",end="")
                else:
                    print("w_"+tokens.token+"\t",end=""); 
                count=count+1;
            count1=0;
            for pos in utterance.pos:
                if(pos.pos==":"):
                    print("pos_"+"colon"+"\t",end="")
                else:    
                    print("pos_"+pos.pos+"\t",end=""); 
                count1=count1+1;    
            print("\n",end="")
        else:
            print("\n",end="") 
        count3=count3+1    
    print("\n",end="")        

def main():
    # for filename in sorted(os.listdir(sys.argv[1])):
        # print(filename)
    create_training(sys.argv[1])

if __name__=="__main__":
    main();