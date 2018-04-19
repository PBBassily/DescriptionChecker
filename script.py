import os, enchant ,re
def check_spellig(input_dir,file,output_dir) :
    global count
    dictionary =  enchant.Dict("en")
    desc = open(input_dir+"/"+file,"r").readline();
    desc_words = desc.split(" ")
    for i in range (0,len(desc_words))  :
        trimmed_word = re.sub("[^a-zA-Z0-9]","", desc_words[i])
        if len(trimmed_word)!=0 and dictionary.check(trimmed_word) == False and trimmed_word != "colorful":
            count = count + 1
            print file ," ==> " , trimmed_word , "( ",count," errors)"
            while(dictionary.check(desc_words[i]) == False):
                desc_words[i] = raw_input("write it correct : ")

    new_desc = ""
    for word in desc_words :
        new_desc = new_desc + " " + word
    new_desc = new_desc.strip()
    out_file = open(output_dir+"/"+file,"w+")
    out_file.write(new_desc)
    out_file.close()

    print file +" is done"

# main function
if __name__=="__main__":

    count = 0
    # output directory that will be created
    output_dir = "text_checked"
    # input directory of the dataset
    input_dir = "text"
    dir = os.getcwd()

    # create output_dir if it is not found
    if not os.path.exists(os.path.join(dir,output_dir)):
        os.mkdir(output_dir)

    # loop over all images of the dataset and modify
    for file in os.listdir(dir+"/"+input_dir):
        check_spellig(input_dir,file,output_dir)
