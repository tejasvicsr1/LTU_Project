def print_func(engtags, engdata, g):
    g.write("English sentences and their POS tags.\n\n\n")
    for i in range(len(engtags)):
        if i != 501:
            g.write(str(i + 1) + ". " + str(engdata[i]) + "\n\n")
        g.write("TAGS:\n\n")
        for j in range(len(engtags[i]["word_tags"])):
            g.write("\t" + str(j + 1) + ". " + str(engtags[i]["word_tags"][j]["word"]) + " -\t" + str(engtags[i]["word_tags"][j]["POS_TAG"]) + '\n')
            if j == len(engtags[i]["word_tags"]) - 1:
                g.write('\n')