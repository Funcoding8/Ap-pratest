res_list = ["In N out","pandan Expess","McDonalds","subway"]

new_res = input("what restrant would you like to add to the list")

def rank_res(new_res,res_list):
    for i in (len(res_list)):
        renk = input ("Do you like A)" +new_res+ "more or B)" + res_list[i] + "more? A/B")

        if renk == "A":
            res_list.insert(i, new_res)
            return res_list

        elif rank =="B":
            continue

    res_list.append(new_res)
    return res_list
print("Your new renking is ",rank_res(new_res, res_list))

