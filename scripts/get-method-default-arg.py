name_for_userid = {
    382: "Alice",
    590: "Bob",
    951: "Dilbert",
}


def greeting(userid):
    return "Hi %s!" % name_for_userid.get(userid, "there")


print(greeting(382))
# output: "Hi Alice!"

print(greeting(333333))
# output: "Hi there!"
