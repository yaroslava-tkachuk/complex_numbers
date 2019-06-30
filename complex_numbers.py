
# coding: utf-8

# In[1]:


'''This module contains a class representing complex numbers and basic arithmetic operations on them.'''


# In[2]:


import math


# In[9]:


class ZeroError(Exception):
    '''Error when calculating the argument of a complex number 0+0*i.'''
    def __init__(self):
        Exception.__init__(self, 'The complex number must be different from zero.')

class Complex(object):
    
    '''A class representing complex numbers.'''
    
    def __init__(self, re, im):
        self._re = re
        self._im = im
    
    @property
    def re(self):
        '''Returns the real part of a complex number.'''
        return self._re
    
    @property
    def im(self):
        '''Returns the imaginary part of a complex number.'''
        return self._im
    
    @re.setter
    def re(self, new_re):
        '''Sets the real part of a complex number.'''
        self._re = new_re
    
    @im.setter
    def im(self, new_im):
        '''Sets the imaginary part of a complex number.'''
        self._im = new_im
        
    def __add__(self, other):
        '''+ operation on complex numbers.'''
        new_re = self.re + other.re
        new_im = self.im + other.im
        my_sum = Complex(new_re, new_im)
        
        return my_sum
    
    def __iadd__(self, other):
        '''+= operation on complex numbers.'''
        new_re = self.re + other.re
        new_im = self.im + other.im
        my_sum = Complex(new_re, new_im)
        
        return my_sum
    
    def __sub__(self, other):
        '''- operation on complex numbers.'''
        new_re = self.re - other.re
        new_im = self.im - other.im
        my_diff = Complex(new_re, new_im)
        
        return my_diff
        
    def __isub__(self, other):
        '''-= operation on complex numbers.'''
        new_re = self.re - other.re
        new_im = self.im - other.im
        my_diff = Complex(new_re, new_im)
        
        return my_diff
    
    def __mul__(self, other):
        '''* operation on complex numbers.'''
        new_re = self.re * other.re - self.im * other.im
        new_im = self.re * other.im + self.im * other.re
        my_prod = Complex(new_re, new_im)

        return my_prod
    
    def __imul__(self, other):
        '''*= operation on complex numbers.'''
        new_re = self.re * other.re - self.im * other.im
        new_im = self.re * other.im + self.im * other.re
        my_prod = Complex(new_re, new_im)

        return my_prod
    
    def __truediv__(self, other):
        '''/ operation on complex numbers.'''
        re_num = self.re * other.re - self.im * (-1) * other.im
        im_num = self.re * (-1) * other.im + self.im * other.re
        denom = other.re**2 + other.im**2
        new_re = re_num / denom
        new_im = im_num / denom
        
        my_quot = Complex(new_re, new_im)

        return my_quot
    
    def __itruediv__(self, other):
        '''/= operation on complex numbers.'''
        re_num = self.re * other.re - self.im * (-1) * other.im
        im_num = self.re * (-1) * other.im + self.im * other.re
        denom = other.re**2 + other.im**2
        new_re = re_num / denom
        new_im = im_num / denom
        
        my_quot = Complex(new_re, new_im)

        return my_quot
    
    @property
    def module(self):
        '''Module of a complex number.'''
        return math.sqrt((self.re)**2 + (self.im)**2)
    
    @property
    def argument(self):
        '''Argument of a complex number.'''
        if self.re > 0:
            if math.degrees(math.atan(self.im/self.re)) < 0:
                return 2*math.pi+math.atan(self.im/self.re)
            else:
                return math.atan(self.im/self.re)
                
        elif self.re < 0:
            return math.pi+math.atan(self.im/self.re)
        else:
             raise ZeroError
    
    @property
    def trigon(self):
        '''Trigonometric form of a complex number.'''
        return '|{0:+.2f}|*cos({1:+.2f})+i*sin({2:+.2f})'.format(self.module, self.argument, self.argument)
    
    def power(self, n):
        '''Power of a complex number.'''
        if ((self.re != 0) and (self.im != 0)):
            new_re = self.module**n * math.cos(n*self.argument)
            new_im = self.module**n * math.sin(n*self.argument)
            wyn = Complex(new_re, new_im)
            return wyn
        else:
            return Complex(0, 0)
    
    def root(self, n):
        '''Root of a complex number.'''
        if ((self.re != 0) and (self.im != 0)):
            roots = []
            for k in range(n):
                new_re = self.module**(1/n) * math.cos((self.argument + 2*k*math.pi)/n)
                new_im = self.module**(1/n) * math.sin((self.argument + 2*k*math.pi)/n)
                my_root = Complex(new_re, new_im)
                roots.append(my_root)
            return roots
        else:
            return [Complex(0, 0)]
        
    def __str__(self):
        '''Returns a string of a complex number.'''
        return '{0:+.2f}{1:+.2f}*i'.format(self.re, self.im)
    
    def __repr__(self):
        '''Returns a string of a complex number.'''
        return self.__str__()

