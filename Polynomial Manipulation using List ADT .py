class Polynomial:
    def __init__(self, terms=None):
       
        self.terms = terms if terms else []

    def add(self, other):
        result = []
        i = j = 0
        while i < len(self.terms) and j < len(other.terms):
            coeff1, exp1 = self.terms[i]
            coeff2, exp2 = other.terms[j]

            if exp1 == exp2:
                result.append((coeff1 + coeff2, exp1))
                i += 1
                j += 1
            elif exp1 > exp2:
                result.append((coeff1, exp1))
                i += 1
            else:
                result.append((coeff2, exp2))
                j += 1

        
        result.extend(self.terms[i:])
        result.extend(other.terms[j:])

        return Polynomial(result)

    def multiply(self, other):
        result = {}
        for coeff1, exp1 in self.terms:
            for coeff2, exp2 in other.terms:
                new_coeff = coeff1 * coeff2
                new_exp = exp1 + exp2
                if new_exp in result:
                    result[new_exp] += new_coeff
                else:
                    result[new_exp] = new_coeff

               terms = [(c, e) for e, c in result.items()]
        terms.sort(key=lambda x: x[1], reverse=True)
        return Polynomial(terms)

    def display(self):
        poly_str = " + ".join([f"{coeff}x^{exp}" if exp != 0 else f"{coeff}"
                               for coeff, exp in self.terms if coeff != 0])
        return poly_str if poly_str else "0"



p1 = Polynomial([(3,2), (2,1), (5,0)])  
p2 = Polynomial([(1,1), (1,0)])         

print("P1 =", p1.display())
print("P2 =", p2.display())

sum_poly = p1.add(p2)
print("P1 + P2 =", sum_poly.display())

mul_poly = p1.multiply(p2)
print("P1 * P2 =", mul_poly.display())


