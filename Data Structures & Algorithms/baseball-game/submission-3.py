class Solution:
    def calPoints(self, operations: List[str]) -> int:
        sum_of_scores = 0
        score_list = []
        for i in operations:
           
                
            if i=='+':
                score_list.append(int(score_list[len(score_list)-1]+score_list[len(score_list)-2]))
            elif i=='D':
                score_list.append(int(2*(score_list[len(score_list)-1])))
            elif i=='C':
                score_list.pop()
            else:
                score_list.append(int(i))
        for j in range(len(score_list)):
            sum_of_scores = sum_of_scores+int(score_list[j])
        return sum_of_scores