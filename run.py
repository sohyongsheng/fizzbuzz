def is_divisible_by(divisor):
    def is_divisible(dividend):
        return dividend % divisor == 0
    return is_divisible

class FizzBuzz:
    condition_to_string = {
        is_divisible_by(3): "Fizz",
        is_divisible_by(5): "Buzz",
        is_divisible_by(7): "Jazz",
    }

    def __init__(self, i):
        self.i = i

    def __str__(self):
        result = ""
        for is_divisible, s in self.condition_to_string.items():
            if is_divisible(self.i):
                result += s
        if not result:
            result = str(self.i)
        return result

if __name__ == '__main__':
    n = 105
    print([
        str(FizzBuzz(i)) 
        for i in range(1, n + 1)
    ])

