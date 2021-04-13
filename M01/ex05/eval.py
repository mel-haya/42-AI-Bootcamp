class Evaluator:
    def zip_evaluate(coefs, words):
        ret = 0.0
        if len(coefs) != len(words):
            return -1
        l = zip(coefs, words)
        for i in l:
            if not isinstance(i[1],str) or not isinstance(i[0],(int,float)):
                print('here')
                return -1
            ret += len(i[1]) * i[0]
        return ret

    def enumerate_evaluate(coefs, words):
        ret = 0.0
        if len(coefs) != len(words):
            return -1
        for i,word in enumerate(words):
            if not isinstance(word,str) or not isinstance(coefs[i],(int,float)):
                print('here')
                return -1
            ret += len(word) * coefs[i]
        print(ret)
        return ret

words = ["Le", "Lorem", "Ipsum", "est", "simple"]     
coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
Evaluator.enumerate_evaluate(coefs, words)