import numpy as np
import matplotlib.pyplot as plt


def function_to_integrate(x):
    return x**2

def analytic_integral_of_f(a=None, b=None):
    return (b**3 / 3) - (a**3 / 3)

def trapezoidal_rule(f, a=None, b=None, n=None):
    #generate linear set of n points starting at a, ending at b
    points = np.linspace(a,b,n)
    h = points[1]-points[0]    
    integral_approx = 0
    for point in points:
        integral_approx += ( (f(point)+f(point+h)) * (h/2) )
    return integral_approx

def lefthand_riemann(f, a=None, b=None, n=None):
    #generate linear set of n points starting at a, ending at b
    points = np.linspace(a,b,n)
    h = points[1]-points[0]    
    integral_approx = 0
    for point in points:
        integral_approx += f(point)*h
    #Fill this in
    return integral_approx

def simpson_rule(f, a=None, b=None, n=None):
    #generate linear set of n points starting at a, ending at b
    points = np.linspace(a,b,n)
    h = points[1]-points[0]    
    integral_approx = 0
    for point in points:
        integral_approx += (f(point-h) + 4*f(point/2) + f(point+h)) * h/3
    return integral_approx

def relative_error(true=None, estimate=None):
    return np.abs((true - estimate)/true)*100
    
def stepVsError(f, a, b, n):
    data = []
    xs = [10,100,1000,10000]
    for x in xs:
        numberOfSteps = x
        y = f(function_to_integrate, a=a, b=b, n=x)
        rows = (x, y)
        data.append(rows)
    return np.array(data)

if __name__ == "__main__":
    a = 0
    b = 1
    n = 10
    
    #calculate exact answer of integral
    exactAnswer = analytic_integral_of_f(a, b)
    print('Exact Answer = ', exactAnswer)

    #calculate array of left hand integral data for graphing
    lefthandIntegral = stepVsError(lefthand_riemann, a, b, n)
    #convert integral value into relative error
    lefthandIntegral[:,1] = relative_error(analytic_integral_of_f(a, b), lefthandIntegral[:,1])
    #plot LH integral
    plt.plot(lefthandIntegral[:,0], lefthandIntegral[:,1], color='black', label='LH')
    
    #calculate array of trapezoidal integral data for graphing
    trapezoidalIntegral = stepVsError(trapezoidal_rule, a, b, n)
    #convert integral value into relative error
    trapezoidalIntegral[:,1] = relative_error(analytic_integral_of_f(a, b), trapezoidalIntegral[:,1])
    #plot trapezoidalIntegral integral
    plt.plot(trapezoidalIntegral[:,0], trapezoidalIntegral[:,1], color='#1443ff', label='Trapezoidal')
    
    #calculate array of trapezoidal integral data for graphing
    simpsonIntegral = stepVsError(simpson_rule, a, b, n)
    #convert integral value into relative error
    simpsonIntegral[:,1] = relative_error(analytic_integral_of_f(a, b), simpsonIntegral[:,1])
    #plot trapezoidalIntegral integral
    plt.plot(simpsonIntegral[:,0], simpsonIntegral[:,1], color='#ff7017', label='Simpson')
    
    #adjust plot
    plt.title('Aidan Walk HW05')
    plt.xlabel('Number of Steps')
    plt.xscale('log')
    plt.yscale('log')
    plt.ylabel('Percent Error')
    plt.legend(loc='best')
    plt.show()
    
    