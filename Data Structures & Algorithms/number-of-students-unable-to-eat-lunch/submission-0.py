class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        #0 -- circular
        #1 -- square
        num_stud_one = 0
        num_stud_zero = 0
       
        for i in students:
            if i==1:
                num_stud_one+=1
            else:
                num_stud_zero+=1
        for j in sandwiches:
            if j==1:
                if num_stud_one==0:
                    break
                num_stud_one-=1
              
                
            elif j==0:
                if num_stud_zero==0:
                    break
                num_stud_zero-=1
                

        return num_stud_one+num_stud_zero
    