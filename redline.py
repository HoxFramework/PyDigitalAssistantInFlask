import wolframalpha
global solution
solution = ["solution:"]
def red_line(question):
        try:
                #
                c = wolframalpha.Client('YOUR API KEY - get it for free at wolframalpha, just make an app')
                res = c.query(question)
                solve = next(res.results).text
                solver = solve
                solution.append(solver)
        except StopIteration:
                solution.append("Im sorry i do not know that.")
        except AttributeError:
                solution.append("Im sorry i do not know that.")



        
