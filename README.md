# CRFSuite

You can find binaries for Linux 64bit on the CRFsuite page. As discussed in the tutorial, each item in the sequence is represented by one line in the data. Each item begins with a label followed by features separated by tab characters. An empty line indicates the end of a sequence (e.g., conversation). The features are binary. The presence of a feature on a line indicates that it is true for this item. Absence indicates that the feature would be false. Here is a training example using features for whether a particular token is present or not in an utterance with the dialogue act "sv".

sv TOKEN_i TOKEN_certainly TOKEN_do TOKEN_.
For testing, you don't have the labels so you should make up labels (e.g., UNK) so that the format will be the same. Do not use the characters ":" or "\" in your feature names.

What to do

Your main goal is produce a set of dialogue act tags for the unlabeled data. You will use your labeled data ("training data set") to pick the best features for this task. In assignment 2, you simply split the labeled data by randomly putting 25% of the examples in the development set and using the rest to train your classifier. In this case, you would include entire conversations in either the training or development sets. In this assignment, it is up to you how you use your labeled data to evaluate different features. You could split the conversations and use a certain percentage for development, or you could use k-fold cross-validation.

You should try a set of features that we'll call baseline. In the baseline feature set, for each utterance you include:

a feature for whether or not the speaker has changed in comparision with the previous utterance.
a feature marking the first utterance of the dialogue.
a feature for every token in the utterance (see the description of CRFsuite for an example).
a feature for every part of speech tag in the utterance (e.g., POS_PRP POS_RB POS_VBP POS_.).
You'll need to create a Python program that converts a single CSV file (either labeled or not) into the baseline features in the data format for CRFsuite. To create a data file for training, you'll need to run this code on every file in the training set and combine the results. REMEMBER that each sequence must be separated by an empty line. Thus, there should be a blank line between the data from one file and the data from another file. To create a data file for development and testing, you'll need to follow the same procedure.

create_baseline_features.py CSV_file_name

the features in CRFsuite data format should be sent to STDOUT
You should try at least one other set of features that we'll call advanced. The advanced feature set should include more information than the baseline feature set. The idea is that you want to improve performance. As discussed in the grading section, part of your grade depends on developing a feature set better than the baseline. You'll need to create a Python program that converts a single CSV file (either labeled or not) into the advanced features in the data format for CRFsuite.

create_advanced_features.py CSV_file_name

the features in CRFsuite data format should be send to STDOUT
