class Term:
    def __init__(self,coeffient,power):
        self.power =power
        self.coeffient = coeffient
    def add(self,term):
        if self.power != term.power:
            raise Exception('Powers are not the same')
        else:
            return Term(self.coeffient+term.coeffient,self.power)
    def p(self):
        return ' %sX%s' % (self.coeffient,self.power)

class Polynomial:
    def __init__(self,*terms):
        data = {}
        for term in terms:
            try:
                data[term.power]=data[term.power].add(term)
            except KeyError:
                data[term.power]=term
        terms =[r for k,r in data.iteritems() ]
        self.terms = list(terms)
        self.terms.sort(key=lambda x: x.power,reverse=True)
    def p(self):
        out =""
        for term in self.terms:
            out += " %sX%s"% (term.coeffient,term.power)
        return out

class JuryArray:
    def __init__(self,polynomial):
        self.polynomial = polynomial
