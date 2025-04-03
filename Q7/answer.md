## QUESTION
whats the output of the following code:
fruits = ['banana', 'mango', 'apple', 'pineapple', 'watermelon', 'avocado']
    for idx, fruit in enumerate(fruits, -2):
        print(idx, fruit)


``Output code ``

-2 banana
-1 mango
0 pineaple
1 watermelon
2 avocado

``Explanation``

Using the for loop to iterate over the list print out elements, the enumerate helps prints indexs, its default value starts from 0 but can be altred as seen above