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
    def generate(self):
        line1 = [term.coeffient for term in reversed(self.polynomial.terms)]
        yield(line1)
        line2 =[term.coeffient for term in self.polynomial.terms]
        yield(line2)
        for line in self.next_line(line1,line2):
            yield line
    def next_line(self,line1,line2):
        if len(line1) > 1:
            line3 = []
            for n in range(len(line1)-1):
                m=n+1
                b=(line1[0]*line1[m])-(line1[m]*line2[0])
                line3.append(b)
            yield(line3)
            line4 = [num for num in reversed(line3)]
            yield(line4)
            for line in self.next_line(line3,line4):
                yield line
