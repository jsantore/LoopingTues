import time
good_answers=["yes", "yup", "fine", "ok", "yeah"]
parent_answer = input("Can I have my candy now")
while parent_answer.lower() not in good_answers:
    parent_answer = input("ok so can I have cany NOW?")

for repeat in range(10):
    print("Hooray I will eat Candy for ever and ever")
    time.sleep(1)