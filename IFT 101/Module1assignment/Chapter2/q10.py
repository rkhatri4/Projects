test_score_1 = 21
test_score_2 = 22
test_score_3 = 25
test_score_4 = 23
test_score_5 = 27

average_test_score = (test_score_1 + test_score_2 +
                      test_score_3 + test_score_4 + test_score_5) / 5


def average_test_score_fn(score1, score2, score3, score4, score5):
    return (score1+score2+score3+score4+score5)/5


print(average_test_score)
print(average_test_score_fn(test_score_1, test_score_2,
      test_score_3, test_score_4, test_score_5))
